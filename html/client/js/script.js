// ref: https://github.com/colinbdclark/osc.js/

// ----- OSC -----

// use localhost when only connecting internally
let host = "localhost"

// use the server machine's IP address when connecting external devices
//let host = "10.10.0.159"

let oscPort = new osc.WebSocketPort({
    url: "ws://"+host+":8081",
    metadata: true
})

oscPort.on("message", function (message) {
    console.log("received osc: ", message)
    document.getElementById("message").innerText = message.address + " " + JSON.stringify(message.args)
})

oscPort.open()

// ----- UI -----

function sendMessage() {
    oscPort.send({
        address: "/bar",
        args: [
            {type: "s", value: "helloworld"},
            {type: "i", value: 1234},
            {type: "f", value: 567.89}
        ]
    })
}
