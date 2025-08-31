---
title: "urllib vs urllib2 in Python - fetch the content of 404 or raise exception?"
timestamp: 2015-07-06T15:30:01
tags:
  - urllib
  - urllib2
published: true
books:
  - python
author: szabgab
archive: true
---


A small snippet of code using [urllib](https://docs.python.org/2/library/urllib.html) and
[urllib2](https://docs.python.org/2/library/urllib2.html) of Python to fetch a page.

The difference I've just encountered is that urllib will return the content of a page even
if the page is not found (404) while urllib2 will throw an exception.


## urllib

{% include file="examples/python/try_urllib.py" %}

Running `python try_urllib.py https://www.python.org/xyz` will print a big HTML page
because [https://www.python.org/xyz](https://www.python.org/xyz) is a big HTML page.

## urllib2

{% include file="examples/python/try_urllib2.py" %}

Running `python try_urllib2.py https://www.python.org/xyz` will print

```
HTTP Error 404: OK
```
