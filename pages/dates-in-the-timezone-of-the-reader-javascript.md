---
title: "Show dates in the timezone of the reader using JavaScript"
timestamp: 2021-05-07T08:30:01
tags:
  - Date
published: true
books:
  - javascript
author: szabgab
archive: true
show_related: true
---


I am running [live](/live) online events that people can join from anywhere in the world if they know when the events start. Computing and showing the
date and time in every possible timezone is exhausting and would be probably confusing to the reader. The best is to show the scheduled date and time
in their local time-zone.

Encouraged by the [posts of Mark Gardner](https://dev.to/mjgardner/localizing-dates-in-a-perl-web-application-with-javascript-1n24) I wanted to implement
it using JavaScript only. This is what I got:


In the first example we have a date string in the <b>mydate</b> variable and then we use the <b>toLocaleString</b> method with various <b>dateStyle</b> options
and <b>toLocaleDateString</b> options to show the date in different formats. You can click on the <b>try</b> link below the example to see the code running
in a separate tab.

{% include file="examples/javascript/date.html" %}

[view](examples/javascript/date.html)

See the list of [options of toLocalString](https://tc39.es/ecma402/#sup-date.prototype.tolocalestring)


## A more real-world version

In the second example you can see a more real-world version. The date string is in an attribute of a <b>div</b> element. It could have been
added there manually or by some back-end application with a template.

Then there is a function that check if there is an HTML element with the "localdate" id. Takes the attribute from it and uses the same
techniques as above to set the date in a nice format. (Use the <b>try</b> link to see it working.

{% include file="examples/javascript/localdate.html" %}

[view](examples/javascript/localdate.html)

## Live events

Now it is your turn to check out our [live](/live) events and join one.

