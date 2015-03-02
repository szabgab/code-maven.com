function rect_21() {
    var draw = SVG('rect_21');
    draw.size(200, 100);

    var gr = draw.gradient('linear', function(stop) {
        stop.at(0, '#FFF');
        stop.at(1, '#000');
    });
    gr.from(0, 0).to(1, 1);
    var rect = draw.rect(200, 100).fill(gr).stroke({ width: 1 });
}
rect_21();
