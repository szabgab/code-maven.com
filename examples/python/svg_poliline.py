#!/usr/bin/env python
import svgwrite

line = svgwrite.shapes.Polyline( [ (200, 100),  (200, 200), (300, 250) ], fill='white', stroke='black' )
line.points.append( (400, 90) )
# line.points.extend( [ (400, 90) ] )

dwg = svgwrite.Drawing(height=400, width=400)
dwg.add( line ) 

with open("steps.svg", "w") as fh:
    fh.write(dwg.tostring())

