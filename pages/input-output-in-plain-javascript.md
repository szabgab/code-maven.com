---
title: "Input Output in plain JavaScript"
timestamp: 2015-03-31T09:30:01
tags:
  - getElementById
  - value
  - addEventListener
published: true
books:
  - javascript
author: szabgab
archive: true
---


In the first article we saw [how to change the DOM to display something](/javascript-hello-world-change-the-dom),
and then we saw how to [handle user events](/handling-events-in-javascript). This time we are going to see how to
get input from the user and combine that with the other two, to create a simple page that can great you.


{% include file="examples/js/pure_js_greating.html" %}

[view](examples/js/pure_js_greating.html)

In this example we have a bit more HTML than earlier. In addition to having a `button</h>, and a `div` element
where we'll show our results, we also have two `input` elements. Each one with its own ID.

If you click on the Try link, you'll see two input boxes and a button:

<img src="/img/input_form.png" alt="Input form" />


In the JavaScript code we have a function called `say_hi`. It used the `getElementById` we have already
seen to locate the DOM element representing the input element with the id `first_name`. The object returned
has a method `value` that will return the text the user has typed in that field.

We use this technique to retrieve the content of both `input` fields and assign their content to two variables:
`fname` and `lname`.

Then, using these variable we create an HTML snippet and assign it to a new variable called `html`.

Then we set the `innerHTML` attribute as [earlier](/javascript-hello-world-change-the-dom) to show the
HTML we generated. The result might look like this:

<img src="/img/input_form_and_output.png" alt="Input form and output" />


## Creating HTML is cumbersome

Even in such a simple HTML we wanted to create we had to use `+` several time and the code is quite unreadable.
Imagine what would happen if we wanted to build a more complex application where we might want to build a list of items,
or even a table. Building the HTML on the fly and the inserting in the DOM would be quite nasty.

In the back-end systems written in Perl, Python or Ruby, people have encountered the same problem and the solution was
the creation of various templating engines. Basically a template would be an HTML snippet with some place holders
and then a function call that gets the HTML snippet (the template) as a parameter, and gets several key-value pairs.
The function then returns a new HTML snippet in which the place holders were replaced by the value of the appropriate key.

In a similar way, there are many templating system for JavaScript as well. We are going to look at
[HandlebarsJS, the JavaScript templating engine](/introduction-to-handlebars-javascript-templating-system).

