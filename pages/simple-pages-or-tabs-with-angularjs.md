---
title: "Simple pages or tabs using AngularJS"
timestamp: 2015-09-28T13:30:01
tags:
  - ng-show
  - ng-init
  - ng-click
published: true
books:
  - angularjs
author: szabgab
archive: true
---


Even though we are calling this applications <b>"Single Page Applications"</b>, because we let the browser talk to the server behind the
scenes, in the end in many application we'll have multiple "views". For example Gmail has the "list inbox" view and the "show single email" view
and probably a few other views.


## Simple page with multiple tabs

This is probably the most simple implementation:

{% include file="examples/angular/simple_pages.html" %}

[view](examples/angular/simple_pages.html)

We created a variable called `page` which is actually connected to the `$scope`, but that's not relevant to us now.

We have two `div` elements using `ng-show` with a simple condition to decide if they need to be shown or not. Basically these two div
elements are the two pages or tabs.

There is a single `div` element with< `ng-init` that sets the initial value of the `page` variable, and thus sets the initial page.


Finall, but what comes at the top of the page, are two buttons. Each one with an `ng-click` directive that will set the `page` variable
when the user clicks on the button. If you try this page, you'll see you can easily switch between the two pages, or two tabs by clicking on the button.

It is also very easy to add more pages with their appropriate buttons. 
