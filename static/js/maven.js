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

    var re_pro = new RegExp('^/pro/');
    if (re_pro.exec(path)) {
        return;
    }

    var re_courses = new RegExp('^/courses(/.*)?$');
    if (re_courses.exec(path)) {
        return;
    }
    var re_pages = new RegExp('^/(services|programming-boootcamp-for-scientists|docker|python)$');
    if (re_pages.exec(path)) {
        return;
    }


    //var re_devops = new RegExp('ansible|docker|jenkins|bash|shell|groovy');
    //if (re_devops.exec(path)) {
    //    show_top('When you are done <a href="/devops-invitation">check out</a> how else we might help you!');
    //    show_bottom('If this article helped you, <a href="/devops-invitation">check out</a> what else can you learn here!');
    //    //show_bottom('If this article helped you, <a href="https://www.patreon.com/szabgab">check out</a> what else can you learn via my Patreon page!');
    //    return;
    //}

    //var re_python = new RegExp('python|flask');
    //if (re_devops.exec(path)) {
    //    show_top('When you are done <a href="/python-invitation">check out</a> how else we might help you!');
    //    show_bottom('If this article helped you, <a href="/python-invitation">check out</a> what else can you learn here!');
    //    return;
    //}

    //show_top('When you are done <a href="https://code-maven.com/invitation">check out</a> how else we might help you!');
    //show_bottom('If this article helped you, <a href="https://code-maven.com/invitation">check out</a> what else can you learn here!');
    //show_bottom('If this article helped you, consider <a href="https://www.patreon.com/szabgab">supporting me</a> via my Patreon page!');

    //show_top('Are you interested to invest some money in the stock market, but don\'t want to waste time chasing data sources? Are you overwhelmed by the meaningless data dumps from the big web-sites? Try <a href=\"https://torto.ai/welcome?utm_source=code-maven&utm_medium=web&utm_campaign=code-maven-top\">Torto.AI</a>.')
    //show_top('Are you interested to invest some money in the stock market? Try <a href=\"https://torto.ai/welcome?utm_source=code-maven&utm_medium=web&utm_campaign=code-maven-top\">Torto.AI</a>.')
    // const bottom_ads = [
    //     'For Software developers only: Are you interested to invest some money in the stock market? Try <a href="https://torto.ai/welcome?utm_source=code-maven&utm_medium=web&utm_campaign=code-maven-bottom">Torto.AI</a>.',
    //     'Any investment in the stock market is partially based on objective data (e.g. P/E ratio) and partially on the subjective worldview of the investor (expected changes in inflation, politics, weather etc.) <a href="https://torto.ai/welcome?utm_source=code-maven&utm_medium=web&utm_campaign=code-maven-bottom">torto.ai</a> works on providing you a platform where you can easily combine these aspects and find the investment that is most suitable for your expectations.',
    // ];

    // let rnd = Math.floor(Math.random() * bottom_ads.length);
    //console.log(rnd);
    // show_bottom(bottom_ads[rnd]);
})
