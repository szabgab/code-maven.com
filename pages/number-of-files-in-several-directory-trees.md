---
title: "Show number of files in several directory trees using Shell"
timestamp: 2017-11-21T08:00:01
tags:
  - ls -1
  - wc -l
  - find -type f
  - "-maxdepth"
  - "-mindepth"
  - "$()"
  - for
published: true
books:
  - shell
author: szabgab
archive: true
---


We already know how to [Show number of files in a single directory tree using Shell](https://code-maven.com/number-of-files-in-a-directory-tree), but what if given a directory,
we would like to know the number of files in each one of its subdirectories separately?


We assume the same directory structure as in that other article:

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

In the [previous article](https://code-maven.com/number-of-files-in-a-directory-tree)
we reached this solution for a single directory:

```bash
$ find groups -type f | wc -l
```

Now we need to go over all the subdirectories and run the above expression for each one of them.

## Wildecard expansion

In our first attempt we use the wildecard expansion `groups/*` to list all the
item in the "groups" directory. We go over it in a `for` loop and for each iteration
we echo the name of the thing and call the above expression.

```bash
$ for x in  groups/*; do (echo $x; find $x -type f | wc -l) ; done

groups/all.txt
1
groups/maskots
2
groups/other
0
groups/people
2
```

The  output includes the directories 'maskots' and 'people' as we wanted, but it
also includes "all.txt" which is a plain file and 'other' which is a symbolic link.

## Find with backtick

We can use `find` here too with `type` directory and `maxdepth` 1,
but that will return the root directory as well:

```bash
$ find groups -maxdepth 1 -type d

groups
groups/maskots
groups/people
```

In this case we can also include `mindepth` to make sure only the right depth is included:


```bash
$ find groups -maxdepth 1 -mindepth 1 -type d

groups/maskots
groups/people
```

Using this we can now write:

```bash
$ for x in  `find groups -maxdepth 1 -mindepth 1 -type d`; do (echo $x; find $x -type f | wc -l) ; done

groups/maskots
       2
groups/people
       2
```


## Using result interpolation

Instead of the backticks ````, it is usually better to write `$()`.
The result is the same:

```bash
$ for x in  $(find groups -maxdepth 1 -mindepth 1 -type d ); do (echo $x; find $x -type f | wc -l) ; done

groups/maskots
       2
groups/people
       2
```


