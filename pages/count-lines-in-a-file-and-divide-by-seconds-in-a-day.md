---
title: "Count number of lines in a file and divide it by number of seconds in a day using Bash"
timestamp: 2016-11-30T08:20:01
tags:
  - Bash
published: true
author: szabgab
archive: true
---


This title might sound strange with two unrelated tasks, but there is a story behind it. I was working on some data processing application that was converting files to some other format. After checking the code, I found that it takes about 1 second to convert a single file and I wanted to know how long will it take to convert all the files.


It isn't really difficult. Just run `find somedir | wc -l` and we get the number of seconds. Except that I already knew there are a lot of files so I split that in two separate steps:

## List all the files

```bash
$ find somedir > files.txt
```

I know, it would be more correct if I ran

```bash
$ find somedir -type f > files.txt
```

but the impact was rather small.

Then I can run

```bash
wc -l files.txt
```

I ran the first command and it did not end.

I ran `wc -l files.txt` several times and I saw the file was growing
and growing and it passed the 1,000,000 and I started to wonder how many days are all those seconds.

One day is 86,400 seconds that can be calculated as `(( x = 60*60*24*72 )); echo $x`

## Bash expression

Anyway, here is the expression I came up with:

Count the lines in a file and divide it by number of seconds in a day which is 86400

```bash
let "x=$(wc -l find.txt | cut -d' ' -f1)/86400"; echo $x
expr $(wc -l find.txt | cut -d' ' -f1) / 86400
```

