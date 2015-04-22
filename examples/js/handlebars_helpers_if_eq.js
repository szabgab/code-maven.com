var data = {
   'name'   : 'Foo',
};

document.getElementById('show').addEventListener('click', function () {
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

