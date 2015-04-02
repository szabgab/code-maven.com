function show() {
    var package = $('#name').val();
    console.log(package);
    var url = 'https://pypi.python.org/pypi/' + package + '/json';
    console.log(url);
    jQuery.get( url, '', function(data) {
        console.log(JSON.stringify(data, null, 2));

        var source   = document.getElementById('text-template').innerHTML;
        var template = Handlebars.compile(source);
        var html    = template(data);

        document.getElementById("text").innerHTML = html;

    });
}

$(function() {
    $('#show').click(show);

});

