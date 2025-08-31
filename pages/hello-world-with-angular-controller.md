---
title: "Hello World with AngularJS module and controller"
timestamp: 2015-08-04T13:00:01
tags:
  - ng-app
  - ng-controller
  - angular.module
  - controller
  - $scope
published: true
books:
  - angularjs
  - javascript
author: szabgab
archive: true
---


In [getting started with AngularJS](/getting-started-with-angularjs) we saw how simple expressions work,
and then we created our [first binding](/angularjs-first-binding). This time we look
at two simple examples using AngularJS modules and controllers.


## Hello World Controller

{% include file="examples/angular/hello_world_controller.html" %}

[view](examples/angular/hello_world_controller.html)

After loading `angular.js` we include some more JavaScript code.
We can do that embedded in the HTML file using a pair of `script` tags or,
as usually is recommended and as we did it in this examples, we can put that code
in an external JavaScript file. The only requirement is that we load that file <b>after</b>
we load `angular.js`.

The JavaScript code looks like this:

{% include file="examples/angular/hello_world_controller.js" %}

First we create an `angular.module` and attached to it we create a `controller`.
The `module` gets two parameters: The first is the name we select for this module. It can be any
string, but as this is the name of the Angular Application  it might be a good idea to call it some "App".

We are going to use this name in our HTML file as the value of the `ng-app` attribute.
(Earlier we did not provide a name to this attribute and thus it used the default application.)

The second parameter of the `module` is a list of dependencies. For now we leave that empty.

The `controller` itself also has two parameters. The first one is its name. Usually it is some
word ending with "Controller". The second parameter is a function that implements the controller.
It will be executed once when the controller is loaded. The environment is passed in the `$scope`
variable. The models and the "variables" in the Angular expressions we used earlier are attributes of this
object. Hence as we create a new attribute called `$scope.greeting`, and assign a value to it,
we'll be able to access this value from our HTML file.

In order for Angular to connect our module and controller we need to create an HTML element with an
`ng-app` attribute that equals to the name of the module, and inside that HTML element we
need to add another HTML element with an attribute called `ng-controller` that equals to the
name of our controller.

These two mark the area in which the `$scope` is relevant.

This was a fairly simple example with a hard-coded value assigned to an attribute and used in an expression.

## Hello user Controller

Let's see a slightly more complex example in which we handle input from the user and process that input in
the controller. The processing will be very simple, just concatenating with a fixed string.

{% include file="examples/angular/hello_user_controller.js" %}

In this case, the attribute `NameChange` we add to the `$scope` is a function
and that function will create the `$scope.greeting` attribute using the value from the
`$scope.name` attribute.

In the HTML

{% include file="examples/angular/hello_user_controller.html" %}

[view](examples/angular/hello_user_controller.html)

The `ng-model="name"` connects the input element to the `$scope.name`.

The `ng-keyup="NameChange()"` connects the keyup event of the HTML page to
the function defined as `$scope.NameChange` which means the function will be
called every time the content of the input box has changed.

The two expression in the HTML code
```
{{name}}
```

and

```
{{greeting}}
```
will display the content of `$scope.name` and `$scope.greeting` respectively.

The result is that as we type "Foo" in the input box, our page will display "Hello Foo" in `h1`
tags and `Foo` in `h2` tags.

## Comments

hey, thanks Gabor

---


it is absolutely Great Tutorial to get started with angular js Thanks :)

---

Great tutorial for beginners, thanks for posting!


