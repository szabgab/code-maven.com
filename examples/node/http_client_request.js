var http = require('http');

var port = 8081;

var s = http.createServer();
s.on('request', function(request, response) {
    response.writeHead(200);
    console.log(request.method);
    console.log(request.headers);
    console.log(request.url);
    response.write('hi');
    response.end();
});

s.listen(port);
console.log('Browse to http://127.0.0.1:' + port);


