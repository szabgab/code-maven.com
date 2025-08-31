---
title: "How to commafy a number? (How to print number with commas as thousands separators using Python?)"
timestamp: 2016-08-16T14:55:01
tags:
  - format
published: true
books:
  - python
author: szabgab
archive: true
---



{% include file="examples/python/commafy.py" %}

We have imported the `print_function` from the
[__future__](https://docs.python.org/2/library/__future__.html)
so this code will work on both Python 2 and Python 3.

The key here is the `{:,}` placeholder.

## Commafy in Jinja and Flask

We can create new filters for Jinja and add them to the environment:

{% include file="examples/python/jinja-commafy/generate_from_filesystem.py" %}

In the template we can filter values using this new filter:

{% include file="examples/python/jinja-commafy/page.html" %}

The output will look like this:

```
12345678

12,345,678
```
