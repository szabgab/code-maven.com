---
title: "JavaScript module to run both in a browser and in Node.js"
timestamp: 2015-06-25T09:15:01
tags:
  - Node.js
published: true
books:
  - javascript
  - cm
author: szabgab
archive: true
---


One of the selling points of using Node.js to write the back-end of your application is that in that case you use the same programming
language in the back-end as you use in the front-end. Then it is easy to share code between the two.

The question then, how can one write a library in JavaScript that can be used both in Node.js and in the web client.



This is a simple library with two methods: `add` and `div`, and an attribute `version`
It uses `this` which refers to the Window object when running in the browser and to the global object when running under Node.js

{% include file="examples/js/node_and_web/calc.js" %}

We can see it working in Node:

{% include file="examples/js/node_and_web/calc_test_node.js" %}

```
$  node calc_test_node.js
calc_test_node
7
4
0.01
```


We can see it working in the web as well. For that we need to write some JavaScript code:

{% include file="examples/js/node_and_web/calc_test_web.js" %}

and then we have to load first the `calc.js` and then the JAvaScript file that uses the `Calc` object:

{% include file="examples/js/node_and_web/calc_test_web.html" %}

[view](examples/js/node_and_web/calc_test_web.html)

If you click on "Try" you will see it working. Just remember you need to open the JavaScript console to see anything.

