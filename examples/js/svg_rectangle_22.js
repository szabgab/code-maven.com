function rect_22() {
    var draw = SVG('rect_22');
    draw.size(200, 100);

    var gr = draw.gradient('linear', function(stop) {
        stop.at(0, '#000');
        stop.at(0.25, '#FFF');
        stop.at(1, '#000');
    });
    gr.from(0, 0).to(0, 1);
    var rect = draw.rect(200, 100).fill(gr).stroke({ width: 1 });

}
rect_22();

