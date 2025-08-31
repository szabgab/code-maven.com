---
title: "Exercise: Implement Reverse Polish Calculator"
timestamp: 2018-04-21T12:45:01
tags:
  - CodeMaven
published: true
books:
  - exercise
author: szabgab
archive: true
---


Implement [Reverse Polish Calculator](https://en.wikipedia.org/wiki/Reverse_Polish_notation)


We are used to write calculations using the infix notation where the operator is between the two operands. e.g. <b>3 + 4 * 7</b>. In order to implement a calculator that knows how to calculate this
one needs to implement the order of operations.

In the Reverse Polish Notation the operator comes after the two operands. e.g. <b>3 4 +</b> instead of <b>3 + 4</b>.

In this notiation there are no preferences between operators.

The above expression can be written in RPN as:

```
3
4
7
*
+
=
```

The task is to implement RPN in your favorite language.

## Python

In order to make it easer for you I've prepared a module that implements the low-level calculations.

{% include file="examples/python/calc.py" %}


## Solutions
* [Python with list](https://code-maven.com/slides/python/solution-stack)
* [Python with deque](https://code-maven.com/slides/python/solution-stack-deque)
* [Perl](https://code-maven.com/slides/perl-programming/stack-implementation)

