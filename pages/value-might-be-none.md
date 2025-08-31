---
title: "Value might be None in Python - checking with mypy"
timestamp: 2022-08-24T09:30:01
tags:
  - mypy
  - Union
  - Optional
  - None
  - float
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


There are many cases in which a variable can be empty, or more correctly can contain the value `None` in Python.

The same with the return value of a function. We might have a function that would normally return a floating point number,
but sometimes it might return None. How can you give type-checking hints so [mypy](/mypy) will accept the situation?

In another article we already saw how to handle the case when a [function parameter can have more than one type.](/different-types-of-parameters)
Now we'll see a special case of that, when one of the potential values is `None`.

In other words, when the value is <b>optional</b>.


## Function that returns either float or None

In this example we have function (admittedly a bit contrived example, but syntactically correct).
We add type-hinting that suggests the function is expected to always return a <b>float</b>.

{% include file="examples/python/mypy/return_might_be_none.py" %}

Obviously it does not, so when we run <b>mypy</b> it will complain:

```
$ mypy return_might_be_none.py

return_might_be_none.py:7: error: Incompatible return value type (got "None", expected "float")
```


## Using Union

Using the `Union` keyword from the `typing` module allows us to declare that a variable,
or in this case the return value of the function can be either one of 2 or more values.
In our case it is either `float` or `None`

{% include file="examples/python/mypy/return_might_be_none_union.py" %}

Running <b>mypy</b> on it will be without complaints.


## Using Optional

While Union can be used, an even better option for this case is to use the `Optional` keyword:

{% include file="examples/python/mypy/return_might_be_none_optional.py" %}

