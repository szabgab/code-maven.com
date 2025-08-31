---
title: "Handlebars helpers"
timestamp: 2015-04-02T23:30:01
tags:
  - Handlebars.registerHelper
published: true
books:
  - javascript
  - handlebars
author: szabgab
archive: true
---


Besides the template language [Handlebars](http://handlebarsjs.com/) offers it also allows us to create handlers.
I think in other environments these might be called macros, or you can think about them as subroutine.

They allow us to create a reusable expression.


There are a number of examples of [block helpers](http://handlebarsjs.com/block_helpers.html) on the Handlebars site,
but I think I am going to show a few others. Let's start with probably the most basic possible helper. One that returns a static
HTML snippet.

## Static HTML helper

The full code looks like this and  you can try it by clicking on the `Try!` button.

{% include file="examples/js/handlebars_helpers_static.html" %}

[view](examples/js/handlebars_helpers_static.html)

The helper is a snippet of JavaScript code. A string (in our case `greeting`) mapped to a function.
That function can return a plain string that will be HTML escaped, or it can return a `SafeString`
object which will left  as it is. In our case, because we want to return an HTML snippet, we used the
`SafeString` object. Normally this code will go to an external JavaScript file. Probably
one shared by several projects.


```javascript
Handlebars.registerHelper('greeting', function() {
    return new Handlebars.SafeString( '<i>Hello World</i>' );
});
```

Now that we have a helper called `greeting` we can use it in our template code:

```javascript
    <script id="text-template" type="text/x-handlebars-template">
        <h3>{{greeting}}</h3>
    </script>
```

A template is just an HTML snippet with a few place holders.

The rest of the code in the example is just the regular Handlebars code that extracts the template from the
HTML code, compiles it and then generates the HTML snippet.

Of course showing Hello World is not that interesting, but maybe if the helper returned copyright information for a web site,
or if return the menu, then it might be more interesting.


## Link handler

The next example is base on one of the examples from the web site of [Handlebars](http://handlebarsjs.com/block_helpers.html).
This one already accepts a parameter. A JavaScript object that is expected to have an attribute called `url` and and optional
attribute called `text`. Given such an object, this handler will return an HTML link using the text as the anchor of the link.
If the 'text' is missing from the object then it will use the URL as the anchor.

The Full example looks like this:

{% include file="examples/js/handlebars_helpers_link.html" %}

[view](examples/js/handlebars_helpers_link.html)

The Handler looks like this:

```javascript
Handlebars.registerHelper('link', function(obj) {
    var url  = obj.url;
    var text = obj.text;
    if (text == undefined) {
        text = url;
    }
    return new Handlebars.SafeString( '[' + text + '](' + url + ')' );
});
```

Here we map the 'link' string to a function that accepts a single parameter. We copy the `url` and the `text`
attributes to the appropriate variables, but we use the `url` as text if no text was given.

Then we manually construct the HTML. This seems to set us back a bit to the age of HTML concatenation, but remember this
will be placed in an external JavaScript file and will be reused throughout a project, or even more projects. We could have use
the Handlebars templating system recursively here, but that seems a bit unnecessary.

Once we have created this Handler, we can use it in our template:

```javascript
    <script id="text-template" type="text/x-handlebars-template">
        {{link home}}<br>
        {{link perlmaven}}<br>
    </script>
```

As opposed to the static case we saw earlier this time we use the new `link` keyword along with a parameter.
Once the parameter is 'home', and once it is 'perlmaven'. These are the place holders that will be replaced by data
passed to the `template()` function.

Finally, let's see the call to the `template()` function along with the data we pass to it.
Here you can see that we pass an object with two attributes, 'home' and 'perlmaven'. These will be mapped
to the appropriate place holders in the template. Note, that for 'home' we provided both the 'url' and the 'text',
while for 'perlmaven' we only provided 'url'.

```javascript
    var html = template({
        'home' : {
           'url'  : '/',
           'text' : 'Code Maven'
        },
        'perlmaven' : {
            'url' : 'https://perlmaven.com/'
        }
    });
```

The result you an see for yourself will be

[Code Maven](/)<br>
[http://perlmaven.com/](https://perlmaven.com/)<br>




