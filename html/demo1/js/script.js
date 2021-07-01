// ref: https://github.com/colinbdclark/osc.js/

let greeting = ["...", "Hello", "Guten Tag", "Bonjour", "Hola"]

// OSC

var oscPort = new osc.WebSocketPort({
    url: "ws://localhost:8081",
    metadata: true
})

oscPort.on("message", function (message) {
    console.log("received osc: ", message)
   	if(message.address == "/detecting") {
   		if(message.args[0].value == 0) {
   			document.getElementById("detecting").style.display = "none"
   		}
   		else {
   			document.getElementById("detecting").style.display = "inline"
   		}
   	}
   	else if(message.address == "/lang") {
   		document.getElementById("greeting").innerHTML = greeting[message.args[0].value]
        document.getElementById("flag").innerHTML = flag[message.args[0].value]
   	}
})

oscPort.open()
