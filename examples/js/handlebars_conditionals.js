var data = {
   'cond1'  : true,
   'cond2'  : false,
   'name'   : 'Foo',
   'answer' : 42
};

document.getElementById('show').addEventListener('click', function () {
    console.log('click');
    var source = document.getElementById('text-template').innerHTML;
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
    if (operator  == '==') {
        bool = a == b;
    } else if (operator  == '>') {
        bool = a > b;
    } else {
    }

    if (bool) {
        return opts.fn(this);
    } else {
        return opts.inverse(this);
    }
});


