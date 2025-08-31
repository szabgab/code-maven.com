---
title: "Materialize CSS: Side-nav with hierarchy"
timestamp: 2022-08-17T16:00:06
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


We had a failed attempt to create hierarchy in the sidenav while creating [Two side-navs with Vanilla JavaScript - left-hand side-nav and right-hand side-nav](/materialize-2-side-nav-vanilla-javascript).
[Materialize](/materialize) has [collapsibles](https://materializecss.com/collapsible.html) that can be used for this.

For more details see the documentation of the [sidenav](https://materializecss.com/sidenav.html)


{% include file="examples/materializecss/side-nav-with-hierarchy.html" %}

[view](examples/materializecss/side-nav-with-hierarchy.html)

In order to open the side navigation bar the user needs to click on the "show main menu" link.

We had to initialize both the sidenav and the collapsible in the JavaScript code.

In order to see the little triangle to open the second level of items we had to include the Material fonts (the second `stylesheet` include at the top of the file).

