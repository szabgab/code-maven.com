---
title: "Exercise: Implement the wc command of Linux/Unix (word count)"
timestamp: 2015-11-05T06:31:25
tags:
  - exercises
  - projects
published: true
books:
  - ruby
  - python
  - javascript
  - php
author: szabgab
---


Exercise: Implement the `wc` command of Linux/Unix

See other [exercises](/exercises).


A sample execution of `wc` looks like this:

```
$ wc *
      11      34     249 README.pod
       2       4     128 authors.txt
      37     110     773 check_examples.pl
wc: examples: read: Is a directory
    2737    2738   27627 python_weekly.pickle
wc: sites: read: Is a directory
       9      15     149 sites.yml
wc: static: read: Is a directory
    2796    2901   28926 total
```

That is. Given a list of things on the command line it counts the number of "lines", "words", and "characters" for each file
printing them in 3 columns (in that order) followed by the name of the file.

At the end it will print the totals of each column.

If it encounters something that is not a file (e.g. a directory) it prints a warning and goes on.

In our case there were 3 directories 'examples', 'sites', and 'static'.

Optionally allow the user to supply any of the 3 flags: `-l` to print the line count, `-w` to print the word count, or `-c` to print the charater count.
By default it prints all 3.

If no input file is provided, `wc` will work on the content arriving on the Standard Input. This means we can write this:

```
$ find . | wc -l
```

and get back the number of file in the directory tree starting in our current working directory.

## Suggestion

[Count words in a file](/exercise-count-words-in-a-file) is a simpler exercise. Solve that first!

## Tools - Perl 5

* [Perl 5: Open file and read content](https://perlmaven.com/open-and-read-from-files)
* [Perl 5: @ARGV](https://perlmaven.com/argv-in-perl)
* [Perl 5: warn](https://perlmaven.com/warn)
* Printing to STDERR
* Create functions
* Check file type (file, directory, etc)

## Tools - Ruby

* [Ruby: Open file and read content in Ruby](/open-file-and-read-content-in-ruby)
* [Ruby: ARGV command line parameters](/argv-the-command-line-arguments-in-ruby)
* Printing to Standard Error

## Solutions

* [Python](/python-wc)

