function rect_27() {
    var draw = SVG('rect_27');
    draw.size(200, 100);

    var gr = draw.gradient('linear', function(stop) {
        stop.at(0, '#1021A3');
        stop.at(1, '#A0A8EB');
    });
    gr.from(1, 0).to(0, 0);
    var rect = draw.rect(200, 100).fill(gr).stroke({ width: 1 });
}
rect_27();



