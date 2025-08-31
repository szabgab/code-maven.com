---
title: "Logging in JavaScript applications"
timestamp: 2016-10-02T07:30:01
tags:
  - console
  - log
  - debug
  - warn
  - error
  - info
published: true
books:
  - javascript
author: szabgab
archive: true
---


When writing a complex web application one of the important debugging tools is using the logging facility
the environment provides. This can help the developer see what's going in the application without interfering
with the real UI.


The standard way to print a message to the [JavaScript console of the web browser](/open-javascript-console)
is using the `log` method of the `console` object. It accepts a list of strings and objects and prints them to the console.

Actually, the `console` object has several additional methods that can be used to fine-tune the logging.
There `debug`, `info`, `log`, `warn`, `error`.

In our sample JavaScript code we use all 5 of them:

{% include file="examples/javascript/logging/logging.js" %}

If you'd like to try the code, here is the HTML file that will load it including a link
to the explanation on [opening the JavaScript console](/open-javascript-console)
in your favorite browser.

{% include file="examples/javascript/logging/logging.html" %}

[view](examples/javascript/logging/logging.html)

If you don't want to try it now, you can check out these screenshots of the output:

In Chrome the various methods have different color and accompanying icon:

<img src="/img/javascript_logging_in_chrome.png" alt="console logging in Chrome" />

In FireFox they are all the same color, but you still get a few icons:

<img src="/img/javascript_logging_in_firefox.png" alt="console logging in FireFox" />

In both case, the right-hand side of the log-line displays the line number in the original file which makes it
easier to understand which part of the code emitted the log message.
