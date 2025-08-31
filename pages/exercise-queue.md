---
title: "Exercise: Queue"
timestamp: 2018-04-21T12:30:01
tags:
  - CodeMaven
published: true
books:
  - exercise
author: szabgab
archive: true
---


The application should manage a queue of people.


* It will prompt the user for a new name by printing `:`.
* The user can type in a name and press ENTER.
* The app will add the name to the queue.
* If the user types in "n" then the application will print the first name in the queue.

A sample interaction will look like this:

```
: Foo
: Bar
: Moo
: n
  next is Foo
: n
  next is Bar
: Peter
: n
  next is Moo
: n
  next is Peter
: n
  the queue is empty
```


