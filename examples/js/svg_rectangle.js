function draw_rectangle() {
    var draw = SVG('blue_rectangle');
    draw.size(200, 100);
    var rect = draw.rect(200, 100);
    rect.attr({ fill: '#00f' });
}

draw_rectangle();
