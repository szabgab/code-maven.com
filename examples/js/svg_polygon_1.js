function draw_polygon() {
    var draw = SVG('polygon_1');
    var width = 200;
    var height = 200;
    draw.size(width, height);
    var background = draw.rect(width, height).attr({ fill: '#FFF' }).stroke({ width: 1 });

    var poly = draw.polygon([ [20, 10], [50, 20], [130, 100], [70, 140] ]);
    poly.attr({ 'fill' : '#456789' });
}
draw_polygon();

