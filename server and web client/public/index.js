body = document.querySelector("body")

const ws = new WebSocket('ws://127.0.0.1:3000');

const currentUrl = window.location.href;
let url = new URL(currentUrl);
console.log("url", url);
extraPath = url.pathname.substring(1);
console.log("path", extraPath == false)

const clientID = uniqueID();
let messageID = [];
console.log(clientID)

let slashCount = (extraPath.match(/\//g) || []).length;
console.log(slashCount);

ws.addEventListener('open', function open() {
    if (extraPath) {
        if (slashCount === 2) {
            messageID = [];
            messageID.push(clientID);
            messageID.push("device");
            messageID.push(extraPath);
            ws.send(JSON.stringify(messageID));
        } else if (slashCount === 4) {
            messageID = [];
            messageID.push(clientID);
            messageID.push("attribute_subscription");
            messageID.push(extraPath);
            ws.send(JSON.stringify(messageID));
        }

    } else {
        messageID = [];
        messageID.push(clientID);
        messageID.push("client");
        ws.send(JSON.stringify(messageID));
    }
});

ws.addEventListener('message', function incoming(data) {
    console.log(data['data']);
    document.getElementById("json").innerHTML = data["data"];
});

ws.addEventListener('close', function open() {
    ws.send("close");
});

function printDevices(deviceList){
    deviceList.forEach(d => {
        printMessage(d);
    });
}

window.onbeforeunload = closeWindow;
function closeWindow(){
    messageID = [];
    messageID.push(clientID);
    messageID.push("close");
    ws.send(JSON.stringify(messageID));
    return null;
}

function printMessage(message){
    const div = document.createElement("div");
    div.innerHTML = JSON.stringify(message, undefined, 4);
    // div.appendChild(text);
    document.body.appendChild(div);
}


function uniqueID() {
    const id = Math.floor(Math.random() * Date.now());
    return id.toString();
}