---
title: "Introduction to Handlebars, the JavaScript templating system"
timestamp: 2015-03-31T12:50:01
tags:
  - Handlebars
  - compile
  - template
published: true
books:
  - javascript
  - handlebars
author: szabgab
archive: true
---


In the article about [input and output with JavaScript](/input-output-in-plain-javascript)
you could see the the problem of creating HTML snippet on-the-fly to be included in the rest of the page.

[Handlebars](http://handlebarsjs.com/) is a templating system for JavaScript that provides
help to reduce anxiety over the creation of such pages.

Let's convert the plain JavaScript example to use Handlebars.


## Pure JavaScript version

This is the example from the [input and output with JavaScript](/input-output-in-plain-javascript) article:

{% include file="examples/js/pure_js_greating.html" %}

[view](examples/js/pure_js_greating.html)


## Switching to Handlebars

This is the solution using Handlebars:

{% include file="examples/js/handlebars_greating.html" %}

[view](examples/js/handlebars_greating.html)

In order to use Handlebars, first we need to load the Handlebars library. We can use it directly from
[CDN JS](https://cdnjs.com/):

```
<script src="https://cdnjs.cloudflare.com/ajax/libs/handlebars.js/3.0.1/handlebars.min.js"></script>
```

or we could download the same file to our server and load it from there.

We create an HTML snippet and put place holders in double curly braces in it:

```
Hello <b>{{first_name}}</b> {{last_name}}
```

We can deliver the template to the HTML in several ways, but one of the recommended ways is to embed
it in the `head` of the HTML file withing `script` tags with a unique `id`.
This way we can easily include several templates and it is much clearer how we would like the final HTML
to look like.

```
<script id="text-template" type="text/x-handlebars-template">
   Hello <b>{{first_name}}</b> {{last_name}}
</script>
```

Then we arrive to JavaScript part. In the JavaScript code we replaced the single line
combining the content of `fname`, `lname` with some HTML that looked like this:

```
var html = 'Hello <b>' + fname + '</b> ' + lname;
```

with new code:

```
var source   = document.getElementById('text-template').innerHTML;
var template = Handlebars.compile(source);
var context = {first_name: fname, last_name: lname};
var html    = template(context);
```

I know, it looks more complex than we had earlier, and indeed in such a simple case
when we only need to embed the content of two varaibles in a simple HTML snippet,
this might be overengineering, but as your application grows you'll see that
the complexity of the pure JavaScript version would increase while for Handlebar,
basically that's the whole complexity.

Let's go over those 4 lines.

In the first line we access the `script` element with the id `text-template` where we put the template and using `innerHTML`
we copy its content to the variable called `source`.

In the second line we compile this template and create a Handlebars object using the `Handlebars.compile()` method. Actually
what the `compile` method returns is a function that we'll call later.

In the third line we create a mapping from keys that will match the place holders to the values that will replace the place holders.
These are the values we got from the `input` elements. This is just a plain JavaScript object. Nothing special.
(You'd call it a hash, associated array or dictionary depending on which other language you are familiar with.)

Finally we ask the template to replace the place holders by the respective values and assign the generated string to the variable `html`


After that we can go back to what we also had in the plain JavaScript code and embed the new HTML in the existing DOM using

```
document.getElementById('result').innerHTML = html;
```

That's it about the basics of Handlebars. If you'd like to learn more, you can check out the
documentation on the web site of [Handlebars](http://handlebarsjs.com/)

## Comments

Hello!! Your article is excellent it has provided me with good information. I need your help in solving one problem I am using handlebarjs for templating. I have three templates in one single file and a singal json object (ie array of objects within array of objects) depending on the condition in one of my helper function i am trying to nest a template into parent template. I can share the piece of code with you.


