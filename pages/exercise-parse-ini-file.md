---
title: "Exercise: parse INI file"
timestamp: 2015-10-31T16:34:40
tags:
  - regexes
types:
  - screencast
published: true
books:
  - beginner_video
author: szabgab
---


Exercise: parse-ini-file


<slidecast file="beginner-perl/exercise-parse-ini-file" youtube="InGai4vtEhc" />


An INI or Config file looks like this:

{% include file="examples/data/inifile.ini" %}

It has sections that start with a section name in square brackets and inside section it has key-value pairs separated by an equal sign surrounded
by 0 or more spaces. Empty rows are disregarded. Any line starting with a `#` is considered a comment and is also disregarded.
In some extended cases we can have key-value pairs before any section was declared and they will belong to an implicit seciton called `_`.
In other extended cases multi-line values are also allowed.

For our purpuse we can go with simple ini files.

The task is to create a script that can parse such input file and create a hash-of-hashes (dictionary of dictionaries in Python)
where the primary key is the section name, the secondary key is the 'key' and the value is the value in each line.

The Perl dump of the above INI file would look like this:

```
$VAR1 = {
          'earth' => {
                       'base' => 'London',
                       'ship' => 'x-wing'
                     },
          'alpha' => {
                       'base' => 'moon',
                       'ship' => 'alpha 3'
                     }
        };
```

## Tools

* 

## Solutions

* 

