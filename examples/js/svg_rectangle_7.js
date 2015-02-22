function rect_7() {
    var img = SVG('rect_7');
    img.size(200, 100);
    img.rect(200, 100).fill({ color: '#FFF' }).stroke({ width: 1 });

    var rect = img.rect(100, 50);
    rect.fill({ color: '#F06' }).dx(30).dy(5).dy(5).dy(5);
}
rect_7();
