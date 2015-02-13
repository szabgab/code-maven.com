var draw_polygon_1 = SVG('polygon_1');
draw_polygon_1.size(120, 120);
var polygon = draw_polygon_1.polygon('0,0 100,50 50,100');
polygon.fill('#2ABFB5').stroke({ width: 3 })
