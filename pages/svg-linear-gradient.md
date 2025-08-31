---
title: "SVG Linear Gradient"
timestamp: 2015-03-02T17:31:01
tags:
  - svg
published: true
books:
  - javascript
  - svg
author: szabgab
archive: true
---


This is part of the [SVG Tutorial and exercises](/svg) adding linear gradient to a rectangle in SVG.

Gradient is when in an area the color gradually changes from one color to another color. In this article we'll look
at <b>linear gradient</b> when the color changes along a straight line. We are going to fill a rectangle shape using
the changing color.


<script src="/try/examples/js/svg.min.js"></script>

Normally, as you can see in the [basic rectangle examples](/svg-rectangle) we can call the `fill` method,
pass an [RGB](http://en.wikipedia.org/wiki/RGB_color_model) value to it and have it filled by that color.
`$shape->fill('#F0F0F0')`. Alternatively we could call the `attr` method: `$shape->attr({ 'fill' : '#F0F0F0' })`.

Instead of a fix color, we can pass a gradient to the `fill` method, and let SVG fill the shape with that changing color.

## White to Black top to bottom

In the first example we create a linear gradient using the `gradient` method. The first argument is just the string `'linear'`,
the second argument is a function setting the color values at various points along a linear line going from 0 to 1. We can supply several
colorts in that range, but we should supply at least the two end-points. If we only supply one color, SVG will use that single color
to fill the whole shape. No gradient will be used. Getting back to our first example: we set the color to be '#FFF' (which is just a short-hand for
'#FFFFFF') which is <b>white</b> at the begining of the 0-1 line. We also set the color to be '#000' (which is a short-hand for '#000000')
which <b>black</b> at the end of the 0-1 line. The whole construct is assigned to an arbitrary variable we called `gr`.

We can then map the 0-1 line onto the corners of the rectangle.  The `from` method connects the beginning of the 0-1 line to the coordinates (0, 0)
of the rectangle that mark the top left corner. The `to` method connects the end of the 0-1 line to the coordinates (0, 1) of the rectangle
that marks the bottom left corner.  (Actualy in both the `from` and `to` methods the first number sets the horizontal side 0 being left 1 being right;
the second coordinate sets the vertical side 0 being top, 1 being bottom.)

Once we configured our gradient, we can create a rectangle and use the variable `gr` that holds the gradient as the value of the `fill` attribute.

The `stroke` method is used to create a line around the rectangle. This helps us to see the edge of the rectangle.

<div id="rect_20"></div>
<script src="/try/examples/js/svg_rectangle_20.js"></script>
{% include file="examples/js/svg_rectangle_20.js" %}

## White to Black corner to corner

In the next example I've changed two things. One is that we use the `fill(gr)` instead of `attr({ 'fill' : gr })`. This change
does not have any impact on the result, I made it only to show that we can use either syntax.

The real change is that the gradient goes now `from(0, 0)` (left, top), `to(1, 1)` (right, bottom). If you look at the
rectangle you'll see that the top left corner is white and the bottom right corner is black. Basically the 0-1 line of the gradiant was mapped to these two corners.

<div id="rect_21"></div>
<script src="/try/examples/js/svg_rectangle_21.js"></script>
{% include file="examples/js/svg_rectangle_21.js" %}

## 3 stop gradient

In this example we got back to the horizontal lines as we had it in the first example, but instead of 2 stop points we now have 3. The two end-points are both
'black', but at the 0.25 of the 0-1 line, meaning at one quarter from the top of the rectangle, we have a white horizontal line. The color changes from black
to white in the top quarter of the rectangle and then to black again in the lower 3/4 of the rectangle.

<div id="rect_22"></div>
<script src="/try/examples/js/svg_rectangle_22.js"></script>
{% include file="examples/js/svg_rectangle_22.js" %}


## Blue gradient

In the next example we use a much smaller change in the gradient. This change in blue is pleasant to the eye.
Starting with a lighter blue on the left side it becomes dark on the right hand side.

<div id="rect_27"></div>
<script src="/try/examples/js/svg_rectangle_27.js"></script>
{% include file="examples/js/svg_rectangle_27.js" %}

## 4 directions

In the next 4 example you can see that the gradient can go between any two colors, in these cases the color changes
from '#FF0000' which is red, to '#0000FF' which is blue.

The 4 examples differ in their direction. (The `from` is always (0, 0) but the `to` has 4 different values.)
Notable might be the 4th example in which the value of `to` is the same as the value of `from` which causes
the whole rectangle to be a single color. Not very useful.

<span id="rect_23"></span>
<span id="rect_24"></span>
<span id="rect_25"></span>
<span id="rect_26"></span>
<script src="/try/examples/js/svg_rectangle_23.js"></script>
{% include file="examples/js/svg_rectangle_23.js" %}
<script src="/try/examples/js/svg_rectangle_24.js"></script>
{% include file="examples/js/svg_rectangle_24.js" %}
<script src="/try/examples/js/svg_rectangle_25.js"></script>
{% include file="examples/js/svg_rectangle_25.js" %}
<script src="/try/examples/js/svg_rectangle_26.js"></script>
{% include file="examples/js/svg_rectangle_26.js" %}


