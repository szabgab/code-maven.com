function flag_of_hungary() {
    var draw = SVG('flag_of_hungary');
    var width = 120;
    var height = width/2;
    draw.size(width, height);

    var red   = draw.rect(width, height/3).fill({ color: '#CD2A3E' });
    var white = draw.rect(width, height/3).fill({ color: '#FFFFFF' }).dy(height/3);
    var green = draw.rect(width, height/3).fill({ color: '#436F4D' }).dy(2*height/3);
}
flag_of_hungary();


