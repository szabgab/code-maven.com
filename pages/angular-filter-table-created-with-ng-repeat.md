---
title: "AngularJS: filter table created with ng-repeat"
timestamp: 2015-11-22T20:01:25
tags:
  - ng-repeat
  - filter
  - ng-model
  - ng-change
published: true
books:
  - angularjs
author: szabgab
---


Creating a table using `ng-repeat` is quite simple. Adding a search box to filter the result is also quite simple,
if we would like to use simple text search. It becomes a bit more complex if you'd like to search for values <b>less than</b>
a certain value typed in by the user.


In our examples we are going to use [the planets of the Solar System](https://en.wikipedia.org/wiki/Solar_System).
We have the name, the average distance from the Sun measured in units of "distance of the Earth from the Sun",
and the mass relative to the mass of the Earth. Therefore both numbers are 1 for the Earth. (We are not Earth centric at all, are we :).

In the first example we have built a table from some data embedded in the code and added a text-filter to all of the fields:

{% include file="examples/angular/angular_table_filter_1.html" %}

[view](examples/angular/angular_table_filter_1.html)


The interesting part of the code is in these two lines:

{% include file="examples/angular/angular_table_filter_1.js" %}

The second row is the one that builds the table. It is a regular `ng-repeat` row, but we have
filtered out the results based on the content of object `f`. The attributes of that object are
bound to the `input` boxes in the first line. Each attribute name will filter in the respective
field of the original array.

That's neat, but in our case the search or filter only makes sense on the first column. As it is a simple text-filter
there is no much use of finding all the planets for which the distance has a digit 7 in them. In other tables this
might be more interesting.


## Search values less than or greater than

A much more interesting search or filter would be to find all the planets where the distance is less than 2.
Or where the mass is less than 20.

{% include file="examples/angular/angular_table_filter_2.html" %}

[view](examples/angular/angular_table_filter_2.html)

This is more complex. I could not find a better solution yet, so for now, every time the user types in a value in either of the "distance"
or the "mass" filter box, the code will go over the values of the array, and add an extra key to each object which is `true` if the
object matches the currently added filter, or `false` if it isn't. The extra key is build using two underscores '__' followed by
the original key. The assumption is that it is very unlikely that we'll encounter data where these are also real keys.

The HTML part has changed slightly. Instead of binding the input boxes to attributes of the filter object, we bind them to another object (called g),
and we also connect the input boxes to functions calls using `ng-change`.

{% include file="examples/angular/angular_table_filter_2b.js" %}

When the user changes either of the two boxes, Angular will run the `filter_by` function. There first we check if the input box is empty.
If it is, then we remove the whole condition.

If there is a value in the input box, we go over all the object in the `planets` array and add the attribute with the appropriate `true`
or `false` value. The actual filtering is done by AngularJS.

{% include file="examples/angular/angular_table_filter_2.js" %}


