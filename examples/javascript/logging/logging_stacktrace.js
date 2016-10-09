function add(x, y) {
    console.log(stacktrace());
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

function stacktrace() {
  function st2(f) {
    var args = [];
    if (f) {
        for (var i = 0; i < f.arguments.length; i++) {
            args.push(f.arguments[i]);
        }
        var function_name = f.toString().split('(')[0].substring(9);
        return st2(f.caller) + function_name + '(' + args.join(', ') + ')' + "\n";
    } else {
        return "";
    }
  }
  return st2(arguments.callee.caller);
}
