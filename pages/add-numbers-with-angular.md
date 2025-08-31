---
title: "Add numbers with AngularJS"
timestamp: 2015-08-04T21:30:01
tags:
  - ng-controller
  - ng-model
published: true
books:
  - angularjs
  - javascript
author: szabgab
archive: true
---


After writing the most basic examples, I wanted to create a small calulator with Angular. It is one of the simplest
code examples I can imagine after the "Hello World" and "Echo" examples.

So I set out to create a page using [AngularJS](/angularjs) that will add two numbers.


## Add naive

The naive solution, that did not work was to have two `input` elements with `ng-model` for 'a' and 'b'
and then to have an expression adding the two values.

{% include file="examples/angular/add.html" %}

[view](examples/angular/add.html)

Unfortunately JavaScript and thus Angular handles the input values as strings, even if they are really numbers
in those strings and then using the `+` operator on the strings acts as concatenation. Thus, if we try
the above examples and type 2 and 3 in the two boxes, we'll see 23 as output.

## Add numbers with controller

First, just like in the [Hello User](/hello-world-with-angular-controller) example,
we [create a module and a controller](/hello-world-with-angular-controller)
Within the controller we create a function called `AddNumbers` attached to the
`$scope`. In that function we take the values from the two `input` elements
and convert them to `Number` with plain JavaScript function call. (In order to aviod using
and `undefined` value we default both numbers to 0.) Then we add the values and
assign it to the newly created `sum` attribute.

{% include file="examples/angular/add_numbers_controller.js" %}

In the HTML file we can then use that `sum` attribute as part of a simple expression.
In order to trigger the `AddNumbers` function, we also add `ng-keyup` attributes
to both of the `input` elements:

{% include file="examples/angular/add_numbers_controller.html" %}

[view](examples/angular/add_numbers_controller.html)

Try it! It works great!

While I was writing this I had this thought that there must be a more simple solution,
that this might be over-engineering this problem and indeed there is a much easier solution.

## Add numbers

As it turns out it is quite easy to tell Angular that we would like to treat the values as numbers.
We only need to add `type="number"` to each one of `input` elements:

{% include file="examples/angular/add_numbers.html" %}

[view](examples/angular/add_numbers.html)
