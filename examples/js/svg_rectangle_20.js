function rect_20() {
    var draw = SVG('rect_20');
    draw.size(200, 100);

    var gr = draw.gradient('linear', function(stop) {
        stop.at(0, '#FFF');
        stop.at(1, '#000');
    });
    gr.from(0, 0).to(0, 1);
    var rect = draw.rect(200, 100).attr({ fill: gr }).stroke({ width: 1 });

}
rect_20();


