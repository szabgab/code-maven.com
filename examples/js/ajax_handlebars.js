function ajax_get(url, callback) {
    xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            console.log('responseText:' + xmlhttp.responseText);
            try {
                var data = JSON.parse(xmlhttp.responseText);
            } catch(err) {
                console.log(err.message + " in " + xmlhttp.responseText);
                return;
            }
            callback(data);
        }
    };

    xmlhttp.open("GET", url, true);
    xmlhttp.send();
}

ajax_get('/try/examples/js/data.json', function(data) {
    document.getElementById("title").innerHTML = data["title"];

    var source   = document.getElementById('text-template').innerHTML;
    var template = Handlebars.compile(source);
    var html    = template(data);

    document.getElementById("text").innerHTML = html;
});



