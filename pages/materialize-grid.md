---
title: "Materialize CSS: Rows and columns - a grid"
timestamp: 2022-08-17T08:00:04
tags:
  - CodeMaven
published: true
books:
  - javascript
  - html
  - css
author: szabgab
archive: true
show_related: true
---


In order to make it easy to place various objects on the web page, people usually use a grid.  In [Materialize](/materialize)
the grid can have multiple rows and each row can be divided into 12 columns. The name "row" is actually slightly confusing in this context.
A name such as "block" might have been better as each "row" can actually contain several 12-width physical row.

For more details see the documentation of the [grid](https://materializecss.com/grid.html)


{% include file="examples/materializecss/rows-and-columns.html" %}

[view](examples/materializecss/rows-and-columns.html)

At the bottom of the file I've added some manual CSS in order to change the background-color of the boxes.
Hopefully this will make it easier to see the individual cells in the grid.


