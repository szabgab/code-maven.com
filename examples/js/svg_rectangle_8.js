function rect_8() {
    var img = SVG('rect_8');
    img.size(200, 100);
    img.rect(200, 100).fill({ color: '#FFF' }).stroke({ width: 1 });

    var rect = img.rect(100, 50);
    rect.fill({ color: '#F06' }).cx(0).cy(0);
}
rect_8();
