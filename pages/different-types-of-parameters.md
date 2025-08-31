---
title: "Handle different types of parameters in the same function in Python"
timestamp: 2022-08-22T07:30:01
tags:
  - mypy
  - isinstance
  - typing
  - List
  - Union
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


Sometimes you have to deal with some data structure that can have either a single (string) value in it or a list.

I have encountered this when writing a dictionary. Most words had a single translation so mapping a word to string made sense,
but some words had multiple translations in which case we used a list of strings to represent them.

Then we had to write a function to handle a value that can be either a string or a list.

We ended up with the following solution:


{% include file="examples/python/mypy/different_types_for_parameters.py" %}

If we run this program it will print

```
['hello']
['hi', 'there']
```

and then raise an exception when a number is passed to.

It works properly, but this looks like a bad idea of code.
I've encountered plenty such functions in various applications and it always felt incorrect.

A better solution would be to create two separate functions. One to handle a single string and one
to handle a list. Before looking at that solution, however, let's see how could we use <b>mypy</b>
to recognize code that will call this function incorrectly with a number?

Let's annotate this function with the proper types!

{% include file="examples/python/mypy/different_types_for_parameters_mypy.py" %}

We use `Union[str, List[str]]` to define that the parameter of the function is
either a string or a list of strings. We can also use `List[str]` to define
that the return value of the function is a list of strings.

If we run [mypy](/mypy) on this file we get an error:

```
$ mypy different_types_for_parameters_mypy.py

different_types_for_parameters_mypy.py:13: error: Argument 1 to "handle_something" has incompatible type "int"; expected "Union[str, List[str]]"
Found 1 error in 1 file (checked 1 source file)
```

This way we can find issues with our code before even running it and without writing lots of tests.


## Using two separate functions

Probably a better approach is to write two functions, one that can handle the list
and the other that can handle the single value (eg. by converting it to a list and
then calling the function that handles the list)

{% include file="examples/python/mypy/different_types_for_parameters_separate.py" %}

This, of course, would require the callers of the function to know what type of data do they have,
but I think in most cases it is better then to magically handle both single values and lists.

