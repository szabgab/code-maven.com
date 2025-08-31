---
title: "JavaScript function that accepts any number of arguments"
timestamp: 2015-06-08T13:30:01
tags:
  - arguments
  - function
  - NaN
  - undefined
published: true
books:
  - nodejs
  - javascript
author: szabgab
archive: true
---


How can you create a function in JavaScript that will accept an unknown number of arguments? For example like a `sum` function to `add` numbers?

For the solution look at the end of the article.


## Add 2 numbers

Let's start by creating a function called `add` that can accept 2 arguments and that returns their sum.

{% include file="examples/js/add_2_numbers.js" %}

We can use Node.js to run the code `node add_2_numbers.js` and the result will the the numbers seen next to each row.

As you can observe, the first two calls gave the correct result. The third one, where we passed 3 numbers return 2,
which might be surprising to someone who does not know the implementation of the `add` function,  but which is correct.
The bigger issue is that it did not issue any warning or error complaining about the unused third parameter.


## Add 3 numbers

We can try to create another `add` function that will accept 3 parameters and will return the sum of all 3.
The results are next to the lines:

{% include file="examples/js/add_3_numbers.js" %}

JavaScript does not allow us to define the same function more than once with different signatures. It just silently
overrides the previous function with the new function of the same name. So we would get the same results even
if we remove the declaration with the 2 parameters.

What happens here is that in the first two cases, because we only passed 2 arguments, the third argument is `undefined`
and when we add two numbers and `undefined` our result is `NaN` - <b>not a number</b>.

The third case, when we pass 3 arguments works as expected.

Clearly this is not the solution.

## arguments, the object holding the passed arguments

The correct solution is to define a function with empty signature, as if it did not accept
any parameters, and then to look at the `arguments` object that holds all the parameters.

We can iterate over the element using a `for` loop and add them all to an internal variable.

As you can see from the results this works even if the user did not pass any argument.

{% include file="examples/js/sum_numbers.js" %}

For further details check out the
[documentation of arguments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#Using_the_arguments_object).
