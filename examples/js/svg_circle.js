function draw_circle() {
    var draw = SVG('circle_1');
    draw.size(120, 120);
    draw.circle(100).attr({ fill: '#32AD4F' });
}

draw_circle();
