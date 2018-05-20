import svgwrite

dwg = svgwrite.Drawing(height=600, width=600)
hlines = dwg.add(dwg.g(id='hlines', stroke='green'))

hlines.add( dwg.line( start=(20, 20), end=(180, 20), stroke_width=12) )
hlines.add( dwg.line( start=(180, 15), end=(180, 25), stroke_width=2) )
hlines.add( dwg.line( start=(180, 25), end=(190, 20), stroke_width=2) )
hlines.add( dwg.line( start=(180, 15), end=(190, 20), stroke_width=2) )

with open("arrow.svg", "w") as fh:
    fh.write(dwg.tostring())


