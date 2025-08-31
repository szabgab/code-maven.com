---
title: "SVG Polyline"
timestamp: 2015-02-25T18:43:01
tags:
  - svg
published: true
books:
  - javascript
  - svg
author: szabgab
archive: true
---


This is part of the [SVG Tutorial and exercises](/svg) drawing a Polyline in SVG.


<script src="/try/examples/js/svg.min.js"></script>

<div id="polyline_1"></div>
<script src="/try/examples/js/svg_polyline.js"></script>
{% include file="examples/js/svg_polyline.js" %}

Note, typicall a polyline defines an open shape and thus it should not be filled by any color.
If I understand it correctly the SVG.js library automatically uses black fill for every shape,
including polylines. Therefore if we want our polyline to be not filled, we need to manually set
the `fill('none')`.

There are two parameter formats for a polyline. The one that seems so be a lot more useful is
the format you see in the solution. In this case we pass an array of two-element arrays.
Each one of the two-element arrays is a point in the sapce `[x, y]` that will be connected.

In the other format we pass a string in which the `x,y` pairs are separated by a space.
In this case the `x,y` pair should have no spaces around the comma.

So we pass either of the following:

```
[ [x1,y1],  [x2,y2], [x3, y3], ... ]
'x1,y1 x2,y2 x3,y3 ...'
```

but this would be incorrect:

```
x1, y1 ...
```


## A polyline of a snail

in which the points are calculated by a function.

<div id="polyline_snail"></div>
<script src="/try/examples/js/svg_polyline_snail.js"></script>
{% include file="examples/js/svg_polyline_snail.js" %}

