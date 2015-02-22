function draw_square() {
    var draw = SVG('square_1');
    draw.size(120, 120);
    var square = draw.rect(100, 100);
    square.attr({ fill: '#f06' });
}

draw_square()
