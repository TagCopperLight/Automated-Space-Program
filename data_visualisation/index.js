const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server, { cors: { origin: '*' }});
var net = require('net');

var net_server = net.createServer();

net_server.listen(4000, '127.0.0.1');

var global_data = {type: 'void'};
var saved_data = [
    {"type": "data","data_type": ["altitude","velocity"],"data": {
        "altitude": {
            "time": 0,
            "altitude": 75
        },
        "velocity": {
            "time": 0,
            "velocity": 0
        },
        "thrust": {
            "time": 0,
            "thrust": 0
        },
        "fuel": {
            "time": 0,
            "fuel": 100
        }
    }},
    {"type": "data","data_type": ["altitude","velocity"],"data": {
        "altitude": {
            "time": 10,
            "altitude": 80
        },
        "velocity": {
            "time": 10,
            "velocity": 5
        },
        "thrust": {
            "time": 10,
            "thrust": 10
        },
        "fuel": {
            "time": 10,
            "fuel": 50
        }
    }}
]

net_server.on('connection', function(socket) {
    socket.on('data', function(data) {
        data = JSON.parse(data);
        if (data.type == 'reset'){
            saved_data = [];
            global_data = {type: 'void'};
        } else {
            global_data = data;
            saved_data.push(data);
        }
    });
    socket.on('close', function() {
        global_data = {type: 'void'}
    });
});

app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/public'));

app.get('/home', (req, res) => {
    res.render('home');
});

server.listen(3001);

io.on('connection', (socket) => {
    socket.emit('message', {type: 'init', data: saved_data});
    socket.on('message', function() {
        socket.emit('message', global_data);
    });
});