function flag_of_switzerland() {
    var draw = SVG('flag_of_switzerland');
    var width = 150;
    draw.size(width, width);
    var red   = draw.rect(width, width).fill({ color: '#FF0000' });

    var horizontal = draw.rect(2*width/3, width/5).dx(width/6).dy(2*width/5);
    horizontal.fill({ color: '#FFFFFF' });
    var vertical = draw.rect(width/5, 2*width/3).dx(2*width/5).dy(width/6);
    vertical.fill({ color: '#FFFFFF' });
}

flag_of_switzerland();

