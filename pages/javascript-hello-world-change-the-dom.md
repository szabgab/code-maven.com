---
title: "JavaScript Hello World - changing the DOM with getElementById and innerHTML"
timestamp: 2015-03-29T14:02:01
tags:
  - DOM
  - document
  - getElementById
  - innerHTML
published: true
books:
  - javascript
author: szabgab
archive: true
---


In the [introduction to JavaScript](/introduction-to-javascript) we saw `document.write`
that will change the content of the web page the user sees, but it has very little control over the location
where the it changed the HTML page.  More specifically it writes to the same place where it is executed
within the HTML page. That makes it very inflexible.

We can do better by fetching an object representing a DOM element and using the `innerHTML` on that DOM
element to changes its content.


First of all, the DOM - [Document Object Model](http://en.wikipedia.org/wiki/Document_Object_Model)
is basically the representation of the HTML page by JavaScript objects. It is the heart of the interaction between
plain JavaScript and the HTML in the browser. When we used `document.write` in [introduction](/introduction-to-javascript)
we changed the HTML, which also changed the DOM.

In this example we change the DOM, which will change the HTML that appears in the browser.

The advantage of this is that regardless the location of our JavaScript we can access and change
any part of the DOM and thus and part of the HTML. The only thing that is important regarding the relative
location of the HTML we want to change and the JavaScript that will change it is that the HTML already has to
be loaded and parsed by the browser when the JavaScript code tries to access it.

This can be achieved either by putting the JavaScript code after that HTML (or loading the JavaScript after the HTML),
or if the JavaScript is loaded before the HTML, then somehow telling it to wait till the page is loaded.
There are several solutions for the latter, but for simplicity we are going to use the former. We simply place
our JavaScript code after the HTML.

In order to be able to change a DOM object, first we need to fetch the object. There are plenty of methods to do that,
but probably the most simple one is the `getElementById` method of the `document` class.
In the next snippet the call `document.getElementById('display')` fetches the object representing the HTML
element that has the id <b>display</b>.

One of the attributes of this object is called `innerHTML`.
If we assign a value to it, that will change the content of the appropriate HTML element.

In this example you can see a simple `div` element (we could have used any element, but divs are sort of neutral
and that's why they are used usually) with an id <b>display</b>.

{% include file="examples/js/set_innerhtml.html" %}

[view](examples/js/set_innerhtml.html)

## Comments

Putting the JavaScript code after the HTML is loaded does not always work. I ran into this after making a HTML, CSS, JavaScript app using PHP desktop.

For whatever reason, the HTML was not completely loaded and there was a need for a 400 millisecond delay before executing the JavaScript code to fill the DIV tags.

Just keep this in mind should you run into that scenario and your JavaScript can't find the HTML tags after the page is loaded.
