function flag_of_greenland() {
    var draw = SVG('flag_of_greenland');
    var width = 300;
    var height = 200;
    draw.size(width+2, height+2);
    var background = draw.rect(width+2, height+2).attr({ fill: '#FFF' }).stroke({ width: 1 }); //.opacity(0);

    var circle1 = draw.circle(8*height/12).cx(1+7*width/18).cy(1+height/2).fill('#FFF');
    var circle2 = draw.circle(8*height/12).cx(1+7*width/18).cy(1+height/2).fill('#FFF');
    var red = '#c8102e';
    draw.rect(width, height/2).fill('#FFF').dx(1).dy(1);
    draw.rect(width, height/2).fill(red).dy(height/2).dx(1).dy(1);
    draw.rect(width, height).maskWith(circle1).fill(red);
    draw.rect(width, height).dy(height/2).maskWith(circle2).fill('#FFF');
}

flag_of_greenland();

