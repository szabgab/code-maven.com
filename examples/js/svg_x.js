function draw_x() {
    var draw = SVG('draw_x');
    draw.size(200, 200);
    draw.line(0, 0, 200,200).attr({
        'stroke'       : '#FF0000',
        'stroke-width' : '5px'
    });
    draw.line(0, 200, 200,0).attr({
        'stroke'       : '#FF0000',
        'stroke-width' : '5px'
    });
}

draw_x();
