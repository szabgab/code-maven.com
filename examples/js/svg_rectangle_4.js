function rect_4() {
    var img = SVG('rect_4');
    img.size(200, 100);
    var rect = img.rect(200, 100);
    rect.fill({ color: '#FFF' }).stroke({ width: 1 });
}
rect_4();
