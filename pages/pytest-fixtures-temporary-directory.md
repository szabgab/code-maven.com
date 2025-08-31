---
title: "Python: PyTest fixtures - temporary directory - tmpdir"
timestamp: 2019-04-09T10:30:01
tags:
  - pytest
  - tempdir
published: true
books:
  - python
author: szabgab
archive: true
---


When writing tests you often need to create files that are need by the test
(e.g. a configuration file, or the output of a command)
Creating in the current directory can problematic for several reasons.

For example if you have more than one test scripts and each use the same filename
then you cannot run the tests in parallel.


In the same way you cannot just designate a directory where you store these temporary files
as that would mean running the tests on the same computer isn't possible. Even in two separate
environments.

Fixtures, is a generic term in the testing world to create a known environment in which the test
can run. PyTest has a rich set of Fixures, one of the, called <b>tmpdir</b> makes it easy to create
a temporary diriectory for each test run.

In order to use this facility, the only thing you need to do is to declare your testing function
accepting the parameter <b>tmpdir</b>. (The exact name is important here as PyTest used introspection
to look at your testing function.

When it sees that you are expecting a <b>tmpdir</b> it will create a temporary directory and a
Python object represnting it and it will pass it to your testing function.

This is also called <a href="">dependency injection</a>.

You can then put whatever you like in that directory. You can be sure that it will only be used by
the current test process. (It is not a random directory name so other processes can easily find it,
but unless someone actively tries to break your test system, you'll be ok.)


{% include file="examples/python/test_json.py" %}

