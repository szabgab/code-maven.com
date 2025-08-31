---
title: "Sequence without 1-on-1 in Crystal"
timestamp: 2021-07-02T18:30:01
tags:
  - Crystal
published: true
books:
  - crystal
author: szabgab
archive: true
show_related: true
---


This is the solution for [the weekly challenge](https://theweeklychallenge.org/blog/perl-weekly-challenge-119/) called
<b>Sequence without 1-on-1</b> in which we are asked to generate a sequence of numbers starting with 1 where each element can contain only the digits 1, 2, or 3
and there can't be 1 twice next to each other. That is "11" cannot be part of the decimal representation of the number.

This solution is written in the [Crystal programming language](/crystal).



## Directory layout

```
.
├── spec
│   └── seq_spec.cr
└── src
    ├── list_seq.cr
    ├── seq.cr
    └── use_seq.cr
```

## The implementation

{% include file="examples/crystal/sequence-without-1-on-1/src/seq.cr" %}

Crystal has multiple-dispatch so we can defined the same function with different signatures.
Here we have two definitions of the <b>seq</b> function. The first one expects a block and will
call the block on every iteration when the code reaches the <b>yield</b> statement.
The function declaration contains <b>&block</b> but that's optional and I only included
in the hope that it makes it clearer that the function expects a block of code.

Inside we have a condition-less <b>loop do ... end</b> which is basically an endless loop.
(even though we do have the <b>end</b> word there ... I know, this was a bad pun)

Inside the loop we increment the value (there is no <b>++</b> in Crystal), then use a regular expression
on the stringified (<b>to_s</b>) version of the number. <b>=~</b> is the regex match operator just as in Perl.
<b>//</b> delimiters the regex, just as in Perl. <b>next</b> is the same as in Perl (other languages have <b>continue</b> instead).

In Crystal an <b>if</b> can be written as the [suffix of an expression](https://crystal-lang.org/reference/syntax_and_semantics/as_a_suffix.html)
and it becomes a statement modifier as it is called in Perl. The condition checked first and only if it <b>true</b> then <b>next</b> is called.

Then we have the <b>yield num</b> statement that will execute the block passing <b>num</b> as an argument. You can see this in use in the <b>list_seq.cr</b> file below
and also in the second implementation of the <b>seq</b> function.

Here we are expecting an Int32 number and we also declare that we are going to return an Int32 number.
Inside we call seq with a block (so this will execute the first implementation). We count down from N to 0 and thus return the Nth
element of the sequence.

## Use the sequence generator

{% include file="examples/crystal/sequence-without-1-on-1/src/list_seq.cr" %}

In this example we use the sequence generator directly. If we did not have some
explicit statement to leave the block it would iterate till we run out of Int32
and then it would raise an exception: <b>Unhandled exception: Arithmetic overflow (OverflowError)</b>

<b>break if num > 200</b> still first checks the condition and only if it is <b>true</b> then it will <b>break</b> out of the block.

{% include file="examples/crystal/sequence-without-1-on-1/src/use_seq.cr" %}

This is the example in which you can pass a number on the command line and it will print the Nth value in the sequence.

```
crystal src/use_seq.cr 60
```


## Testing / Spec

This is the spec file. One could cd into the root of the "project" and type <b>crystal spec</b>
to execute the tests.

{% include file="examples/crystal/sequence-without-1-on-1/spec/seq_spec.cr" %}

