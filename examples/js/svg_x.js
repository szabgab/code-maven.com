function draw_x() {
    var draw = SVG('draw_x');
    draw.size(200, 200);
    draw.line(0, 0, 199, 199).attr({
        'stroke'       : '#FF0000',
        'stroke-width' : '3px'
    });
}

draw_line();
