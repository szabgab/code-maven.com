---
title: "Handlebars conditional"
timestamp: 2015-04-22T10:00:01
tags:
  - Handlebars.registerHelper
  - if_eq
  - comparison
  - iff
published: true
books:
  - javascript
  - handlebars
author: szabgab
archive: true
---


The [Handlebars JavaScript](http://handlebarsjs.com/) templating engine provide a single `if`-conditional with an optional `else`,
but that `if`-statement can only handle a single value, not an expression. You can write

```
{{#if name}}
..
{{/if}}
```

but you cannot write

```
{{#if name == 'Foo'}}
..
{{/if}}
```

Let's create a [Handlebars helper](/handlebars-helpers) that will provide this functionality.


## if conditional

Before creating the helper though, let's see a full example using the plain `if` statement.
There are two values in the data object: cond1 and cond2, true and false respectively. The rest of the
JavaScript code is just fetching the template and letting Handlebars process the data.

{% include file="examples/js/handlebars_if.js" %}

The template itself has two entries like this using each one of the variables:

```
{{#if cond1}}
    true
{{else}}
    false
{{/if}}
```

The full html code is this:

{% include file="examples/js/handlebars_if.html" %}

[view](examples/js/handlebars_if.html)

You can try it by clicking on the Try link. In the new page the "show" button will trigger the process.

## if_eq

In the next example we have implemented a [Handlebars helper](/handlebars-helpers) called
`if_eq`. It expects two parameters and will compare them using `==`.
The helper itself looks like this:

```javascript
Handlebars.registerHelper('if_eq', function(a, b, opts) {
    if (a == b) {
        return opts.fn(this);
    } else {
        return opts.inverse(this);
    }
});
```

The template using this looks like this: (`name` is an attribute passed to the `template` function.)

```
{{#if_eq name 'Foo'}}
      true
{{else}}
      false
{{/if_eq}}
```

The full JavaScript file also contains the data object and the
code we had earlier combining the template with the data:

{% include file="examples/js/handlebars_helpers_if_eq.js" %}

The full HTML file including the template looks like this:

{% include file="examples/js/handlebars_helpers_if_eq.html" %}

[view](examples/js/handlebars_helpers_if_eq.html)

You can try it after clicking on the "Try" link.

## Uncaught Error: if_eq doesn't match if - 3:7

When I encountered this error it took me quite a while to figure out what went wrong.
It might have been just something blocking my mind, I am not sure. Can you spot the  problem in the next example:

{% include file="examples/js/handlebars_helpers_if_eq_typo.html" %}

[view](examples/js/handlebars_helpers_if_eq_typo.html)

This happened when I started to convert my `if` conditional to an `if_eq` conditional, but I only changed the opening
expression from
```
{{#if ...}}
```
to
```
{{#if_eq ...}}
```
but not the closing expression that was left as
```
{{/if}}
```
.
Hence the error telling us that `if_eq` does not match `if`. Maybe if the error message had the keywords stand out,
it would have been easier.

Anyway, look out for such typos. They are a waste of time. Make some more interesting bugs!

## iff - for other conditionals

Finally we got to build the more generic helper for conditional expressions. I called it `iff`. I am aware of the mathematical
meaning of it, but it just looked cute and short to be used for a generic comparision helper. The idea is that I'd like to
be able to write expressions like these:

```
    {{#iff name '==' 'Foo'}}
```

and like this:

```
    {{#iff answer '>' 40}}
```

In the sample I've created two templates. In the first template I used there are 3 such conditionals.
In the second template there is a single conditional:
```
{{#iff 4 '*' 5}}
```
that I included just to
show what will happen if we supply an operator that is not supported by the `iff` helper. I also added two buttons,
one to process and show the first template and one to process and show the second template.

{% include file="examples/js/handlebars_conditionals.html" %}

[view](examples/js/handlebars_conditionals.html)

The JavaScript file has the data, the code reacting to clicks and processing the templates and the the partial(!)
implementation of the `iff` helper. Basically it is just a giant `switch` statement with a separate
`case` for each valid operator. The `default` behavior, when the given operator is not handled
by any of the `case` statements, is to `throw` an exception.

{% include file="examples/js/handlebars_conditionals.js" %}


## #compare

After reaching this point I found out that there is already an implementation of such a helper called `#compare`.
It can be found among the [comparison helpers](http://assemble.io/helpers/helpers-comparison.html).

In any case I think it was interesting to see how to build and use this.

## Comments

Handlebars is pretty useless, how difficult can it be to include support for expressions? That you have to declare so much code for this kind of basic behaviour...

<hr>

Thank you so much for this! Spent ages looking online for an example of 'if_eq' and yours is the first one that clicked for me.

<hr>

Thank you for the Uncaught Error section, saved me several hours :)

<hr>

Thanks for this great post! But for the first example, where true is expected false is returned. please verify and correct it. I ma facing the same issue in my project.


