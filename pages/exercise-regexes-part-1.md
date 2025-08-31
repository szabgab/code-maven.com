---
title: "Exercise: Regexes part 1"
timestamp: 2015-10-30T12:10:13
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


Regexes exercise 1


Pick up a file with some text in it. Write a script (one for each item) that prints
out every line from the file that matches the requirement.
You can use the script at the end of the page as a starting point but you will have to change it!

* has a 'q'
* starts with a 'q'
* has 'th'
* has an 'q' or a 'Q'
* has a '*' in it
* starts with an 'q' or an 'Q'
* has both 'a' and 'e' in it
* has an 'a' and somewhere later an 'e'
* does not have an 'a'
* does not have an 'a' nor 'e'
* has an 'a' but not 'e'
* has at least 2 consequtive vowels (a,e,i,o,u) like in the word "bear"
* has at least 3 vowels
* has at least 6 characters
* has at exactly 6 characters
* all the words with either 'Bar' or 'Baz' in them
* all the rows with either 'apple pie' or 'banana pie' in them
* for each row print if it was apple or banana pie?
* Bonus: Print if the same word appears twice in the same line
* Bonus: has a double character (e.g. 'oo')

## Ruby
{% include file="examples/ruby/regex_exercise_1.rb" %}

## Python
{% include file="examples/python/regex_exercise_1.py" %}


## Perl
For Perl check out the respective [regex exercise](https://perlmaven.com/beginner-perl-maven-exercise-regexes-1) page on the Perl Maven site.


## Solution - Perl 5

* [Perl 5 regexes 1](https://perlmaven.com/beginner-perl-maven-solution-regexes-1)
* [Perl 5 regexes 2](https://perlmaven.com/beginner-perl-maven-solution-regexes-2)
* [Perl 5 regexes 3](https://perlmaven.com/beginner-perl-maven-solution-regexes-3)



