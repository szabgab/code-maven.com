---
title: "How to exit a Node.js script"
timestamp: 2015-01-31T08:30:01
tags:
  - process
  - exit
published: true
books:
  - nodejs
author: szabgab
archive: true
---


Normally a Node.js script stops running when it reaches the end of the script and when there are no more event handlers waiting for events.
What if you want the script to stop earlier?


It's quite easy.

The built-on [process](http://nodejs.org/api/process.html) module has a method
called [exit](http://nodejs.org/api/process.html#process_process_exit_code):

{% include file="examples/node/process_exit.js" %}

## Comments

ctrl+C twice

or type:

.exit

---

nice

---

It was just what I was looking for. Thank you very very much

