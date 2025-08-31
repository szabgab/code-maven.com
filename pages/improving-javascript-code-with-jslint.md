---
title: "Improving JavaScript code with JSLint"
timestamp: 2015-06-17T07:30:01
tags:
  - JSLint
  - use strict
published: true
books:
  - javascript
  - cm
author: szabgab
archive: true
---


In the [previous article](/javascript-function-that-accepts-any-number-of-arguments) we had a few small JavaScript files. I was wondering how well
were they written so I've installed [JSLint](http://www.jslint.com/) using `npm install -g jslint`
and then I ran it on the files:


## spaces around operators

```
$ jslint add_2_numbers.js 

add_2_numbers.js
 #1 Missing 'use strict' statement.
    return x+y; // Line 2, Pos 5
 #2 Missing space between 'x' and '+'.
    return x+y; // Line 2, Pos 13
 #3 Missing space between '+' and 'y'.
    return x+y; // Line 2, Pos 14
```

JSLint found 3 issues with this code. Issues #2 and #3 are fairly trivial. Instead of writing 
`x+y` it is better to leave some spaces around operators and write `x + y`.

## use strict

The first one, on the other hand is slightly more involved. Just as in [Perl](https://perlmaven.com/),
JavaScript also allows a lot of bad practices, and just as with Perl, the developers of JavaScript cannot just
eliminate the features that allow these bad practices. Such move would break tons of code that worked earlier.

So in ECMAScript 5 a new feature was added. You can include a string `"use strict";` at the beginning of a
file or the beginning of a function and that will turn on the strict mode for the whole file or
for that specific function, respectively. Because the construct is a string literal and because JavaScript has the
strange behavior of disregarding string literals floating around the code, this snippet will be disregarded in
any browser that does not support it. Which is not that interesting any more as by today virtually
every browser on the market supports it.

[John Reisig](http://ejohn.org/), the author of [jQuery](http://jquery.com/),
and former [Perl developer](https://metacpan.org/author/JERESIG)
has an article on [ECMAScript 5 strict mode](http://ejohn.org/blog/ecmascript-5-strict-mode-json-and-more/).

So we add `"use strict";` to the top of our script.

The resulting script 

{% include file="examples/js/add_2_numbers_fixed.js" %}

works as the original one: `node add_2_numbers_fixed.js`
and it is JSLint error free: `jslint add_2_numbers_fixed.js`


## Redefining function is not captured

Once I was done with the `add_2_numbers.js` script I moved on to check `add_3_numbers.js`.
The error were similar, we just had more of them. I added `"use strict";` and added spaces around
the operators. This eliminated all the JSLint complaint, but it left my baffled a bit.
Neither `JSLint`, nor `"use strict";` complained about the multiple definition of the
`add` function while clearly it is a problem in the code.

I guess this means redefining functions is a common and even recommended practice in JavaScript.

I'll get back to you when I digest this idea.

## Move 'var' declarations to the top of the function.

{% include file="examples/js/sum_numbers.js" %}

Once I was done with that script I ran `jslint sum_numbers.js` It gave me the following report:

```
 #1 Missing 'use strict' statement.
    var s = 0; // Line 2, Pos 5
 #2 Move 'var' declarations to the top of the function.
    for (var i=0; i < arguments.length; i++) { // Line 3, Pos 10
 #3 Stopping. (21% scanned).
     // Line 3, Pos 10
```

We are already familiar with the first one, but the second one took me by surprise.

A little thinking and research later I found out, that unlike in Perl the `for`
loop does not create a separate context and thus the variable declared in the `for`
loop is scoped to the global environment, or to the function if the loop is in a function.

So this code might give the impression, especially to Perl developers, that `i`
is only defined in the loop.

```javascript
    for (var i=0; i < arguments.length; i++) {
        s += arguments[i];
    }
```

## Scope of JavaScript variable in a loop

In reality, even if we declare the variable `i` inside the `for`-loop
it is still available after the loop has ended.

{% include file="examples/js/scope_of_variable_in_loop.js" %}

So it is better to declare all the variables at the top of the function, or if they are global then
at the top of the file. (But you should not use global.)

I fixed that, added `"use strict";` to the top and an the script again on this version:

{% include file="examples/js/sum_numbers_step1.js" %}

The result was this:

```
 #1 Combine this with the previous 'var' statement.
    var i = 0; // Line 4, Pos 9
 #2 Missing space between 'i' and '='.
    for (i=0; i < arguments.length; i++) { // Line 5, Pos 11
 #3 Missing space between '=' and '0'.
    for (i=0; i < arguments.length; i++) { // Line 5, Pos 12
 #4 Unexpected '++'.
    for (i=0; i < arguments.length; i++) { // Line 5, Pos 38
```

#2 and #3 are the usual complaints about lack of spaces around operators. It is funny, because when I write Perl
I always put spaces around operators. I am not sure why have I started to avoid them in JavaScript.
I guess I learned JavaScript that way. It's time to unlearn that.

So let's see the first one:

## Combine this with the previous 'var' statement.

There is an excellent site explaining the [JSLint errors](https://jslinterrors.com/). For example 
this error:
[Combine this with the previous 'var' statement](https://jslinterrors.com/combine-this-with-the-previous-var-statement).

It wants me to write 

```javascript
    var s = 0,
        i;
```

instead of

```javascript
    var s = 0;
    var i;
```

## Unexpected '++'

The remaining error is about [Unexpected '++'](https://jslinterrors.com/unexpected-plus-plus).
I know that Python does not have `++`, and I've just listened to a presentation by
[Douglas Crockford](http://crockford.com/), author of JSLint explaining why he does not use `++`,
but I wonder if it needs to be banned from this situation as well? A `for` loop is a fairly simple and standard
expression.

There is a way to tell JSLint to not complain about `++`, but I think in many other cases it might be justified
to avoid it. So I'd like to turn it off on this specific line of code. Because I could not find how to that,
I went with the slightly cumbersome solution and replaced `i++` by `i += 1`.

This brought me to this result:

{% include file="examples/js/sum_numbers_fixed.js" %}

