var data = {
   'cond1'  : true,
   'cond2'  : false,
};

document.getElementById('show').addEventListener('click', function () {
    var source = document.getElementById('text-template').innerHTML;
    var template = Handlebars.compile(source);
    var html = template(data);
    document.getElementById('content').innerHTML = html;
});

