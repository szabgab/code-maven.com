function add(x, y) {
    console.trace('add called with ', x, 'and', y);
    return x+y;
}

function calc() {
    return add(8, 11) + add(9, 14);
}

function main() {
    var x = add(2, 3);
    var y = calc();
}


main();
