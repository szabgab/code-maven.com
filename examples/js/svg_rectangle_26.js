function rect_26() {
    var draw = SVG('rect_26');
    draw.size(200, 100);

    var gr = draw.gradient('linear', function(stop) {
        stop.at(0, '#FF0000');
        stop.at(1, '#0000FF');
    });
    gr.from(0, 0).to(0, 0);
    var rect = draw.rect(200, 100).fill(gr).stroke({ width: 1 });
}
rect_26();



