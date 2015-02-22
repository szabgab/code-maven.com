if (process.argv.length <= 2) {
    console.log("Usage: " + __filename + " SOME_PARAM");
    process.exit(-1);
}

var param = process.argv[2];

console.log('Param: ' + param);


