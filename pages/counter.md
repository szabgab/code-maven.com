---
title: "Counter Examples"
timestamp: 2019-03-30T21:40:01
tags:
  - counter
  - ++
published: true
books:
  - counter
author: szabgab
show_related: false
---


I love experimenting with programming languages, databases, frameworks, etc.

The standard example of a "Hello World" program is nice to get started, but usually way too simple. So I started to create a slightly more complex example. A counter example.

In each example we are going to create a counter. A simple counter will just increment a single number. A multi-counter will handle several counters. e.g. one per client, one per user, or one per  some arbitrary string.

<b>I think these counter example can show you several aspects of a programming environment and can help you get started writing your own applications.</b>


In this project we are going to implement a counter with various front-ends and back-ends. Sometimes these two parts will be in one program.
Some of the solution will be web based. Some will be command line based. Some might be GUI-based.

The counters might be stored in some kind of a "database". It can be a plain text file, some data serialization format, a relational database, a NoSQL database and who knows what else.

The simpler version of the counter handles a single counter. Every time we run the counter it will show a number one higher than the previous one.

An interaction with a command-line tool might look like this:

```
$ count
  1
$ count
  2
$ count
  3
```

The multi-counter is slightly more complex. It will be able to maintain several counters at once.
So an interaction with a command-line tool might look like this:

```
$ count foo
  foo: 1
$ count foo
  foo: 2
$ count bar
  bar: 1
$ count foo
  foo: 3
```

This is going to be a long project, but it might help understand various techniques for data serialization.

## JavaScript
* [Plain Vanilla JavaScript](/vanilla-javascript-counter)
* [Improved Vanilla JavaScript](/improved-vanilla-javascript-counter)
* [On-load counter with plain Vanilla JavaScript and local storage](/on-load-counter-with-javascript-and-local-storage)
* [Multiple counters with plain Vanialla JavaScript and local storage](/multiple-counters-with-plain-javascript-and-local-storage)

## Python
* [Command-line counter in Python](/comman-line-counter-in-python) for a single counter.
* [Python and MongoDB](/python-counter-with-mongodb)
* [Flask counter with SQLite, SQLAlchemy, pytest](/flask-counter-sqlite-sqlalchemy)

## Go
* [Single counter with simple text file using Go](/counter-using-go)

## Perl
* A [command-line counter script in Perl](https://perlmaven.com/command-line-counter) that uses a plain file called `counter.txt` for a single counter.
* [Multiple command line counters with plain TSV text file back-end in Perl.](https://perlmaven.com/multiple-command-line-counters)
* [A command line counter with database back-end using Perl DBIx::Class](https://perlmaven.com/counter-with-database-backend-using-dbix-class)
* [Command line counter with JSON backend in Perl.](https://perlmaven.com/command-line-counter-with-json-backend)
* [Counter with Perl Dancer session](https://perlmaven.com/counter-with-dancer-sessions)
* [Command line counter in Perl with MongoDB as storage](https://perlmaven.com/command-line-counter-with-mongodb)
* [Counter with Perl Mojolicious Lite](https://perlmaven.com/pro/counter-with-mojolicious-lite)
* [Command line counter with Memcached using Perl](https://perlmaven.com/command-line-counter-with-memchached)
* [Increasing numbers in a text file using Perl](https://perlmaven.com/increase-numbers-in-a-file)
* [Counter example in Perl using YAML file to store the data](https://perlmaven.com/cli-counter-with-yaml-backend)
* [A counter using Perl Dancer and an in-memory SQLite database](https://perlmaven.com/counter-with-dancer-using-in-memory-sqlite-database)
* [A counter using Perl Dancer and Redis, both in a Docker container](https://perlmaven.com/counter-dancer2-redis-docker)

## R
* [Simple file-based counter in R](/simple-counter-with-r)

## Rust
* [Command line counter with plain text file storage in Rust](https://rust.code-maven.com/cli-counter-with-plain-text-file)
* [Command line multi-counter with JSON file storage in Rust](https://rust.code-maven.com/multi-counter-in-json-file)
* [Rocket web framework - Single counter in a plain text file](https://rust.code-maven.com/rocket-single-counter-in-text-file)
* [Rocket web framework - Multi-counter using cookies](https://rust.code-maven.com/rocket-multi-counter-using-cookies)
* [Rocket web framework - Multi counter using encrypted cookies](https://rust.code-maven.com/rocket-multi-counter-using-encrypted-cookies)
* [Multi-counter with embedded SurrealDB database using Rust](https://rust.code-maven.com/surrealdb-cli-multi-counter)
* <a href=""></a>

## Angular JS
* [Simple In-memory counter using AngularJS](/simple-in-memory-counter-with-angularjs)
* [Automatic counter using AngularJS](/automatic-counter-using-angularjs)
* [Several counters in MongoDB client](/counter-in-mongodb-client)


<!--
## Front-end

* command line
* web based:
        <ul>
* plain CGI
* CGI with Ajax
* plain PSGI
* PSGI with Ajax
* Dancer
* Mojolicious
        </ul>
    

## Back-end

* several counters each one in its own file
* several counters in a .txt file in CSV format
* several counters in a yaml/json file
* 1 counter in SQLite
* several counters in SQLite
* 1 counter in MySQL
* several counters in MySQL
*   ? PostgreSQL
* 1 counter in MongoDB
* several counters in MongoDB
-->
