function ellipse() {
    var draw = SVG('ellipse_1');
    draw.size(200, 100);
    var ellipse = draw.ellipse(140, 70).attr({
        'fill'         : '#32AD4F',
        'stroke'       : '#723891',
        'stroke-width' : '3px'
    });
    ellipse.dx(5).dy(5);
}
ellipse();


