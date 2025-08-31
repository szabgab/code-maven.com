---
title: "Show ads to visitors based on referrer using JavaScript only"
description: "Show or hide HTML snippets (ads or anything else) to people based on the previously visited site."
timestamp: 2015-10-02T18:30:01
tags:
  - JavaScript
  - document.referre
  - document.getElementById
  - style.display
published: true
books:
  - javascript
author: szabgab
archive: true
---


You might want to treat visitors to your site differently based on where they came from. Especially if they came from another
page on the same site. You can easily achieve this using some JavaScript code and looking at the `referrer`.


{% include file="examples/js/ads_to_selected_visitors.html" %}

[view](examples/js/ads_to_selected_visitors.html)

In most browsers the attribute `document.referrer` contains the page that was visited earlier.
It is normally set by the browser wen you click on a link or when you are somehow forwarded from one page to another.

If you type in a new URL in the address bar and press ENTER them this attriibute will be empty.

We can use this attribute to identify which other site and which page sent the visitor to us.
We can use the full value in `document.referrer` or we can extract part of if. For example
`document.referrer.split('/')[2]` will extract the domain name.


We can then locate an HTML element using `getElementById` and the `id` of the element and we can
set the `display` attribute  to either `'none'` to remove the element  from the DOM and make it disappear,
or we can set it to `'block'` to show it. (We could also set it to `'inline'` if you'd like to show it in the
same line as another element. There are a few additional values it can take, but these are the most common.

In our code example we have two `div` elements. One of them is shown to 'internal visitors', the others to everyone else.
Of course, you could use similar conditions to show specific message to people coming from Google or from any other site.

## Comments

not working

---

my bad, works but it must be exactly the same url. Meaning that if you are on www.code-maven.com, this code won't work. It must be changed to code-maven.com (without www prefix).
