---
title: "Project Management, Quality Assurance, and Test Automation in Open Source Projects"
timestamp: 2017-08-16T07:30:01
tags:
  - testing
  - automated testing
  - QA
  - open source
published: true
books:
  - qa
author: szabgab
archive: true
---


Some Open Source projects are almost exclusively developed inside a corporation which provides Project management, development, and QA just as the do for their proprietary products.

Others, actually most of the Open Source projects, don't have a dedicated project manager and QA team. They don't even have a paid team of developers. Just a few volunteers who spend their own time to work on the project they care about. 

Yet there are plenty of high-quality Open Source project that provide an enormous value to their users and to the world in general.

How does that work? How do Open Source projects ensure high quality?

In this article series we are going to look at some Open Source projects and see how they do this.


We are going to look at projects that are pure volunteer-based and projects that are (almost 100%) internal to a company. Project where the company releases the source code under an Open Source license, but there is effectively no developer community outside the company.

## The audience - are these articles for you?

You might be a software developer, team leader, QA engineer, QA manager, or CxO in a company with extensive technology who has been wondering: Can we trust Open Source projects?

You might be even wondering: Can we learn anything from the open source world and implement in our company to improve the quality of our proprietary software?

Finally, you might recognize the value you have already received from the Open Source world and you would like to <b>"give back"</b>. Learning about quality and value creation in Open Source projects is the first step towards contributing to one of the projects.


## Content
<p>
While the main focus of these articles is the testing phase it is often easier to understand how it works if we see the whole development process of the project.
Especially as in most of the cases testing is integrated in the development process of the applications and is done by the developers themselves.

These are some of the issues we are going to look at, but the list will change as we learn more about the practices of the various Open Source projects.

* Who are the developers? Are they employed by one or more companies to work on the project? Are they volunteers or paid? Who pays them?
* Who makes the decisions in the project? A core team? A project manager?

* Which Version Control System (VCS) are they using? Git? Subversion? Mercurial?
* Who has the right to commit to the version control system? (is there a rule-book for that?)


* Which bug-tracking system is used?

* What versions of the software are supported?
* In which language(s) is the product written?
* How to compile/build the product? (Link to the instructions is enough)

* Is there a test suite for automated tests?
* Where are the tests located? Same repository? Which directory?
* In which languages(s) are the tests written?
* How to run the tests?

* Are they running smoke test?
* Is there an CI (Continuous Integration) system?
* Do they have a test farm? Is it company owned or volunteer based as well?
* Where are the test reports?
* How easy is it to setup smoke testing?
* Do they have centralized management of the testing effort or is it distributed?
* What is the automated test coverage?

* Are there parts that need manual testing? (That would be very hard to test automatically.)
* Are there manual testers involved?

Diversity of test environment:
* OS-es: Linux , *BSD , OSX, Windows  (build farm by volunteers)
* Compiler (clang gcc, Visual Studio, mingws, etc)
* Database backends (MySQL, PostgreSQL, SQLite, Oracle, MS SQL Server, Sybase, etc.)

## Relevant material
* [Producing Open Source Software](http://producingoss.com/) by Karl Fogel is an excellent book about the subject.

## History

The first version of this article was written in 2007, exactly 10 years ago. Then it was followed by a number of articles discussing several open source projects. Since then a lot has changed in the Open Source developer world. We are going to revisit the projects covered in the old articles and discuss plenty of other projects as well.

## Articles by others
* [How SQLite Is Tested](http://sqlite.org/testing.html)
* [How Apache Kafka is Tested](https://www.confluent.io/blog/apache-kafka-tested/)
* [Testing curl](https://daniel.haxx.se/blog/2017/10/12/testing-curl/) by Daniel Stenberg. Author and maintainer.


## Old Articles
* [Quality Assurance of Perl 5](https://szabgab.com/quality-assurance-of-perl-5.html)
* [Smoked Parrot](https://szabgab.com/smoked-parrot.html)
* [Testing SQLite](https://szabgab.com/testing-sqlite.html)
* [Testing NUT, the Network UPS Tools](https://szabgab.com/testing-nut-the-network-ups-tools.html)
* [Testing GHC, the Glasgow Haskell Compiler](https://szabgab.com/testing-ghc-the-glasgow-haskell-compiler.html)
* [Testing Ruby](https://szabgab.com/testing-ruby.html)
* [Testing Pugs and Perl 6](https://szabgab.com/testing-pugs-and-perl-6.html)
* [Testing PostgresSQL](https://szabgab.com/testing-postgressql.html)

## Case Studies


## Newsletter

If you are interested in hearing about new entries in this series, sign up to our
[newsletter](https://mail.szabgab.com/cgi-bin/mailman/listinfo/test-automation-tips) called
Test Automation Tips.


