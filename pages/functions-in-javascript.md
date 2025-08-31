---
title: "Functions in JavaScript"
timestamp: 2015-02-12T13:30:01
tags:
  - function
published: true
books:
  - javascript
author: szabgab
archive: true
---


Just as in many other programming languages, in JavaScript too we can create functions.

In JavaScript we use the `function` keyword for this followed by the name of the new function.
Then the list of parameters in parentheses and then a block of expressions in curly braces. This is the body of the
function.


{% include file="examples/js/function.html" %}

[view](examples/js/function.html)

If you try this example, and [open the JavaScript console](/open-javascript-console) to see the output you'll see that the order of the output is

```
before
Hello World
after
```

So as you can see, unlike earlier, the code is not executed in the order it can be found in the file.
Although the function is declared before everything else, it is only executed later, when we call it using
its name `show();`

## Calling a function more than once

This was not yet very interesting, but in the next example you'll see we can call the same function multiple times.

{% include file="examples/js/function_calls.html" %}

[view](examples/js/function_calls.html)

This already shows one of the values of functions. They can help eliminate code repetition. Of course if the content
of the function was bigger then the gain was more obvious. We would still only add one line each time we
call the function, but all the content of the function would be executed.

```
Hello World
before
Hello World
after
Hello World
```

## Function with parameters

A much more interesting case is when we also provide parameters to the function.
In the next example, in the function declaration we wrote that we are going to accept a single value
and we want it to be assigned to the `name` variable. Then, we called the function and passed
a value to it. In every call we passed a different value.

Inside the function the `name` variable holds the current value.

This show the real power of functions.

We can have one piece of code, that can be tested on it own, separately from the rest of the code,
and then reused multiple times.

{% include file="examples/js/function_parameters.html" %}

[view](examples/js/function_parameters.html)

The output of these function

```
Hello  Foo
Hello  Bar
Hello  Zorg
```


