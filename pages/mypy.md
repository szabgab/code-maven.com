---
title: "Type checking of Python code using mypy"
timestamp: 2020-05-28T17:30:01
tags:
  - mypy
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


Python cares a lot less about types than languages such as C, Java, or Go.

Unlike in those strongly typed languages, in Python a variable can be assigned a number and then replaced by a string.
You can pass any type of value to a function parameter and Python will only complain if later, in the body of the function,
that type turns out to be incompatible with an operation.

Recent versions of Python have started to allow you to declare the types of variables and function parameters, but Python itself
does not (yet) do anything with these types.

However, the [mypy](http://mypy-lang.org/) project offers you a tool that will statically check your code and verify that the types are correct.


<b>mypy</b> provides optional type-checking for python code. See the [docs of mypy](https://mypy.readthedocs.io/).

After installing it with <b>pip install mypy</b> you should be able to run

```
mypy  some_file.py
```

or maybe

```
mypy --ignore-missing-imports some_directory/
```

to avoid certain warnings.

<b>mypy</b> will already find an warn about some issues even without you doint any extra work.

## mypy success

Before showing all the problems mypy can find let's spend a few seconds to see what happens if our code does not have any issues:

{% include file="examples/python/mypy/hw.py" %}

```
$ mypy hw.py
Success: no issues found in 1 source file
```

## mypy without annotation

{% include file="examples/python/mypy/a.py" %}

This code does not have any annotation yet, but we put different values in the same variable and <b>mypy</b> will report it.

```
$ mypy a.py
a.py:2: error: Incompatible types in assignment (expression has type "str", variable has type "int")
Found 1 error in 1 file (checked 1 source file)
```

A more interesting case might be this one:

{% include file="examples/python/mypy/aa.py" %}

We expect the user to type in an integer and we convert it to an integer.
We need to convert it, because <b>input</b> always return a string.
So in this rather common code we can see how <b>mypy</b> suggest that we write stricter code.

```
$ mypy aa.py
aa.py:2: error: Incompatible types in assignment (expression has type "int", variable has type "str")
Found 1 error in 1 file (checked 1 source file)
```

One of the solutions is to use two separate variable names:

{% include file="examples/python/mypy/aaa.py" %}

```
$ mypy aaa.py
Success: no issues found in 1 source file
```

## mypy and functions without annotation

If we have similar isse but inside a function like here:

{% include file="examples/python/mypy/b.py" %}

mypy will disregard this. By default <b>mypy</b> does not look inside functions.

```
$ mypy b.py
Success: no issues found in 1 source file
```


I have not found a way to tell <b>mypy</b> to look into those functions without changing my code.
If we add the smallest annotation to a function, <b>mypy</b> will start checking the whole function.

So here I declared that the function returns <b>None</b>.

{% include file="examples/python/mypy/c.py" %}

```
$ mypy c.py
c.py:4: error: Incompatible types in assignment (expression has type "str", variable has type "int")
Found 1 error in 1 file (checked 1 source file)
```

## mypy catching a bug

Let's see an example, still a simplified one, in which <b>mypy</b> will help us discover a bug.
If course writing extensive unittest would uncover such bugs, but if the code is complex
(unlike this example) then it is quite likely you won't be able to cover all the cases.

Moreover this shows that even if you don't have time to add unittest, adding simple annotation to your code
and using mypy will already allow you to find problems.

{% include file="examples/python/mypy/reg.py" %}

As long as there Is a match the above code works, but if there is no match this python code raises an exception.

Using mypy we can find out about this problem as mypy gives the following error:

```
$ mypy reg.py
reg.py:7: error: Item "None" of "Optional[Match[str]]" has no attribute "group"
Found 1 error in 1 file (checked 1 source file)
```


## Conclusion

These example can already show you the usefulness of mypy. In upcoming articles we'll see more use-cases.

