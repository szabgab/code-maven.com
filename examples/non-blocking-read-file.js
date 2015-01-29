var fs = require('fs');

fs.readFile('DATA', 'utf8', function(err, contents) {
    console.log(contents);
});

console.log('after calling readFile');

