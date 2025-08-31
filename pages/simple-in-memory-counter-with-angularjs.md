---
title: "Simple in-memory counter with AngularJS"
timestamp: 2015-08-05T21:10:01
tags:
  - ng-app
  - ng-click
  - ng-init
published: true
books:
  - angularjs
  - javascript
author: szabgab
archive: true
---


In the [big counter example](/counter) we see a number of implementations of counters.
Here is one using [AngularJS](/angularjs).


## Simple button to increment counter

{% include file="examples/angular/in_memory_counter.html" %}

[view](examples/angular/in_memory_counter.html)

In this example we have an HTML button that has two Angular attributes.
`ng-init` will be executed once when the page loads. It gives the initial value to the
attribute `counter`.

The content of `ng-click` will be executed every time we click on the button. That will increment the counter by 1.
(`counter++` does not work here)

When we load the page we can see the button "Increment" and the number 0. Then as we click on the button the number
gets incremented.

## Increment and decrement buttons

In the next example we have added another button to decrement the counter by 1.
In addition, in order to make the step clearly separated, we have moved the `ng-init` attribute to
a separate `div` element which is not going to be displayed at all.

{% include file="examples/angular/in_memory_counter_with_decrement.html" %}

[view](examples/angular/in_memory_counter_with_decrement.html)

## In-memory counter with controller

In preparation from some more substantial actions behind the counter,
in the third example we have move the code decrementing the counter to a controller.
(The button incrementing the counter was left as it was before.)

This time we've created an [Angular module and controller](/hello-world-with-angular-controller),
in which we set the default value of `$scope.counter` to 0 and we have also defined a method called
`decrement`. As this is already plain JavaScript, here we can already use the autoincrement and autodecrement
expression like this one: `counter--`.

In the HTML we set `ng-click="decrement()"` which means the `decrement`
method will be called every time a button is pressed.

{% include file="examples/angular/in_memory_counter_with_controller.html" %}

[view](examples/angular/in_memory_counter_with_controller.html)
