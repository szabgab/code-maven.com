---
title: "Materialize CSS: Side-nav with Vanilla JavaScript on both sides"
timestamp: 2022-08-17T11:00:06
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


We already saw how to create a [Side-nav with Vanilla JavaScript](/materialize-side-nav-vanilla-javascript)
in [Materialize](/materialize). Now we are goint to create two. A left-side navbar and a right-side navbar.

For more details see the documentation of the [sidenav](https://materializecss.com/sidenav.html)


{% include file="examples/materializecss/2-side-nav-vanilla-javascript.html" %}

[view](examples/materializecss/2-side-nav-vanilla-javascript.html)

In order to open the left-side navigation bar the user needs to click on the "show main menu" link.
In order to open the right-side navigation bar the user needs to click on the "show secondary menu" link.

The bar automatically closes when the user clicks on the content of the page outside the navbar.

The main by sidenav is aligned to the left side of the screen. The secondary is aligned to the right-side of the screen.

At the bottom of the file you can see the JavaScript code. In this example we searched for the navbars one-by-one using their ID
and then initialized them separately using (slightly) different options.

I also included a commented out line of code that would open the navbars when the page is loaded.

You could also use the <b>open<b> method if you wanted to open the secondary navbar when the user selected something on the primary navbar.

In this example I also tried to add a second level of hierachy to the links in the sidenav. It was not really successful.
In the first case I had a title that was not a link itself and it got outdented. In the second case everything was just in the same column
so the hiearachy is not visible to the users.
