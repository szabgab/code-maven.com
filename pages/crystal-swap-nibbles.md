---
title: "Crystal: Swap Nibbles"
timestamp: 2021-07-02T17:00:01
tags:
  - Crystal
published: true
books:
  - crystal
author: szabgab
archive: true
show_related: true
---


In this [weekly challenge](https://theweeklychallenge.org/blog/perl-weekly-challenge-119/) the task was to swap the lower and upper 4 bits (nibbles) of an integer.

This is my implementation in the [Crystal language](/crystal).

At first I thought to convert the number to its binary representation and do the swapping there, but then I fugured it is just a simple mathematical operation.


* <b>%</b> is modulo
* <b>//</b> is integer division

Below the function I included the code to iterate over the range between 0 and 255 (inclusive)
and for each iteration print the binary representation (padded with 0s) and the decimal representation of the original number
followed by the decimal representation of the nibble-swapped number.

{% include file="examples/crystal/swap_nibbles.cr" %}
