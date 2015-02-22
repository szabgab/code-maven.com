var http = require('http');

var s = http.createServer(function(request, response) {
    response.writeHead(200);
    response.write("Hello World");
    response.end();
});

s.listen(8080);

console.log("Listening on http://127.0.0.1:8080/");
