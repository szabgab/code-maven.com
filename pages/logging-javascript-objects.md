---
title: "Showing objects in the JavaScript console without going mad"
timestamp: 2016-10-18T21:30:01
tags:
  - JSON.parse
  - JSON.stringify
published: true
books:
  - javascript
author: szabgab
archive: true
---


We have already seen how to [print logging in JavaScript](/logging-in-javascript), but the really interesting
part is when we would like to see the content of variables. Especially variable that hold objects.

It is actually quite easy, but there is a catch.


## Logging JavaScript object

In this example we create a simple object and then use the `console.log` function to print
it to the [JavaScript console of the browser](/open-javascript-console).

{% include file="examples/javascript/logging/logging_object.js" %}

The result shows the object. In Chrome, after clicking on the small `+` sign it looks like this:

<img src="/img/javascript_logging_object_chrome.png" alt="Logging JavaScript object in Chrome" />

Here is the HTML you might need to try it right here.

<try file=examples/javascript/logging/logging_object.html">

## Logging JavaScript object that changes

Printing out the content of an object is important, but we usually do that when we would like to see
how has the content changed. So let's see how does that work out.

In this example we have created the same object as above, printed it to the console, changed it, and then printed it again:

{% include file="examples/javascript/logging/logging_changed_object.js" %}

<img src="/img/javascript_logging_changed_object_chrome.png" alt="Logging JavaScript changed object in Chrome" />

Oh-oh. That does not look good. The JavaScript object printed both before and after the change has the same content.
In this example it is obvious that there is some problem, but in the real world this object might further change before
you look at the output and it will always reflect the last state of the object and not the one that was in it when you called
`console.log`

No matter what, you'll spend a lot of time wondering what's going on in your code.

The problem is that in some browsers (at lest Chrome), the `console.log` does not really print the
object. It only "connects" it to the console. So when you look at it later you'll see the content
of the object at the time when you look at the object.

You can try it yourself with the following HTML that loads the above JavaScript.

<try file=examples/javascript/logging/logging_changed_object.html">

## Clone the object before printing

The solution is to copy the content of the object when printing it to the console.
There are a number of ways to do that in plain JavaScript. We are going to see one
using the `stringify` and `parse` methods of the `JSON` object.

Effectively for every logging we first convert the object to a [JSON string](/json)
and then convert it back to a JavaScript object before sending it off to `console.log`.

{% include file="examples/javascript/logging/logging_cloned_object.js" %}

The output now looks as we expect. The content of the object is shown properly.

<img src="/img/javascript_logging_cloned_object_chrome.png" alt="Logging JavaScript cloned object in Chrome" />

You can try it yourself using this HTML file:

<try file=examples/javascript/logging/logging_cloned_object.html">

`Solutions`

There are a number of ways to achieve similar results.

We used the  `JSON.parse(JSON.stringify(obj))` to create a real clone and let the browser do its folding of the data structure.

If you'd like to type less it is enough to write `JSON.stringify(obj)`,
but then you get a single string which might be hard to read if the object has a lot of data in it.

You could also use the longer `JSON.stringify(obj, null, 4)` that will beautify the
content of the object by showing each element on a separate line and indenting the internal
elements 4 spaces.

The drawback of these options is that a large object might take up a lot of
real-estate in the console and it might be harder to navigate.

You'll have to experiment yourself.

## Cloning JavaScript object in AgularJS

If you are using [AngularJS](/angularjs) you can use the
`angular.clone(obj)` method to clone the object.

## Cloning JavaScript object in JQuery

In JQuery there is a method called [extend](https://api.jquery.com/jquery.extend/) that can
achieve the same this way: `$.extend({}, obj)`.

## Comments

Hey
Its really helped..thanks a lot

---

Me trying the wrong code (examples/javascript/logging/logging_changed_object.js):

Before Change {fname: "Foo", lname: "Bar"}
Acter Change {fname: "Foo", lname: "Bar", email: "foo@bar.com"}

Anyway, there's a typo: "Acter" instead "After".

---

What about if the object has 'get' and 'set'?
function Foo() {}
Foo.prototype = {
get val() {
return {
bar: 3
}
}
}

let foo = new Foo()
console.log(foo) // {}


