---
title: "AngularJS - first binding"
timestamp: 2015-07-24T07:30:01
tags:
  - ng-model
published: true
books:
  - angularjs
  - javascript
author: szabgab
archive: true
---


Now that we have created our very [first expressions in AngularJS](/getting-started-with-angularjs),
its time to make another step, this time with something much more interesting. We are going to connect an
input field with an expression that will automatically display whatever we type in.


## Minimal Hello User

The Hello World examples are usually quite boring as they are one-way. Just display some
string that was part of the code. In this example we have an `input` element
in which we declare the `ng-model` with a value `name`.

```html
<input ng-model="name">
```

Once we do that we can use the `name` attribute in Angular expressions: `{{ name }}`
for example in order to show the content:

{% include file="examples/angular/minimal_hello_user.html" %}

[view](examples/angular/minimal_hello_user.html)

If you open this example, you'll see an input box. As you type in the input box
the text you type in will also appear after the word <b>Hello</b>.

With this we see how can we <b>bind</b> input elements to attributes of AngularJS
that can be used in expressions.

## Full Hello User example

The above was probably the smallest possible example using data binding in AngularJS.
A full, or at least "fuller" example can be found here:

{% include file="examples/angular/hello_user.html" %}

[view](examples/angular/hello_user.html)

In this version we have a "real" HTML 5 page, the `ng-app` marks the whole
`html` file to be our Angular Application, and the `input` element
is also better described with `type` and a `placeholder` to give
a hint to the user what to do with the HTML form.
