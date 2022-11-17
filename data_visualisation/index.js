const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server, { cors: { origin: '*' }});
var net = require('net');

var net_server = net.createServer();

net_server.listen(4000, '127.0.0.1');

net_server.on('connection', function(socket) {
    console.log('Connected: ' + socket.remoteAddress + ':' + socket.remotePort);
    socket.on('data', function(data) {
        console.log('Received: ' + data);
    });
});

app.set('view engine', 'ejs');

app.get('/home', (req, res) => {
    res.render('home');
});

server.listen(3001);

io.on('connection', (socket) => {
    socket.emit('message', {type: 'init'});
    socket.on('message', (message) => {
        socket.emit('message', message);
    });
});