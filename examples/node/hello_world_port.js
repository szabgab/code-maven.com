var http = require('http');

var port = 8081;

var s = http.createServer(function(request, response) {
    response.writeHead(200);
    response.write("Hello World");
    response.end();
});

s.listen(port);

console.log("Listening on http://127.0.0.1:" + port + "/");

