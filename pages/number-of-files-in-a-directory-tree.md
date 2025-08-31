---
title: "Show number of files in a directory tree using Shell"
timestamp: 2017-11-16T07:30:01
tags:
  - ls -1
  - wc -l
  - find -type f
published: true
books:
  - shell
author: szabgab
archive: true
---


Given a directory tree such as in the following example, we would like to know

1. How many files are in it?
1. How many files are in each one of the subdirectories?

```
groups/
  all.txt
  people/
    John.txt
    Jane.txt
  maskots/
    Foo.txt
    Bar.txt
  other -> maskots
```

All that using the Unix/Linux Shell.


## Number of items in the directory

If we would like to know the number of files in the `groups` directory we can run
`ls -1 groups` (that's the number one in the options), That will list
all the items in the directory:

```shell
$ ls -1 groups
all.txt
maskots
people
other
```

We can then pipe it through `wc -l` (that's the lower case L in the options) that will count
and display the number of lines in the standard input:

```shell
$ ls -1 groups | wc -l
     4
```

`wc` stands for word-count, the `-l` flag tells it to count lines.

This contains everything in the directory: files, directories, symbolic links and whatnot.
In addition it only counts the items in the immediate directory. Not in the whole tree.

This is not really what we wanted though.

## Number of items in the directory tree

If we run the `find` command and only give it the name of the directory it will "find" everything within
that directory tree. Including all its subdirectories.

```shell
$ find groups
groups
groups/all.txt
groups/maskots
groups/maskots/Bar.txt
groups/maskots/Foo.txt
groups/other
groups/people
groups/people/Jane.txt
groups/people/John.txt
```

Note: It lists 'other', but not the 2 files that are inside the directory where 'other' links to.
In other words: it won't descend into directories pointed to by symbolic links.
In the unlikely case that we wanted to follow symbolic links we can run `find -L groups`.

We can count the number of entries using `wc -l` as we did with the `ls`.

```shell
$ find groups | wc -l
     9
```

This contains all the items in the whole directory tree.
Files, directories, symbolic links, etc.

## Number of files in the dirctory tree

If we would like to count only the files, we can tell `find` to print out only the names of the files using the
`-type f` option:

```shell
$ find groups -type f
groups/all.txt
groups/maskot/Bar.txt
groups/maskot/Foo.txt
groups/people/Jane.txt
groups/people/John.txt
```

Piping it through the `wc -l` we get:


```shell
$ find groups -type f | wc -l
       5
```

## Number of files in the directory

Though this was not our original task, but if we would like to know the number of
**files** in the directory (and not the whole tree) we can use `find`
to restrict the item type to file as we already did, and we can also ask it to
go only 1 level deep in the directory structure. Meaning not to traverse.

```shell
$ find groups -maxdepth 1 -type f | wc -l
       1
```


(The groups directory tree can be found [here](https://github.com/szabgab/code-maven.com/tree/main/examples/groups).)

## Comments

Note that, within a script or pipe, ls acts the same as ls -1, so there is no need to specify the -1 option. So, "ls | wc -l" will have the same result in less characters (and one less option to remember to use).


