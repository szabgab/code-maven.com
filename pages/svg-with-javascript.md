---
title: "SVG - Scalable Vector Graphics with JavaScript"
timestamp: 2015-02-13T16:30:01
tags:
  - SVG
published: true
books:
  - javascript
  - svg
author: szabgab
archive: true
---


On a computer, every image is made out of pixels in various colors.
If the image is very smooth then we have a lot of pixels. Still just pixels.

If we want to save a picture to a file basically we can have two options.
Either we save the pixels which is called <b>raster image</b>, or we store instructions
how to draw lines in order to generate the pixels. This is called <b>vector image</b>.

The advantage of vector graphics is that we can enlarge the image without loss of quality.


[Scalable Vector Graphics (SVG)](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) is
an XML file containing instructions to draw an image.  [SVG.JS](http://svgjs.com/) is 
a JavaScript library that makes it easy to create such XML file and even without saving them
to disk, to use them to draw images on a web site.

Just as we saw a [examples for SVG images drawn with Perl](https://perlmaven.com/scalable-vector-graphics-with-perl),
let's see a few simple examples with the JavaScript library.

<script src="/try/examples/js/svg.min.js"></script>

Download the implementation of [SVG.JS](http://svgjs.com/) using
`wget https://raw.github.com/wout/svg.js/master/dist/svg.min.js`
or some other way and let's start drawing.

## Square

Create the following two files:

An HTML file that loads the `svg.min.js` we have just downloaded. This can go anywhere in the HTML file.

Then we add an HTML  element with an id. (`square_1` in our case). This is where the drawing will be placed.

Finally we load a JavaScript file where we put the instructions. Unless we employ some kind of delayed execution,
this JavaScript file has to come after the other two.

{% include file="examples/js/svg_square.html" %}

[view](examples/js/svg_square.html)

The other file is the JavaScript file with the instruction.
The `SVG()` function gets the `id` of the HTML element where we want to put our drawing.
This returns an object. On this object we can call various methods that will impact the drawing.

{% include file="examples/js/svg_square.js" %}

The result will look like this:

<div id="square_1"></div>
<script src="/try/examples/js/svg_square.js"></script>

## Circle

In order to draw a circle it is enough to provide its diameter:

{% include file="examples/js/svg_circle.js" %}

And have the appropriate HTML file to load the JavaScript:

{% include file="examples/js/svg_circle.html" %}

[view](examples/js/svg_circle.html)


<div id="circle_1"></div>

<script src="/try/examples/js/svg_circle.js"></script>

## Polygon

{% include file="examples/js/svg_polygon.js" %}

And have the appropriate HTML file to load the JavaScript:

{% include file="examples/js/svg_polygon.html" %}

[view](examples/js/svg_polygon.html)

<div id="polygon_1"></div>

<script src="/try/examples/js/svg_polygon.js"></script>


