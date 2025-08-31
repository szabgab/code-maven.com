---
title: "List Comprehension vs Generator Expressions in Python"
timestamp: 2015-06-26T09:00:01
tags:
  - ()
  - []
published: true
books:
  - python
author: szabgab
archive: true
---


A Generator Expression is doing basically the same thing as a List Comprehension
does, but the GE does it lazily. The difference is quite similar to the
difference between [range and xrange](/range-vs-xrange-in-python).

A List Comprehension, just like the plain `range` function, executes
immediately and returns a list.

A Generator Expression, just like `xrange` returns an object that
can be iterated over.


The comparision is not perfect though, because in an object returned by
the generator expression, we cannot access an element by index.

The difference between the two kinds of expressions is that the
List comprehension is enclosed in square brackets `[]`
while the Generator expression is enclosed in plain parentheses `()`.

```python
l = [n*2 for n in range(1000)] # List comprehension
g = (n*2 for n in range(1000))  # Generator expression
```

## Type

The types of the resulting values are `list` and `generator` respectively:

```python
print(type(l))  # 'list'
print(type(g))  # 'generator'
```

## Size in memory

The size of the objects is 9032 bytes (the list), and 80 bytes (the generator):

```python
print(sys.getsizeof(l))  # 9032
print(sys.getsizeof(g))  # 80
```

## Access by Index

We can access the elements of the `list`, but if we try to access the elements
of the `generator` we get a `TypeError`:

```python
print(l[4])   # 8
print(g[4])   # TypeError: 'generator' object has no attribute '__getitem__'
```

## Loop over

Finally, but most importantly, we can iterate over either of them:

```python
for v in l:
    pass
for v in g:
    pass
```

## The full example

{% include file="examples/python/generator_expression.py" %}

## Comments

Scenerio.From a large data collection 'else where 'you have to collect certain items and store at your end subject to complex conditions you impose. On-the-go nature of expression will help you save 'temporary storage' at your end compared to list comprehension which will make a list. Of course list comprehension can use if clause to 'filter' but your requirement may be too complex to code in relational and logical operations.

<hr>

The idea is expression helps on-the-go decision making. For example getting an item from one source and deciding to keep it or not for you then and there will be huge memory saving,

<hr>

Thanks. So it takes more memory to iterate over a list comprehension. Which one is faster to iterate over, all things being equal?

---

You never got a reply to your question but it's a good one.

My guess is that their speed for small data sets is identical or close to it. Start forcing OS swapping with huge lists and that goes out the window (obviously).

Python generators remind me of Unix pipes.


