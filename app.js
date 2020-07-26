var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var port = process.env.PORT || 3000;
const user = '(Anonymus) ';

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', (socket) => {
  console.log('user conect');
  socket.on('chat message', (msg) => {
    msg = user + msg
    io.emit('chat message', msg);
  });
  socket.on('prueba', (msg) => {
    console.log(msg);
  });
  socket.on('disconnect', () => {
    console.log('user disconnected');
  });
});

http.listen(port, function(){
  console.log('listening on *:' + port);
});
