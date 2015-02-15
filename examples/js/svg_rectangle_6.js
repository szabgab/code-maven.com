function rect_6() {
    var img = SVG('rect_6');
    img.size(200, 100);
    img.rect(200, 100).fill({ color: '#FFF' }).stroke({ width: 1 });

    var rect = img.rect(100, 50);
    rect.fill({ color: '#F06' }).x(30).y(5);
}
rect_6();
