---
title: "Counter Example: Vanilla JavaScript"
timestamp: 2023-01-03T16:30:01
tags:
  - JavaScript
published: true
books:
  - javascript
author: szabgab
archive: true
show_related: true
---


This code is part of the [counter example](/counter) project. If you are looking for the buzz-words for this project then this is a Single Page Application implemented using HTML5
and Vanilla JavaScript.

It has two buttons.
<ol>
    <li>One of them is a counter. Every time you click on it the value on it will increase by one.</li>
    <li>The other one is a reset button.</li>
</ol>


{% include file="examples/javascript/vanilla-javascript-counter.html" %}

[view](examples/javascript/vanilla-javascript-counter.html)

At the top of the file we have two HTML buttons. Both have IDs for easier identification.

The JavaScript code has two functions and then two calls to <b>document.getElementById</b>.  These two calls will locate the HTML element with the ID given as a parameter and then connect a function to the "click" event  of each one of them. These are the two functions we have.

This means that when the user clicks on the HTML element with the ID <b>counter</b> the function <b>increment_counter</b> will be executed and when the user clicks on the element with the ID <b>reset</b> the <b>reset_counter</b> function will be called.


![](/static/img/vanilla-javascript-counter.gif)

In this little animated gif you can see the two small buttons at the top and most of the view is taken up by the console where you can see the `console.log` messages.


## Reset counter

The <b>reset_counter</b> function is the easier to explain:

```javascript
console.log('reset');
```

Is only there so we can see on the console of the browser that something happened.
Then we use the call

```javascript
document.getElementById('counter')
```

to locate the HTML element and innerHTML to set the content of the element to 0.

## Increment counter

Here we first copy the content of the HTML element to a variable we cleverly named <b>counter</b>.

Then we increment it by one using the <b>++</b> operator.

Then we have the <b>console.log</b> call. Just so we can see in the console what's happening.

Finally we write back the value the HTML document.

## Issues

Keeping our data (the counter) as part of the HTML is probably not a very good idea in a project more complex than this one. However, in this case it has the advantage that we don't need to think how we keep our data (which is normally in JavaScript) in sync with the display (which is the HTML).

This counter is also not persistent. If you reload the page the counter will be reset.




