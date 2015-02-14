function flag_of_switzerland() {
    var draw = SVG('flag_of_switzerland');
    var width = 600;
    draw.size(width, width);
    var red   = draw.rect(width, width).fill({ color: '##FF0000' });
    
}

flag_of_switzerland();

