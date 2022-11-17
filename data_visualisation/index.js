const { json } = require('express');
const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server, { cors: { origin: '*' }});
var net = require('net');

var net_server = net.createServer();

net_server.listen(4000, '127.0.0.1');

var global_data = {type: 'void'};

net_server.on('connection', function(socket) {
    console.log('Client connected');
    socket.on('data', function(data) {
        //convert the ArrayBuffer to json
        global_data = JSON.parse(data);
    });
    socket.on('close', function() {
        global_data = {type: 'void'}
    });
});

net_server.on('error', function() {
    console.log('Connection closed');
});

app.set('view engine', 'ejs');

app.get('/home', (req, res) => {
    res.render('home');
});

server.listen(3001);

io.on('connection', (socket) => {
    socket.emit('message', {type: 'init'});
    socket.on('message', (message) => {
        socket.emit('message', global_data);
    });
});