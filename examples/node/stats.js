var fs = require('fs');

if (process.argv.length <= 2) {
    console.log("Usage: " + __filename + " path/to");
    process.exit(-1);
}

var path = process.argv[2];

fs.stat(path, function(err, stats) {
    console.log(path);
    console.log();
    console.log(stats);
    console.log();

    if (stats.isFile()) {
        console.log('    file');
    }
    if (stats.isDirectory()) {
        console.log('    directory');
    }

    console.log('    size: ' + stats["size"]);
    console.log('    mode: ' + stats["mode"]);
    console.log('    others eXecute: ' + (stats["mode"] & 1 ? 'x' : '-'));
    console.log('    others Write:   ' + (stats["mode"] & 2 ? 'w' : '-'));
    console.log('    others Read:    ' + (stats["mode"] & 4 ? 'r' : '-'));

    console.log('    group eXecute:  ' + (stats["mode"] & 10 ? 'x' : '-'));
    console.log('    group Write:    ' + (stats["mode"] & 20 ? 'w' : '-'));
    console.log('    group Read:     ' + (stats["mode"] & 40 ? 'r' : '-'));

    console.log('    owner eXecute:  ' + (stats["mode"] & 100 ? 'x' : '-'));
    console.log('    owner Write:    ' + (stats["mode"] & 200 ? 'w' : '-'));
    console.log('    owner Read:     ' + (stats["mode"] & 400 ? 'r' : '-'));


    console.log('    file:           ' + (stats["mode"] & 0100000 ? 'f' : '-'));
    console.log('    directory:      ' + (stats["mode"] & 0040000 ? 'd' : '-'));



});


