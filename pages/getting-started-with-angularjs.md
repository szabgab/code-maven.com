---
title: "Getting started with AngularJS"
timestamp: 2015-07-20T23:30:01
tags:
  - ng-app
  - {{
  - }}
published: true
books:
  - javascript
  - angularjs
author: szabgab
archive: true
---


[AngularJS](/angularjs) is a JavaScript framework that enhances HTML.


In order to get started with AngularJS we need to have an HTML page with 3 things:

## 1) Loading angular.js

We need to load the angular.js file from one of the CDNs or from the local disk.

If you'd like to load it from Google CDN then put this in your HTML:

```
<script src="http://ajax.googleapis.com/ajax/libs/angularjs/1.4.2/angular.min.js"></script>
```

If you'd like to use the Cloudflare CDNjs, use this entry:

```
<script src="http://cdnjs.cloudflare.com/ajax/libs/angular.js/1.4.2/angular.min.js"></script>
```

You can also download the angular.min.js file, put it on your server and serve it from there:

```
<script src="angular.min.js"></script>
```

In the above examples I used version 1.4.2 of AngularJS, but by the time you read this
Angular might have a newer releases in the 1.x series and you might want to use that version.

## 2) Add ng-app

Add `ng-app` to one of the HTML elements in our page. Anything within this element will be seen
as part of our AngularJS code. We can add this to the `html` element, to the `body`, or even
a `div` as it has been done in our first example.

## 3) Add an AngularJS expression.

AngularJS has various elements. An <b>expression</b> is a code snipped wrapped
in `{{ }}`. It can contain a limited set of JavaScript expressions.

That brings us to our first example. Even before writing a Hello

## Hello World with AngularJS

{% include file="examples/angular/hello_world.html" %}

[view](examples/angular/hello_world.html)

In our very first example, the expression is a hard-coded string. Nothing fancy.
Even a bit insulting.

The result is `Hello World`.

## Simple AngularJS expression

In our next example, the expression is a hard-coded computation.

{% include file="examples/angular/first_expression.html" %}

[view](examples/angular/first_expression.html)

The result is `Hello Angular 42`.

Angular executed the expression and displayed the result.

Remember, this runs in the browser, so if you click on "view source", you'll
see the code as it was in the html file.

## Variables in AngularJS expressions

In the next, still very simple example, we can see that we can assign values
to variables, and then we can use those variables in the expression.

Note: we don't use the `var` for variable assignment here because these
are actually attributes on an internal object of AngularJS.

{% include file="examples/angular/variables_in_expressions.html" %}

[view](examples/angular/variables_in_expressions.html)

## Separate variable assignment and usage into two expressions.

We can even have the assignment in one expression and use those variables in
another expression. Not only that, but the location of those expressions in the HTML
file does not matter. As we can see in the following example, we can use the
variables even before the assignment:

{% include file="examples/angular/assignment_and_expression.html" %}

[view](examples/angular/assignment_and_expression.html)

The result will be:

```
Result 42
Assignment: 19
Result 42
```

There is a slight problem though, the last result of the expression where we had the assignment
is also displayed. That's why we see the 19 on the page.

The solution is to add another statement to the assignment expression that does
not return any visible value. It can be `null` or `''` (the empty string).

{% include file="examples/angular/assignment_and_expression_fixed.html" %}

[view](examples/angular/assignment_and_expression_fixed.html)

The result will be:

```
Result 42
Assignment:
Result 42
```
