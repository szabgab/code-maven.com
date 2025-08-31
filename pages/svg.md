---
title: "SVG (Scalable Vector Graphics) Tutorial and Exercises"
timestamp: 2015-02-14T18:30:01
tags:
  - svg
published: true
books:
  - javascript
  - svg
author: szabgab
archive: true
---


This SVG - [Scalable Vector Graphics](http://en.wikipedia.org/wiki/Scalable_Vector_Graphics) tutorial uses small tasks as exercises
to help you learn how to build images.


<script src="/try/examples/js/svg.min.js"></script>

In order to get started check out the [SVG with JavaScript](/svg-with-javascript) and/or
the [SVG in Perl](https://perlmaven.com/scalable-vector-graphics-with-perl) article.

Then you can do the following exercises. I've tried to put them in order of growing complexity.
For each task you'll find a (hopefully) reasonable description of what you should do and you will also see the end-result
I was expecting. In addition you will find links to the pages where my solutions are presented.

Also see a recommended [svg tutorial](http://tutorials.jenkov.com/svg/index.html) by Jakob Jenkov.

(This is a first draft of this page, more shapes and more exercises will follow.)

## Basic shapes

<h3>Rectangle</h3>

Draw a blue rectangle of 200px width, 100px height.

<div id="blue_rectangle"></div>
<script src="/try/examples/js/svg_rectangle.js"></script>

My solution and more examples for an [SVG Rectangle](/svg-rectangle).

<h3>Square</h3>

Draw a square of 100px each side. I am not sure. Whatever this color is:

<div id="square_1"></div>
<script src="/try/examples/js/svg_square.js"></script>

My [SVG Square](/svg-square).

<h3>Ellipse</h3>

Draw an ellipse.

<div id="ellipse_1"></div>
<script src="/try/examples/js/svg_ellipse.js"></script>

The [SVG Ellipse](/svg-ellipse) I managed to create.


<h3>Circle</h3>

Draw a nice green circle with 100 px diameter.

<div id="circle_1"></div>
<script src="/try/examples/js/svg_circle.js"></script>

The [SVG Circle](/svg-circle) I managed to create.

<h3>Line</h3>

Draw a simple red line.

<div id="line_1"></div>
<script src="/try/examples/js/svg_line.js"></script>

The [SVG Line](/svg-line) I managed to create.

<h3>X</h3>

Draw a huge X. Which are actually just two lines crossing each other.

<div id="draw_x"></div>
<script src="/try/examples/js/svg_x.js"></script>

The [SVG X](/svg-x).


<h3>Polyline</h3>

<div id="polyline_1"></div>
<script src="/try/examples/js/svg_polyline.js"></script>

The [SVG Polyline](/svg-polyline) I managed to create.

<h3>Polygon</h3>

<div id="polygon_1"></div>
<script src="/try/examples/js/svg_polygon_1.js"></script>

The [SVG Polygon](/svg-polygon) I managed to create.




## Slightly more advanced tasks

<h3>Flag of Hungary</h3>

According to [Wikipedia](http://en.wikipedia.org/wiki/Flag_of_Hungary) and
the [Wikimedia svg](http://commons.wikimedia.org/wiki/File:Flag_of_Hungary.svg),
the Hungarian flag has a 2:1 ratio and the 3 stripes have the following RGB color values:
The Red is #CD2A3E, the white is, well, it is white #FFFFFF, and the green is #436F4D.

<div id="flag_of_hungary"></div>
<script src="/try/examples/js/svg_flag_of_hungary.js"></script>

My drawing of the [Hungarian flag](/svg-flag-of-hungary).


## Flag of Switzerland

According to the [Wikipedia](http://en.wikipedia.org/wiki/Flag_of_Switzerland) entry,
to the [Wikimedia svg](http://commons.wikimedia.org/wiki/File:Flag_of_Switzerland.svg)
example and to the 
[CD Bund V7.0](http://www.bk.admin.ch/themen/02268/02385/index.html?lang=de)
the red colour of the flags is #FF0000, the with of the
middle part is 1/5 of the full width, the width of the sides is 1/5 of the full width + 1/6 of the middle width.
Which seems to be 0.2 + 0.2 / 6 = 1.4/6 of the full width.

<div id="flag_of_switzerland"></div>
<script src="/try/examples/js/svg_flag_of_switzerland.js"></script>

My drawing of the [Swiss flag](/svg-flag-of-switzerland).

## Flag of Greenland

According to the [Wikipedia](http://en.wikipedia.org/wiki/Flag_of_Greenland) the flag of
Greenland is from two colors: white and red (PMS 186C). The size is 18:12 parts. The disk is 8 parts
in diameter and its center is 7 parts from one side.


<div id="flag_of_greenland"></div>
<script src="/try/examples/js/svg_flag_of_greenland.js"></script>

My drawing of the [flag of Greenland](/svg-flag-of-greenland).

## Other

* [SVG Linear Gradient](/svg-linear-gradient)

