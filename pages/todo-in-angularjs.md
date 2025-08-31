---
title: "TODO in AngularJS"
timestamp: 2015-08-07T16:50:01
tags:
  - ng-repeat
  - push
  - ng-click
  - $index
published: true
books:
  - angularjs
  - javascript
author: szabgab
archive: true
---


Trailing closely the [Hello world](/getting-started-with-angularjs),
the [Echo](/angularjs-first-binding), and the [simple calculator](/calculator-in-angularjs)
examples, creating a TODO list is one of the rite of passage entering the world of whatever
language or environment. Let's see how to implement a TODO using AngularJS.


## Simple TODO list

After loading `angular.min.js` we create an Angular JS module called `todoApp` and
a controller called `todoController`. Inside the controller we set up an empty array
called `tasks` that will hold the todo list.
We make it an attribute of the current `$scope` in order to make it accessible form the HTML.

We also declare a function called `add` (also an attribute of the `$scope`) that takes the
value of `title` (we'll later see this is the name of the `input` box), and appends it
to the list of tasks using `push`. That's all the JavaScript code we need for a simple TODO list.

In the HTML part we have a `div` element that defined the area of the
AngularJS Application `ng-app` and the Angular JS controller `ng-controller`.

Inside the controller in the HTML we have two parts. The first part is an `input` element
connected to the `$scope.title` attribute using `ng-model` and a button that uses
`ng-click` to launch the `$scope.add` method when the button is clicked.

The second part uses the `ng-repeat` directive to iterate over the elements of the `$scope.tasks`
array and display them one-by-one as list items.

{% include file="examples/angular/todo1.html" %}

[view](examples/angular/todo1.html)

## Submit input box on pressing ENTER

It is a bit cumbersome that for every additional item we need to click on the button.
It would be much better if we could just press ENTER. In order to do that we had to wrap
the `input` element in a `form` and in the form add an `ng-submit`
directive calling the `$scope.add` function. At the same time, in order to eliminate
duplicate calling of the `$scope.add` function.

```html
  <form ng-submit="add()">
  <input ng-model="title"><button>Add</button>
  </form>
```

## Duplicate values in ng-repeat

If yo have tried the above example, you might have noticed that adding the same element twice
will crash the application. The reason is that by default the `ng-repeat` directive
assumes unique values in an array. I am not sure if having the same value in a TODO list
is actually desirable, but for now I'd like to be able to allow the user to enter the same value
twice. To do so we can tell `ng-repeat` to use the `$index` of the array for tracking
values like this:

```html
<li ng-repeat="t in tasks track by $index">{{ t }}</li>
```

## Deleting an element from the TODO list

While for most of us the reality is that we have an ever growing TODO list, but sometime
we get lucky and manage to finish an item. (Or maybe it just gets cancelled.) We would like
to have a way to remove an element. For that we are going to add a button next to each item,
and clicking on that button will remove the specific element from the array of tasks.

Adding the button is simple:

```html
<button ng-click="delete()">x</button>
```

The appropriate `delete` function made me scratch my head a bit, but finally I
got it:

```javascript
$scope.delete = function() {
    $scope.tasks.splice(this.$index, 1);
}
```

When running the `delete` function `this` contains an attribute called `$index` that
seems to indicated the index in the current list. We can use that to locate the element in the
`tasks` array. Using the plain JavaScript `splice</a> function we remove one element from
the array that immediately updates the list displayed on the HTML page.

{% include file="examples/angular/todo2.html" %}

[view](examples/angular/todo2.html)
