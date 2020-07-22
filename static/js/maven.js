$(document).ready(function() {
    var show_top = function(msg) {
        $('#top-poster').html(msg);
        $('#top-poster').css('font-size', '30px');
        $('#top-poster').css('background-color', '#42e8f4');
        $('#top-poster').show();
    };
    var show_bottom = function(msg) {
        $('#after-content').html(msg);
        $('#after-content').css('font-size', '30px');
        $('#after-content').css('background-color', 'orange');
        $('#after-content').show();
    };

    // $('#after-abstract').html(msg);

    var path = window.location.pathname;
    var re = new RegExp('docker|jenkins');
    if (re.exec(path)) {
        show_top('When you are done <a href="/devops-invitation">check out</a> how else we might help you.';
    }

//    msg = 'Was this article useful? Support me via <a href="https://www.patreon.com/szabgab">Patreon</a>!';
})
