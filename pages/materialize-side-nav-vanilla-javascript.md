---
title: "Materialize CSS: Side-nav with Vanilla JavaScript"
timestamp: 2022-08-17T11:00:05
tags:
  - Materialize
  - sidenav
published: true
books:
  - javascript
  - html
  - css
author: szabgab
archive: true
show_related: true
---


[Materialize](/materialize) has several features that require the use of JavaScript. One of the is the side navigation bar.

For more details see the documentation of the [sidenav](https://materializecss.com/sidenav.html)


{% include file="examples/materializecss/side-nav-vanilla-javascript.html" %}

[view](examples/materializecss/side-nav-vanilla-javascript.html)

In order to open the navigation bar the user needs to click on the "show menu" link.
The bar automatically closes when the user clicks on the content of the page outside the navbar.

By default the navbar is aligned to the left side of the screen. In our example we used the "edge" field of the "options"
to make it appear on the right side.


At the bottom of the file you can see the JavaScript code. In this example we searched for <b>all</b> the navbars (even though we only have one in our example)
and then initialized all of them by a single call using the same options. If you have more than one navbar you could locate each one of them by their id
and initialize each one of them with different options.

I also included a commented out line of code that would open the navbar when the page is loaded.

