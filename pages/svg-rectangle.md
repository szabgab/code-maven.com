---
title: "SVG Rectangle"
timestamp: 2015-02-14T18:31:01
tags:
  - svg
published: true
books:
  - javascript
  - svg
author: szabgab
archive: true
---


This is part of the [SVG Tutorial and exercises](/svg) drawing a rectangle in SVG.


<script src="/try/examples/js/svg.min.js"></script>

The solution to the rectangle exercise as listed on [SVG page](/svg):

<div id="blue_rectangle"></div>
<script src="/try/examples/js/svg_rectangle.js"></script>
{% include file="examples/js/svg_rectangle.js" %}


<h2>Drawing Rectangles</h3>

In the next section we go over various attributes you can set on a rectangle. Many
of these are relevant to every other shape as well.

<h3>Default rectangle</h3>

In this example we just create an SVG image and then create a rectangle of the same size.

<div id="rect_1"></div>
<script src="/try/examples/js/svg_rectangle_1.js"></script>
{% include file="examples/js/svg_rectangle_1.js" %}

<h3>White rectangle</h3>
<div id="rect_2"></div>
<script src="/try/examples/js/svg_rectangle_2.js"></script>
{% include file="examples/js/svg_rectangle_2.js" %}

Of course, on a white background it is hard to see the white rectangle...


<h3>Nice rectangle</h3>

Let's give it some other color:

<div id="rect_3"></div>
<script src="/try/examples/js/svg_rectangle_3.js"></script>
{% include file="examples/js/svg_rectangle_3.js" %}

<h3>White rectangle with border</h3>

Alternatively, we can have the background in white, but we can add a border. We use `stroke` for this:

<div id="rect_4"></div>
<script src="/try/examples/js/svg_rectangle_4.js"></script>
{% include file="examples/js/svg_rectangle_4.js" %}


<h3>Smaller rectangle</h3>

Up until now the rectangle we drew was the same size as the image itself. Now we are going to see how a smaller rectangle can be
placed on that image. In order to make it clearer we actually use two rectangles. The first one created by `img.rect(200, 100).fill({ color: '#FFF' }).stroke({ width: 1 });`
provides the background with a 1 pixel wide border. That will make it easier to see what happens to the other rectangle we draw.

The second rectangle is smaller (only 100 pixel wide and 50 pixel high) and it has that nice color we had earlier.

As you can see the smaller rectangle is attached to the top-left corner of the image. That's because the point at <b>(x,y)</b> coordinates <b>(0,0)</b> in SVG is the
top left corner. 

<div id="rect_5"></div>
<script src="/try/examples/js/svg_rectangle_5.js"></script>
{% include file="examples/js/svg_rectangle_5.js" %}

<h3>Move the SVG element on the x and y axes</h3>

Let's put the rectangle in some other place.
There are several ways to indicate the location of an SVG element. The `x()` and `y()` methods allow us to set the
coordinates of (the top-left corner of) a rectangle to absolute values on the <b>x,y</b> axes.

In this example we have moved the rectangle 30 pixels to the right on the x axis, and 5 pixels down on the y axis.

We could call `x(30)` several times, on the same object, only the last call would matter.

If we call `x()` or `y()` with a parameter as above, they both return the current object, which means
we can stack the calls one on the other as we do in the examples.

On the other hand, calling `x()` or `y()` without any parameter will return the current location of the object
on the <b>x,y</b> axes.

<div id="rect_6"></div>
<script src="/try/examples/js/svg_rectangle_6.js"></script>
{% include file="examples/js/svg_rectangle_6.js" %}

<h3>Move the element relative to its own position</h3>

The `dx()` and `dy()` methods allow us to move the object relative to its current position.
When the object is created it does not matter if we use `x()` or `dx()` (at least on rectangles)
as the default location of the rectangle is <b>0,0</b>, but later we'll see how we can change the coordinates
of an existing object. Then it will be important that we can either set the coordinates in absolute terms
using `x()` and `y()`, or in relative terms using `dx()` and `dy()`.

In the example we can see that we call `dy()` multiple times stacked one on the other and the movements
add up.

<div id="rect_7"></div>
<script src="/try/examples/js/svg_rectangle_7.js"></script>
{% include file="examples/js/svg_rectangle_7.js" %}

<h3>Positioning by the center of the object</h3>

Sometimes it is easier to position an element by its center. Using `cx()` and `cy` is quite similar to
using `x()` and `y()`, except that the coordinates we give are that of the center of the rectangle.
For example if we set the center to <b>0, 0</b> then we'll only see one quarter of the rectangle:

<div id="rect_8"></div>
<script src="/try/examples/js/svg_rectangle_8.js"></script>
{% include file="examples/js/svg_rectangle_8.js" %}



