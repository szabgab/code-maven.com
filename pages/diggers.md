---
title: "Code Diggers"
timestamp: 2023-06-17T19:30:01
tags:
  - Diggers
published: true
author: szabgab
archive: true
show_related: true
---


Most of the popular programming languages have open source 3rd-party libraries with [library registries](/package-registry).
In the Digger projects we try to collect data about these project and show them in a way that help the users and the potential contributors.


## What are the goals?

Each 3rd-party registry provides some meta-data about the projects. e.g. information about the license of the project, the requirements of the projects,
a link the public VCS (Version Control System) of the project. However, many of the libraries don't supply this data. Not including a link to the VCS
makes it unnecessarily difficult to find it and to contribute to the project. Thus one of the first things we try to map is the list of libraries
that do NOT have that link. Then we encourage contributors to find the repos and send a pull-request to include the link.

For the projects where we have a link to the VCS we can also check if they have CI (Continuous Integration) configured.

We can show how important each package is by counting all the other packages that depend on it.

Where it is available we also display the test-coverage report of each project.

## Why separate projects?

Each Digger is written in the language of the libraries. Partially because I feel this as a good opportunity to learn the language
and partially because that will make it easier for people who write those 3rd-party libraries to contribute to the respective projects.
In addition each language has tools accessing the the registry and analyzing the code in their language. So writing in the "native" language
gives us access to those tools.


## Current projects

* [Python](https://pydigger.com/) - [source](https://github.com/szabgab/pydigger.com)
* [Perl](https://cpan-digger.perlmaven.com/) - [source](https://github.com/szabgab/CPAN-Digger/)
* [Ruby](https://ruby-digger.code-maven.com/) - [source](https://github.com/szabgab/ruby-digger)

## Planned projects

* PHP - [source](https://github.com/szabgab/php-digger)
* [Rust](https://rust-digger.code-maven.com/)
* JavaScript / NodeJS [source](https://github.com/szabgab/jsdigger)


