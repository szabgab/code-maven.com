function rect_23() {
    var draw = SVG('rect_23');
    draw.size(200, 100);

    var gr = draw.gradient('linear', function(stop) {
        stop.at(0, '#FF0000');
        stop.at(1, '#0000FF');
    });
    gr.from(0, 0).to(0, 1);
    var rect = draw.rect(200, 100).fill(gr).stroke({ width: 1 });
}
rect_23();


