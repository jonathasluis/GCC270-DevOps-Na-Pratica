var http = require('http');

http.createServer(function (req, res) {
  res.write('Olá, Mundo!'); 
  res.end(); 
}).listen(8080);