---
title: "Testing SQLite"
timestamp: 2017-08-17T07:30:01
tags:
  - SQLite
  - testing
  - Fossil
published: false
books:
  - qa
author: szabgab
archive: true
---


This is part of a series of articles I started with [Quality Assurance and Automated Testing in Open Source Projects](/quality-assurance-and-automated-testing-in-open-source-projects).

According to its site [SQLite](http://www.sqlite.org/) is a small C library 
that implements a self-contained, high-reliability, embeddable, full-featured, zero-configuration SQL database engine.

It is also probably [Most Widely Deployed Software Module of Any Type](http://sqlite.org/mostdeployed.html).

I usually call it an in-process database. I am using it in many applications.


## Development

SQLite has been developed by D. Richard Hipp and was placed in the [public domain](http://www.sqlite.org/copyright.html).
So actually it is not Open Source according to the definition of
[OSI](http://www.opensource.org/), but we can look at it so it is interesting to us.
In order to ensure the legality of all the code, the developers of SQLite require any other contributor to relase their contribution to the public domain.

Currently most of the development is done by Richard Hipp, Dan Kennedy, and Joe Mistachkin with a few more occasional contributors. There is a page dedicated to the [SQLite crew](http://www.sqlite.org/crew.html).

They are using [Fossil](http://www.fossil-scm.org/index.html/doc/trunk/www/index.wiki) as their version control system. (It is an open source distributed VCS similar to Git and Mercurial 

[SQLite source code repo](https://www.sqlite.org/src/doc/trunk/README.md)

Source code is available either as a released zip file or via the read only interface of the version control ststem. See the [download](http://sqlite.org/download.html) page for both.


Building SQLite from CVS does not seem to be simple
but there is a description of the
[SQLite build process](http://www.sqlite.org/cvstrac/wiki?p=SqliteBuildProcess)
on the site.<br />

On the other hand the released versions are easy to build. For example
the Perl driver of SQLite [DBD::SQLite](https://metacpan.org/pod/DBD::SQLite) contains the source code of SQLite and you can download and install it with a single command.
Python does not even need that as the standard release of CPython comes with a built-in copy of SQLite and the Python driver to access it.

## Testing

The page about [the Architecture Of SQLite](http://www.sqlite.org/arch.html)
mentions testing as well, albeit quite shortly. (See the bottom of that page)

The point is that 50-60% of the code base are tests and quality related. 
Given that the application is written in C and most of the tests are 
written in Tcl we can assume a good number of tests.
Based on what Richard wrote me we can describe the test as follows:

There are two levels of testing in the default SQLite package.
You can type:

<b>make test</b>

And this runs a quick set of tests that provides good code coverage
of most features.  However, many of the tedious and time-consuming
tests, such as tests for recovery from malloc() errors, are omitted.
You can also do

<b>make fulltest</b>

This latter does a much longer series of tests that provides 98%
code coverage.  The remaining 2% is mostly unreachable defensive
code.

We also have some unpublished scripts that compile SQLite under
various configurations (enabling or disabling compile-time options)
and run extra-long versions of full-test. These are our "soak-test"
scripts. These soak-tests are unpublished as they contain 
configurations used by support customers who do not want their 
configurations published.

Richard wrote:

"The last time I measured, around 60% of 
the SQLite source tree was devoted to testing.  
There are over 6000 individual test
cases.  Many of those test cases are parameterized and run
in loops with varying parameters, so that a fulltest runs over
250K separate tests, depending on compile-time options.

For every bug reported against the SQLite core, we always generate
new test cases to exhibit the bug in order to avoid regressions.

In builds of SQLite that are designed for testing, we have hooks
in the OS interface that allow us to simulate malloc() failures,
disk I/O errors, and other real-world anomalies so that we can
verify that SQLite responds correctly.  We can even simulate the
effects of a power loss in the middle of a transaction in order
to verify that transactions rollback correctly after power is
restored.

Testing is done by building a executable named "testfixture"
that include a TCL interpreter and the version SQLite under
test.  We then run testfixture with an argument that is the
name of the test script we want to run.  Example:

    ./testfixture ../sqlite/test/select4.test

There are some special test scripts "quick.test" and "all.test"
that recursively run other test scripts in order to do our "test"
and "fulltest" make targets.

The high reliability of SQLite is largely a result of its 
extensive test suite.  And the test suite would not have 
been achievable without the TCL scripting language.  We
believe, therefore, that SQLite would have never been possible
without the TCL programming language."


## Automated Testing

There is no smoke testing setup, it is basically only what Richard 
himself does and he does it on Linux only. As he wrote me, most of 
the complexity is in the non-platform specific parts of the code, 
so problems in the platform interfaces are not common. 
Still if those arise the user community alerts him quite quickly.

Right now most of my work is done on Linux so I am not worried about this, 
also I believe most of the issues are found and fixed quickly on other
platforms as well, but still I would be glad to see some people running
the test suite and then sending the reports to a central database 
from other platforms as well. Similar to what we can see in some of the
other successful open source projects.

## Newsletter

If you are interested in hearing about new entries in this series, sign up to our
[newsletter](https://mail.szabgab.com/cgi-bin/mailman/listinfo/test-automation-tips) called
Test Automation Tips.


