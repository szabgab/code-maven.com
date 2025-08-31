---
title: "Handlebars with dynamically loaded and cached template"
timestamp: 2015-06-03T18:30:01
tags:
  - Handlebars.compile
  - jQuery.get
published: true
books:
  - handlebars
  - jquery
author: szabgab
archive: true
---


In the earlier examples in the [Handlebars tutorial](/handlebars) we
always had the templates, which are themselves small HTML snippets,
embedded in the HTML file as a script tag. That makes it hard to edit them
and get confusing. It might be better to load the templates dynamically
as they are needed.

Then of course if the same template is needed more than once, it would save time
if we could cache the already compiled template.



## The HTML file

The HTML file for this example is fairly simple.
We load `handlebars.min.js` from the CDN.
We also load `jQuery` from its CDN. Instead of the plain JavaScript
Ajax call we used earlier, we are going to use the Ajax functionality of jQuery.

Finally we load `handlebars_dynamic_loader.js` that holds our JavaScript code.

The `body` of the HTML page contains a `button` and an empty `div`,
waiting for us to fill.

{% include file="examples/js/handlebars_dynamic_load.html" %}

[view](/examples/js/handlebars_dynamic_load.html)

## The Template

The template we use in this examples is the most simple template there can
be. In this article we are only interested how we can dynamically load the
templates from the server.

{% include file="examples/js/handlebars_template_show.htm" %}

## The JavaScript code gluing it all together

This is the main part of the example.

{% include file="examples/js/handlebars_dynamic_loader.js" %}

We have a global object called `templates` that will hold the compiled templates.
Each template has a name. The name will be the key in the object, and the value will be the
content of the template.

The `display_template` function expects the name of a template, and the data that
needs to be sent to the template. After making sure, the template actually exists,
it will copy the template to the variable also called `template`

```javascript
var template = templates[tmpl];
```

Then it will run this template filling it with the data it received:

```javascript
template(data);
```

Remember, we are planning to store the already compiled version of the template
that is actually a JavaSCript function object.

The final step of the `display_template` function is injecting the generated
HTML in the DOM.

## The click event handler

In the callback of the jQuery document ready we attach an event handler to the button we have
on the page. In order to make the code more generic, I put the name of the template in the
`name` variable, and the data I'd like to show in the `data` object.

Then if the `templates[name]` is empty, that is, if this is the first time we would like
to use the given template, we need to fetch it from the server with an Ajax request.
When the response arrives, we can compile it using

```javascript
Handlebars.compile(resp);
```

and assign that value to the `templates[name]` for later reuse.

Then we can call the `display_template` function.

In case we already had the template in the memory, we can directly call the `display_template`
function.

## Improved JavaScript code

After writing all that down I had an idea for improvement. After all, in a real application
I'll have several jQuery callbacks that will trigger the use of templates. Each one of them
will need to load the template from server. So better hide all that in a single function,
the `display_template` function:

{% include file="examples/js/handlebars_dynamic_loader_improved.js" %}

In this solution, the code fetching the raw template from the server was
moved inside the `display_template` function. It is called if the
template is not in the `templates` object.

## Comments

Do you think its beneficial to rend a new file with a 2/3 same partials and the middle partial missing or doing what you do here?


