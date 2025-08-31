---
title: "Handlebars with (slightly) complex data"
timestamp: 2015-04-01T21:00:01
tags:
  - Handlebars
published: true
books:
  - javascript
  - handlebars
author: szabgab
archive: true
---


In the article where we looked at [Handlebars the JavaScript templating engine](/introduction-to-handlebars-javascript-templating-system) for the first time,
there was a working example, but it was probably not very convincing as to why using Handlebars is much better than concatenating the HTML snippet
together in plain JavaScript.

Then there was this example with an [Ajax request returning JSON data](/ajax-request-for-json-data).
There too we used plain JavaScript code but that was already quite unpleasant. Let's now see how can we do the same using Handlebars.


In the earlier example we received a JSON response with the following content:

{% include file="examples/js/data.json" %}

We used this code:

{% include file="examples/js/ajax.js" %}

[Try it here!](/try/examples/js/ajax.html)

## Using Handlebars

The `ajax_get` function remained the same. It is explained in the article
about [Ajax request](/ajax-request-for-json-data).

The change is in lines 23-25, where instead of concatenating the HTML piece-by-piece, we 
fetch the template from the `text-template` tag, compile this template-source into
a function called `template` and then we just pass the data we have received by
the Ajax request to this `template()` function. Much cleaner than earlier
when we had to think about using single-quotes outside so they won't interfere with the
double-quotes we wanted to use for the HTML attributes.

{% include file="examples/js/ajax_handlebars.js" %}

The template itself is located in the HTML file in a `script` tag.

{% include file="examples/js/ajax_handlebars.html" %}

[view](examples/js/ajax_handlebars.html)

The place-holders for `{{title}}` and `{{description}}` are simple values that we have already seen
in the [introduction to Handlebars](/introduction-to-handlebars-javascript-templating-system), but there is also a loop
to go over the elements of an array.
`{{#each articles}}` starts a loop on the elements of the array in the `articles` key.
The loop ends when we encounter `{{/each}}`.
Inside the loop we can use the keys of the objects that are the elements of the `articles` array.

This makes the template much clearer than what we had in the HTML concatenation earlier.

