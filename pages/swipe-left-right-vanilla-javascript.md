---
title: "Mobile swipe left, swipe right of HTML pages using vanilla JavaScript"
timestamp: 2020-07-23T16:30:01
tags:
  - touchstart
  - touchend
  - addEventListener
  - getElementById
description: "Using Vanilla JavaScript recognize when the mobile phone user swipes leftor swipes right on yout page."
published: true
books:
  - javascript
author: szabgab
archive: true
show_related: true
---


At one point I wanted to add this feature to my [slides](/slides) but I later remove it as some of the pages
needed to have horizontal scrolling and this code did not work well together with that. Maybe the only thing I need
is to adjust some of the parameters. So check it out maybe by the time you read this, the swiping on my slides might work.

Anyway, if you have some HTML pages you might want to allow your users to move between pages, using JavaScript, but you don't
want to rely any of the JavaScript libraries.


{% include file="examples/javascript/swipe_vanilla.js" %}

1. Wrap the whole area where you'd like the swipe to work in a div with an ID=content.
1. Replace the two commented-out alert calls by function calls implementing the left-swipe and the right swipe actions.
1. Adjust the 3 numbers to your liking.
1. Done.

```
    var min_horizontal_move = 30;
    var max_vertical_move = 30;
    var within_ms = 1000;
```


