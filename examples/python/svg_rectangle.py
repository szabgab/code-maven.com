import svgwrite

dwg = svgwrite.Drawing(height=200, width=100)
dwg.add( dwg.rect(insert=(200, 100), size=(200, 100), fill='blue', stroke='red', stroke_width=3) )
with open("rect.svg", "w") as fh:
    fh.write(dwg.tostring())

