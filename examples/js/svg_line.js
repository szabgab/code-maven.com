function draw_line() {
    var draw = SVG('line_1');
    draw.size(200, 100);
    draw.line(0, 0, 100, 70).attr({
        'stroke'       : '#FF0000',
        'stroke-width' : '3px'
    });
}

draw_line();
