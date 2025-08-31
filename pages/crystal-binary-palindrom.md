---
title: "Binary Palindrom - Crystal"
timestamp: 2021-06-26T12:30:01
tags:
  - Crystal
published: true
books:
  - crystal
author: szabgab
archive: true
show_related: true
---


A Binary Palindrom is a positive integer for which the binary representation is a palindrom.
See the [Weekly challange](https://theweeklychallenge.org/blog/perl-weekly-challenge-118/).

This is a solution in the [Crystal programming language](/crystal).


## Directory layout

```
.
├── spec
│   └── palindrome_spec.cr
└── src
    ├── palindrome.cr
    └── use_palindrome.cr
```

## Implementation

{% include file="examples/crystal/binary_palindrome/src/palindrome.cr" %}

In Crystal you can have <b>?</b> as the last character of a function name.
It is often used for functions that return a boolean value.

The original requets was for returning 1 and 0, but most likely it was defined that way
because Perl does not have a special boolean type. In the Crystal solution I opted to return <b>true</b> or <b>false</b>
respectively as that's the right way to do it in Crystal.

Functions in Crystal return the value of the last statement so the <b>return</b> keyword is optional, but I prefer to have it explicitely.

Extra: If the function is called with a negative value an ArgumentError exception is raised.

## Usage

A simple Crystal program that will accept one or more numbers on the command line and will print Yes or No for
each number:

```
$ crystal src/use_palindrome.cr 3 4 5
3 Yes
4 No
5 Yes
```

{% include file="examples/crystal/binary_palindrome/src/use_palindrome.cr" %}

* <b>ARGV</b> is an array of string containing the values from the command line
* <b>#{}</b> is interpolation of variables and expressions inside a string
* A string can be delimitered using double-quotes <b>"</b> or this construct: <b>%[]</b> where you can use any type of brackets.
* <b>ARGV.each</b> iterates over the elements of <b>ARGV</b> and on each iteration the current value is assigned to the "number" variable.
* <b>to_i</b> converts a string to an integer.
* <b>?:</b> is just the conditional operator (aka. the ternary operator)


## Spec tests

I also included a test script.

{% include file="examples/crystal/binary_palindrome/spec/palindrome_spec.cr" %}

In order to run the tests [install Crystal](https://crystal-lang.org/),
re-created the directory layout with the two files.
(You can clone [the repository](https://github.com/szabgab/code-maven.com/) and cd to <b>examples/crystal/binary_palindrome/</b>)
Then  run

```
crystal spec
```


