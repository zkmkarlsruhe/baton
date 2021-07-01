baton
=====

Relay messages between UDP and a websocket. Faster together.

This code base has been developed by [ZKM | Hertz-Lab](https://zkm.de/en/about-the-zkm/organization/hertz-lab) as part of the project [»The Intelligent Museum«](#the-intelligent-museum). 

Copyright (c) 2021 ZKM | Karlsruhe.  
Copyright (c) 2021 Dan Wilcox.  

BSD Simplified License.

Description
-----------

This script acts as a websocket relay server which creates a local websocket and forwards messages to/from a set of UDP ports. This is useful for creative coding tools which work with OSC (Open Sound Control) messages natively, but do not have built-in websocket support.

Dependencies
------------

  * Python 3
  * [simple-websocket-server](https://github.com/dpallot/simple-websocket-server)

Setup
-----

Install Python 3, if not already available:

```shell
brew install python3
```

Create a virtual environment for the script's dependencies and activate it:

```shell
python3 -m venv venv-baton
source venv-baton/bin/activate
```

Install the websocket server library via pip:

```shell
pip3 install git+https://github.com/dpallot/simple-websocket-server.git
```

Running
-------

Make sure to activate the virtual environment before the first run in a new commandline session:

    source venv-baton/bin/activate

Next, start the server on the commandline via:

    ./baton.py

It can simply sit in the background and automatically handles the websocket connection. Websocket clients can then connect to send/receive messages whiel baton is active.

To configure the send/receive address and ports, see the commandline argument help for baton by running:

    ./baton.py -h

To stop baton, use CTRL+C to issue an interrupt signal. You need to do this a couple of times until it exits completely.

When finished, deactivate the virtual environment with:

    deactivate

Example Clients
------------

A couple of example clients are included:

* html/client: HTML+JS websocket client, open index.html in your browser
* pd/osclient.pd: Pure Data patch which sends and receives OSC messages over UDP 

Both examples should work together with the default address & ports on the same localhost:

    pd/client.pd <-UDP-> baton.py <-WS-> html/client/index.html

First start baton, then start the clients.

To connect clients running on different computers, you may need to change the websocket and/or UDP address and port values.

The Intelligent Museum
----------------------

An artistic-curatorial field of experimentation for deep learning and visitor participation

The [ZKM | Center for Art and Media](https://zkm.de/en) and the [Deutsches Museum Nuremberg](https://www.deutsches-museum.de/en/nuernberg/information/) cooperate with the goal of implementing an AI-supported exhibition. Together with researchers and international artists, new AI-based works of art will be realized during the next four years (2020-2023).  They will be embedded in the AI-supported exhibition in both houses. The Project „The Intelligent Museum” is funded by the Digital Culture Programme of the [Kulturstiftung des Bundes](https://www.kulturstiftung-des-bundes.de/en) (German Federal Cultural Foundation) and funded by the [Beauftragte der Bundesregierung für Kultur und Medien](https://www.bundesregierung.de/breg-de/bundesregierung/staatsministerin-fuer-kultur-und-medien) (Federal Government Commissioner for Culture and the Media).

As part of the project, digital curating will be critically examined using various approaches of digital art. Experimenting with new digital aesthetics and forms of expression enables new museum experiences and thus new ways of museum communication and visitor participation. The museum is transformed to a place of experience and critical exchange.

![Logo](media/Logo_ZKM_DMN_KSB.png)
