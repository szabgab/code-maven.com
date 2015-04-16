
$(function() {
    console.log('start');
    //var url = 'https://pypi.python.org/pypi/';
    var url = '/try/examples/js/data.json';
    jQuery.get( url, function(data) {
        console.log("hello");
        //console.log(JSON.stringify(data, null, 2));
        //var source   = document.getElementById('text-template').innerHTML;
        //var template = Handlebars.compile(source);
        //var html    = template(data);
        //$("#title").html( html );
    }).fail(function(x) {
        console.log('Error');
		console.log(JSON.stringify(x, null, 2));
    });
    console.log('end');
});

