const WebSocket = require('ws');

const ws = new WebSocket('ws://127.0.0.1:3000/');

ws.on('open', function open() {
  ws.send('Hello, I am the client!');
});

ws.on('message', function incoming(data) {
  console.log(data); 
});




