const WebSocket = require('ws');
const mysql = require('mysql');
const MySQLEvents = require('@rodrigogs/mysql-events');
const express = require('express');
const path = require('path');

const app = express();
const server = require('http').createServer(app);

const PORT = 3000;

const wss = new WebSocket.Server({ noServer: true });

let wsClients = [];

app.use(express.static(path.join(__dirname, 'public')));

app.get('/*', (req, res) => {
  res.sendFile("/public/index.html", { root: __dirname })
})

// app.get('/*/*/*', (req, res) => {
//   res.sendFile(__dirname + '/public/index.html');
// })

conn = {
  host: "127.0.0.1",
  user: "tango",
  database: "tango",
  password: "tango",
  port: 3306
};

const c = mysql.createConnection(conn);

wss.on('connection', function connection(ws, req) {
    ws.on('message', function incoming(message) {
      const messageObject = JSON.parse(message);
      const clientID = messageObject[0];
;
      switch (messageObject[1]) {
        case "client":
          wsClients.push([ws, clientID, "root"]);
          selectDeviceNames(c,ws);
          break;
        case "close": 
          wsClients = wsClients.filter((a) => {
            return a[1] != clientID;
          })

          break;
        case "device": 
          wsClients.push([ws, clientID, "device", messageObject[2]]);
          selectDeviceInfo(c, ws, messageObject[2])
          break;
        case "attribute_subscription": 
          wsClients.push([ws, clientID, "attribute_value", messageObject[2]]);
          sendAttribute(ws, "unknown");
          break;
        case "attribute_value":
          wsClients.forEach(cl => {
            console.log("CLIENT: ", cl);
            if (cl[2] === "attribute_value" && cl[3] === messageObject[0] ) {
              sendAttribute(cl[0], messageObject[2]);
            }
          });
          
          break;
        default:
          console.log('Some other message arrived');
      }
      
      console.log(wsClients);
      console.log('received: %s', message);
    });
    
    // ws.send('The WebSocket server greets you');
    
    
});

server.listen(PORT, () => console.log(`Lisening on port: ${PORT}` ));
server.on('upgrade', (request, socket, head) => {
  wss.handleUpgrade(request, socket, head, socket => {
    wss.emit('connection', socket, request);
  });
});


console.log((new Date()) + " Server is listening to the port " + PORT)

const program = async () => {

  const instance = new MySQLEvents(c, {
    startAtEnd: true,
    excludedSchemas: {
      mysql: true,
    },
  });

  await instance.start();

  instance.addTrigger({
    name: 'TEST',
    expression: '*',
    statement: MySQLEvents.STATEMENTS.ALL,
    onEvent: (event) => { // You will receive the events here
      console.log(event);
      wsClients.forEach(client => {
        selectDeviceNames(c,ws);
      });
      
    },
  });
  
  instance.on(MySQLEvents.EVENTS.CONNECTION_ERROR, console.error);
  instance.on(MySQLEvents.EVENTS.ZONGJI_ERROR, console.error);
};

program()
  .then(() => console.log('Waiting for database events...'))
  .catch(console.error);

async function selectDeviceNames(c, w){
  c.query('SELECT name FROM device',(err,rows)=>{
    if(!err){
      let result = []
      let obj;
      rows.forEach(row => {
        obj = {}
        obj['name'] = row['name'];

        let host = server.address().address;
        let port = server.address().port;
        if (host === "::") {host = "localhost"};
        obj['address'] = 'http://' + host + ':' + port + '/' + row['name'];
        result.push(obj);
      });

      // console.log(result);
      // console.log(JSON.stringify( result, null, 4 ));
      let rootClients = wsClients.filter((a) => {
        return a[2] == "root"
      })

      rootClients.forEach(client => {
        client[0].send(JSON.stringify( result, null, 4 ));
      });
      

    } else {
      let err = {};
      err['error'] = 'Database connection failed';
      w.send(JSON.stringify( err, null, 4 ));
    }
  });
}


async function selectDeviceInfo(c, w, device){
  c.query(`SELECT * FROM tango.device WHERE name = '${device}'`,(err,rows)=>{
    if(!err){
      console.log("fsdfsdfsdfsdfsDDDDDDDD", rows);
      if (rows.length > 0 ){
        w.send(JSON.stringify( rows[0], null, 4 ));
      } else {
        let err = {};
        err['error'] = 'This object does not exist in the database';
        w.send(JSON.stringify( err, null, 4 ));
      }
      
 
    } else {
      let err = {};
      err['error'] = 'This object does not exist in the database';
      w.send(JSON.stringify( err, null, 4 ));

    }
  });
}

async function sendAttribute(w, value){
  let attrMessage = {};
  attrMessage["value"] = value;
  attrMessage = JSON.stringify( attrMessage, null, 4 )
  w.send(attrMessage);
}