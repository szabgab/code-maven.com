---
title: "Simple command-line counter with file storage in R"
timestamp: 2023-02-10T14:30:01
tags:
  - R
published: true
author: szabgab
archive: true
show_related: true
---


I have been learning R and preparing [examples for R](https://code-maven.com/slides/r/). One of the fun small script I created is also part of the [counter example series](/counter).

{% include file="examples/r/counter.R" %}

After [installing R](https://cran.r-project.org/) we can run this script by typing in

```
Rscript counter.R
```

In R there are at least 3 ways to assign a value to a variable. One can use the boring <b>=</b> sign as we have in the first two assignments.
We can also use the left arrow <b>&lt;-</b> and we can also use the <b>-&gt;</b>. In this script I used all 3, just to demo them. I think in a real script I'd stick to boring <b>=</b>, but as I can see code written by others, the also like to use the other signs.

The <b>file.exists</b> and the <b>readLines</b> functions seem to have very descriptive names.

The <b>as.numeric</b> function converts a string or "characters" as they are called in R to a number or "numeric" as it is referred to in R.

<b>cat</b> is a similar to <b>print</b>, but as I understand it is more generic function. Among other things it does not "number" the output lines. It also accepts various parameters such as the <b>end</b> parameter and the <b>file</b> parameter.

The <b>file</b> function with the <b>w</b> parameter opens the file for writing and returns a filehandle. We then use <b>cat</b> and direct its output to the file. At the end we <b>close</b> the file.


