#! /usr/bin/env python3
#
# Copyright (c) 2021 ZKM | Hertz-Lab
# Dan Wilcox <dan.wilcox@zkm.de>
#
# BSD Simplified License.
# For information on usage and redistribution, and for a DISCLAIMER OF ALL
# WARRANTIES, see the file, "LICENSE.txt," in this distribution.
#
# This code has been developed at ZKM | Hertz-Lab as part of „The Intelligent 
# Museum“ generously funded by the German Federal Cultural Foundation.
#
# TODO:
# * add signal handler to exit gracefully? probably needs nonblocking io...
# * verbose event messaging instead of commenting print() out
# * replace SimpleWebSocketServer with websockets lib?
# * replace UDP code with asyncio versions

from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import socket, threading, argparse

##### parser

parser = argparse.ArgumentParser(description="udp <-> websocket relay server")
parser.add_argument(
    "--wshost", action="store", dest="wshost",
    default="localhost", help="websocket host ie. ws://####:8081 default: localhost")
parser.add_argument(
    "--wsport", action="store", dest="wsport",
    default=8081, type=int, help="websocket port ie. ws://localhost:####, default: 8081")
parser.add_argument(
    "--recvaddr", action="store", dest="recvaddr",
    default="localhost", help="udp receive addr, default: localhost")
parser.add_argument(
    "--recvport", action="store", dest="recvport",
    default=9999, type=int, help="udp receive port, default: 9999")
parser.add_argument(
    "--sendaddr", action="store", dest="sendaddr",
    default='localhost', help="udp send port, default: localhost")
parser.add_argument(
    "--sendport", action="store", dest="sendport",
    default=8888, type=int, help="udp send addr, default: 8888")

##### UDP

# simple UDP sender socket wrapper
class UDPSender(object):

    # init with address, port, and optional brodcast (aka multicast)
    def __init__(self, address, port, broadcast=False):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.setblocking(0)
        if broadcast:
            self._sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.address = address
        self.port = port

    # send raw data 
    def send(self, data):
        self._sock.sendto(data, (self.address, self.port))

# simple UDP receiver socket wrapper
class UDPReceiver(object):

    def __init__(self, port, address="localhost"):
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._sock.bind((address, port))
        self.running = True

    def listenforever(self, wsserver):
        print("udp: starting")
        while self.running:
            data, addr = self._sock.recvfrom(1024)
            #print("udp: received ", data)
            for client in wsserver.connections:
                #print(wsserver.connections[client], "sending")
                wsserver.connections[client].sendMessage(data)

##### WebSocket

# websocket -> UDP relay implementation
class WSServer(WebSocket):

    # setup UDP sender object
    def __init__(self, server, sock, address):
        WebSocket.__init__(self, server, sock, address)
        self.udpsender = UDPSender(args.sendaddr, args.sendport)

    # client connect callback
    def handleConnected(self):
        print("websocket: connected", self.address)

    # simply relay raw messages to UDP client
    def handleMessage(self):
        #print("websocket: received ", self.data)
        self.udpsender.send(self.data)

    # client disconnect callback
    def handleClose(self):
        print("websocket: disconnected", self.address)

##### GO

args = parser.parse_args()
print(f"send -> udp {args.recvaddr}:{args.recvport} -> ws://{args.wshost}:{args.wsport}")
print(f"recv <- udp {args.sendaddr}:{args.sendport} <- ws://{args.wshost}:{args.wsport}")

# websocket server
wsserver = SimpleWebSocketServer(args.wshost, args.wsport, WSServer)

# UDP server
udpserver = UDPReceiver(args.recvport, args.recvaddr)
def listenUDP():
    udpserver.listenforever(wsserver)
threading.Thread(target=listenUDP).start()

print("websocket: starting")
wsserver.serveforever()
