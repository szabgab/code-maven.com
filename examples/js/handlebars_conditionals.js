var data = {
   'cond1'  : true,
   'cond2'  : false,
   'name'   : 'Foo',
   'answer' : 42
};

document.getElementById('show').addEventListener('click', function () {
    var source = document.getElementById('text-template').innerHTML;
    var template = Handlebars.compile(source);
    var html = template(data);
    document.getElementById('content').innerHTML = html;
});

document.getElementById('show2').addEventListener('click', function () {
    document.getElementById('content').innerHTML = 'Look at the console!';
    var source = document.getElementById('text2-template').innerHTML;
    var template = Handlebars.compile(source);
    var html = template(data);
    document.getElementById('content').innerHTML = html;
});


Handlebars.registerHelper('if_eq', function(a, b, opts) {
    if (a == b) {
        return opts.fn(this);
    } else {
        return opts.inverse(this);
    }
});


Handlebars.registerHelper('iff', function(a, operator, b, opts) {
    var bool = false;
    switch(operator) {
       case '==':
           bool = a == b;
           break;
       case '>':
           bool = a > b;
           break;
       default:
           throw "Unknown operator " + operator;
    }

    if (bool) {
        return opts.fn(this);
    } else {
        return opts.inverse(this);
    }
});


