---
title: "Bash shell path relative to current script"
timestamp: 2019-05-22T22:30:01
tags:
  - realpath
  - dirname
  - $0
published: true
books:
  - shell
author: szabgab
archive: true
---


If you bash script then it is a good idea to make sure it does not matter where you put the script
and what is your current working directory when you run it.

If you have a large project written using bash then it is even more important to make it directory independent.
So developers can have the whole project in any location on their disk and it still functions.

In such case, however, how does a script find other files that come with the project? e.g. Imagaes or data files.

It is easy. Use relative pathes.


Let's say this is the directory structure of your project:

```
project/
├── bin
│   └── code.sh
└── data
    └── names.txt
```

How can the "code.sh" reliably find the "names.txt" file?
It needs to find its own directory. Then go one directory up and then enter the "data" directory.

We can use the `realpath` and `dirname` command as we saw them in the
page about [absolute path](/bash-absolute-path).


We have a similar case in the code-maven directory tree. It looks like this, just a lot bigger:

```
.
├── examples
│   ├── data
│   │   ├── airports.csv
│   │   └── words_to_sort.txt
│   ├── shell
│   │   ├── relative.sh
│   │   ├── relative_one.sh
│   │   ├── relative_project.sh
```

The point is, however, that getting from the `relative.sh` we need to go one directory up and then down the
"data" direcotry.

This script implements it step by step using `realpath` and then `dirname`:

{% include file="examples/shell/relative.sh" %}

```
./examples/shell/relative.sh
/home/gabor/work/code-maven.com/examples/shell/relative.sh
/home/gabor/work/code-maven.com/examples/shell
/home/gabor/work/code-maven.com/examples
DATA: /home/gabor/work/code-maven.com/examples/data
```

In the following example we do it in one step:

{% include file="examples/shell/relative_one.sh" %}

```
DATA: /home/gabor/work/code-maven.com/examples/data
```

In the last example we split it into two steps and went a bit further.

In the first step we calculate the path to the root of the project, the root of our git repository.
(In our case it is the parent directory of the "examples" directory, that is 2 steps above the "shell" directory
so we call `dirname` 3 times. Once to get rid of the filename and then twice to move up the directory tre to the
root of the project. Then from there we can add the path of each file or directory relative to the root of the it
working directory.

{% include file="examples/shell/relative_project.sh" %}

```
/home/gabor/work/code-maven.com
DATA: /home/gabor/work/code-maven.com/examples/data
```


As you can from the results, no matter which version you pick, it can point to the directory where the data is located.
