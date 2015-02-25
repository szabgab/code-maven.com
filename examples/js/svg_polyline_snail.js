function draw_polyline_snail() {
    var draw = SVG('polyline_snail');
    draw.size(200, 200);
	var s = new Array;
	var step = 180;
	var delta = 10;
	var x = 10;
	var y = 10;
	s.push([x, y]);

	while (Math.abs(step) > 10) {
		x += step;
		s.push([x, y]);
		y += step;
		s.push([x, y]);
		step -= delta;
		step *= -1;
		delta *= -1;
	}

    var p = draw.polyline(s);
	p.fill('none').attr({
        'stroke'       : '#00FF00',
        'stroke-width' : '3px'
    });
}

draw_polyline_snail();


