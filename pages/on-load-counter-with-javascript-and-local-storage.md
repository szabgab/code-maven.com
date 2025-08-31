---
title: "On-load counter with JavaScript and local storage"
timestamp: 2015-03-28T09:20:01
tags:
  - localStorage
  - getItem
  - setItem
  - removeItem
  - getElementById
  - addEventListener innerHTML
published: true
books:
  - javascript
author: szabgab
description: "Simple Vanilla JavaScript example useing localStorage, getItem, setItem, getElementById, addEventListener, innerHTML to create a counter."
archive: true
---


As part of the big [Counter Example](/counter) project,
in this article we'll see how to create a simple load-counter
with plain JavaScript utilizing the Local Storage introduced in HTML5.


In HTML5 <b>localStorage</b> is a term used for a flat key-value database inside the browser (or more specifically on
the hard-disk of the computer, table, or smartphone where the browser runs) that can be accessed using JavaScript.

This is a very simple example showing a counter that will increment by one every time you reload a a page.
As the counter is saved in your own browser and it is associated with the site you visited, this number will be
independent of what other people see, or what you'll see if you visit the same page using a different device
or even a different browser on the same devide.

{% include file="examples/js/counter_on_load.html" %}

[view](examples/js/counter_on_load.html)

Click on the <a href="/try/examples/js/counter_on_load.html" target="_new">Try!</a> link to see how it works in a separate window.

The example contains a single HTML `div` element that has a unique ID `counter` and a piece of JavaScript.
The `getItem` method of the `localStorage` class will fetch the current value of the given key (in this case 'on_load_counter')
and assign it to `n`.

The first time we load the page there won't be such key, and thus `getItem` will return a `null` value.

Next we check if the retreived value was indeed `null` and if it was, we initialize our counter to 0.

Then comes the incrementing of the counter `n++;`.

Then using the `setItem` method of `localStorage` we set the value of the 'on_load_counter' key to whatever is in `n`.

The final step is displaying the new number on the HTML page.  `document.getElementById('counter')` provides access to HTML
element with the id `counter` and then we set its content to be the value of n.


## Reset the counter

In the next example we are going to add a button to reset th counter, but first we'd like to observe something else.
If you click on the <a href="/try/examples/js/counter_on_load_reset.html" target="_new">Try!</a> link you'll open this second example
which has a different URL, but resides on the same site. You'll see the counter on this page starts from the number where
you left the first page. Actually if you click on the two pages alternately, you'll see that they are actually mapped
to a single counter, to a single storage location.

{% include file="examples/js/counter_on_load_reset.html" %}

[view](examples/js/counter_on_load_reset.html)

In this example we added another HTML element, a `button` with an ID of `reset`.
In the JavaScript code we added a function called `reset_counter` that, if called, will use the `removeItem` method
of `localStorage` to remove a key/value pair from the local storage.

In the last line we use `document.getElementById('reset')` again to identify the HTML button, and then we attach an
event listener using the `addEventListener` method. This will make JavaScript execute the `reset_counter` function 
every time the given HTML element (the 'reset' button) is 'click'-ed.

If you open this example using the <b>Try!</b> link, you'll see the counter and the button. When you click on the button it will
seem that nothing happened. That's because we have not updated the page after reseting the counter. The only thing that really
happened is that we removed the key-value pair from the local storage.

If you'd like to play with this example, then add some code that will autmatically display the new value of the counter, after clicking
on the reset button.


