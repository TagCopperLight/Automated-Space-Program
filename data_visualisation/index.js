const express = require('express');
const app = express();
const server = require('http').createServer(app);
const io = require('socket.io')(server, { cors: { origin: '*' }});
var net = require('net');
const { SliceArray } = require('slice');

var net_server = net.createServer();

net_server.listen(4000, '127.0.0.1');

var data_buffer = SliceArray();

net_server.on('connection', function(socket) {
    socket.on('data', function(data) {
        data = data.toString().split('eof');
        data.pop();

        data.forEach(function (item) {
            item = JSON.parse(item);
            if (item.type == 'reset'){
                io.sockets.emit('message', {type: 'reset'});
            } else {
                data_buffer.push(item);
            }
        });
    });
    socket.on('close', function() {});
});

app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/public'));

app.get('/home', (req, res) => {
    res.render('home');
});

server.listen(3001);

io.on('connection', (socket) => {
    socket.emit('message', {type: 'init'});
    socket.on('message', function() {
        socket.emit('message', {type: 'data', data_list: data_buffer[[,,Math.ceil(data_buffer.length + 0.1 / 11)]]});

        data_buffer.length = 0;
    });
});