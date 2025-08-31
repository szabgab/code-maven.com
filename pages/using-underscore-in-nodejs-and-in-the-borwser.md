---
title: "Using Underscore in Node.js and in the browser"
timestamp: 2015-06-20T11:00:01
tags:
  - _
published: true
books:
  - nodejs
  - javascript
  - cm
author: szabgab
archive: true
---


[Underscore.js](http://underscorejs.org/) provides lots of small functions to
help you use JavaScript as a functional programming language. Besides the actual functions it provides,
it can also be great for learning more JavaScript as it provides an annotated version of its source code
and it also allows us to use it both as a Node.js module and in the browser.

Let's see how is that done.


## Use Underscore in Node.js

Install Underscore.js using `npm install underscore`, that will install it
locally in the `node_modules` subdirectory. Then write the following code:

{% include file="examples/js/node_underscore.js" %}

and run it `node node_underscore.js`

The output is

```
[ 1, 4, 25, 9 ]
```

We loaded the module using the `require` function and assigned it to the `_`.
Actually we could have used any variable name, but because this is the "underscore" module
we use the underscore `_`.

Then we could use the `map` method of this new, `_` object.

## Use Underscore in the Browser

For this we can download Underscore, or we can use a copy of it from a CDN.
In either case we need to create an HTML file that will load the underscore library
and then it will load our own script:

{% include file="examples/js/web_underscore.html" %}

[view](examples/js/web_underscore.html)

We could have added the HTML header and body, but non of those are required for this to work.

Our script then can look like this:

{% include file="examples/js/web_underscore.js" %}

It looks exactly the same as the code in Node.js, except that we've already loaded the
Underscore module in the HTML file and it automatically assigned it to the `_` variable.

