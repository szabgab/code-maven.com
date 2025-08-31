---
title: "Infinite scrolling and footer don't work well together (not even on DEV.to)"
timestamp: 2022-11-23T07:30:01
tags:
  - Web
types:
  - screencast
published: true
author: szabgab
archive: true
show_related: true
---


I like the [DEV.to](https://dev.to/) website, I even [posted some articles there](https://dev.to/szabgab/), but the infinite scrolling on some of the
pages that also have a footer is driving me mad.


{% youtube id="LnW157GNMlg" file="infinite-scrolling-and-footer.mp4" %}

Go to the page of this article on  [DEV.to](https://dev.to/szabgab/infinite-scrolling-and-footer-dont-work-well-together-not-even-on-devto-3619) and press the END button on your keyboard.
It will jump to the bottom of the page where you'll see a footer with a number of links including one to [Forem](https://www.forem.com/) the platform DEV runs on.

However, if you open the [main page of DEV](https://dev.to/) or the listings of one of the [tags](https://dev.to/tags),
you will notice that after a very short period of time more content is loaded and the links disappear.
The automatic loading of additional content at the bottom of the page is called "*infinite scrolling*".
Unfortunately this is rendering the footer unusable on these pages making the whole experience very frustrating.

So frustrating that I decided to write a whole post about it :-)

I seemed to remember that I already complained about it, but did not remember where. I was also wondering if it only frustrates me or others as well.

So I went to the GitHub repository of the project and found several related issues:

* [Infinte scrolling needs to be fix on homepage](https://github.com/forem/forem/issues/11576)
* [Footer should be viewable](https://github.com/forem/forem/issues/9034)

And a discussion [Footer should be viewable](https://github.com/forem/forem/discussions/15322)

I have not been able to read all the comments, but I am surprised this issue still exists. I think I'd just remove the footer from all the pages that have infinite scrolling.

