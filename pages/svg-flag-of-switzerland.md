---
title: "Flag of Switzerland in SVG"
timestamp: 2015-02-15T14:50:01
tags:
  - svg
published: true
books:
  - javascript
  - svg
author: szabgab
archive: true
---


This is part of the [SVG Tutorial and exercises](/svg) drawing the Swiss flag in SVG.


<h3>Flag of Switzerland</h3>

<script src="/try/examples/js/svg.min.js"></script>

According to the [Wikipedia](http://en.wikipedia.org/wiki/Flag_of_Switzerland) entry,
to the [Wikimedia svg](http://commons.wikimedia.org/wiki/File:Flag_of_Switzerland.svg)
example and to the 
[CD Bund V7.0](http://www.bk.admin.ch/themen/02268/02385/index.html?lang=de)
the red colour of the flags is #FF0000, the width of the
middle part of the cross is 1/5 of the full width, the width of the sides is 1/5 of the full width + 1/6 of the middle width.
Which seems to be 0.2 + 0.2 / 6 = 1.4/6 of the full width.

The total width (or hight) of the cross =  2* 1.4/6+ 1/5  = 20 / 30 = 2/3 of the total width.

The both start at (total width - width of cross)/2 = 1/6 width.


<div id="flag_of_switzerland"></div>
<script src="/try/examples/js/svg_flag_of_switzerland.js"></script>
{% include file="examples/js/svg_flag_of_switzerland.js" %}

