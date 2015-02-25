function draw_polyline() {
    var draw = SVG('polyline_1');
    draw.size(200, 200);
    var p = draw.polyline([
		[10,10],
		[190,10],
		[190,190],
		[20,190],
		[20,20],
		[180,20],
		[180,180],
		[30, 180]
	]);
	p.fill('none').attr({
        'stroke'       : '#FF0000',
        'stroke-width' : '3px'
    });
}

draw_polyline();

