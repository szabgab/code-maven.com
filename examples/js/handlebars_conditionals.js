var data = {
   'cond1' : true
};

document.getElementById('show').addEventListener('click', function () {
    console.log('click');
    var source = document.getElementById('text-template').innerHTML;
    var template = Handlebars.compile(source);
    var html = template(data);
    document.getElementById('content').innerHTML = html;
});


//Handlebars.registerHelper('link', function(obj) {
//    var url  = obj.url;
//    var text = obj.text;
//    if (text == undefined) {
//        text = url;
//    }
//    return new Handlebars.SafeString( '<a href="' + url + '">' + text + '</a>' );
//});


