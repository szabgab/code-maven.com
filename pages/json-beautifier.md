---
title: "Pretty print JSON with beautifier: How to make a JSON readable"
timestamp: 2018-09-18T17:30:01
tags:
  - JSON
  - Perl
  - Python
  - Ruby
published: true
author: szabgab
archive: true
---


[jq](https://stedolan.github.io/jq/) is the swiss army knife for dealing with JSON files. If you can install it use that.

However I often find myself in situations where, for whatever technical, legal, or just plain stupid reason I cannot install it.

If you find yourself in similar situation, here are a few tools that might help you.


## What is JSON

Read a bit about [JSON](/json).

## Input

Just a random JSON file:

{% include file="examples/data/in.json" %}

## Expected Output

{% include file="examples/data/out.json" %}

## How to use these?

Save the code in a file. Make the file executable:

```
chmod +x filename
```

Run the file and redirect the JSON string into its Standard Input (STDIN).
If the JSON is in a file called "in.json":

```
./filename < in.json
```

If it is received from an API then:

```
curl http://... | ./filename
```


## Perl 5

If you have Perl 5 installed you might use the following code:

{% include file="examples/jq.pl" %}

You could also use one of the other [JSON implementations](https://perlmaven.com/json) in Perl
and you can also read my [Perl Tutorial](https://perlmaven.com/).

## Rakudo Perl 6

If you have [Rakudo](http://rakudo.org/) [Perl 6](https://perl6.org/) installed you might use the following code:

{% include file="examples/perl6/jq.pl6" %}

and then you can read more on the [Perl 6 Maven](http://perl6maven.com/) site.

## Python

{% include file="examples/python/jq.py" %}

Please remember NOT to call this file json.py as that will not work.

An alternative Python one-liner suggested by [Caleb Clark](https://www.linkedin.com/in/caleb-clark-0529ab2/) looks like this:

```
python -m json.tool in.json
```

```
curl ... | python -m json.tool
```


## Ruby

It is less likely that you have Ruby installed, but in any case here is the example in Ruby:

{% include file="examples/ruby/jq.rb" %}


