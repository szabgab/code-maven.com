Handlebars.registerHelper('abc', function(options) {
  //return options.fn(this);
  return 'some text';
});

function show(package_name, package_version) {
    //console.log(package_name);
    var url = 'https://pypi.python.org/pypi/' + package_name;
    if (package_version != undefined) {
        url += '/' + package_version;
    }
    url += '/json';
    //console.log(url);
    jQuery.get( url, function(data) {
        console.log(JSON.stringify(data, null, 2));

        var source   = document.getElementById('text-template').innerHTML;
        var template = Handlebars.compile(source);
        var html    = template(data);

        $("#text").html(html);
        console.log(html);

    }).fail(function() {
        $("#text").html('Error');
    });
}

$(function() {
    $('#show').click(function() {
        show( $('#name').val() );
    });
    $('.pypi-link').click(function () {
        var package_name    = $(this).attr('data-package');
        var package_version = $(this).attr('data-version');
        show(package_name, package_version);
        event.stopPropagation();
    });

});

