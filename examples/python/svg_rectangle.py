import svgwrite

dwg = svgwrite.Drawing(height=200, width=100)
dwg.add( dwg.rect(insert=(200, 100), size=(200, 100), fill='blue', stroke='red', stroke_width=3) )
with open("rect.svg", "w") as fh:
    fh.write(dwg.tostring())

#import cairosvg
#cairosvg.svg2png(bytestring=dwg.tostring(), write_to="rect.png")
#cairosvg.svg2pdf(url="rect.svg", write_to="rect.pdf")


#print(dwg.tostring())
#print(dir(dwg))
#dwg.save()

