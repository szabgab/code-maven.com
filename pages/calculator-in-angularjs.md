---
title: "A simple calculator in AngularJS"
timestamp: 2015-08-07T07:30:01
tags:
  - ng-app
  - ng-controller
  - ng-model
published: true
books:
  - angularjs
  - javascript
author: szabgab
archive: true
---


Not long ago I have written an example [adding numbers with AngularJS](/add-numbers-with-angular),
but then I found left-overs from a previous attempt to write a AngularJS examples and slides where I found
this example. A simple calculator in AngularJS.


If you have followed the [previous articles](/angularjs) then you'll see in this case
I've separated the HTML part and the JavaScript part.

## The HTML

You'll also see that the HTML part is fairly simple though it contains another new element.
In this examples the declarations of `ng-app` and `ng-controller` are in the same
HTML element. Why create an extra level if we can do it in a single `div` element?

Besides that we have 2 `input` boxes and a `select` element.
Each one has its own `ng-model`.

The last part of the HTML is the `{{ result() }}` directive.
I think this is also the first time we have a function call in the directive.

{% include file="examples/angular/calculator.html" %}

[view](examples/angular/calculator.html)

## The JavaScript

In the JavaScript part we create the `Angular module and controller` and
we declare the `result` function as an attribute of the current `$scope`.
This is what allows us to use the function in the Angular directive inside the HTML.

The JavaScript code calculating the result of the simple math operations is straight forward
albeit a bit boring.

{% include file="examples/angular/calculator.js" %}
