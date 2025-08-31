---
title: "Create temporary directory on Linux with Bash using mktemp"
timestamp: 2019-01-11T07:30:01
tags:
  - mktemp
  - date
published: true
author: szabgab
archive: true
---


When writing a test or whenn running a build job it is usually a good practice to use a temporary directory and then
clean up after the process is done.

It is also a good practice to make sure the temporary directoy is unique so if two processes run at the same time they
won't interfere.


In Linux one usually has a directory called `/tmp` to store temporary files. In most of the programming languages
there is some tool to create temporary directories. Sometimes these also handle the removal of these directories once
they are not needed any more.

In Unix/Linux shell we can use the `mktemp` commmand to create a temporary directory inside the `/tmp`
directory.

```
mktemp -d -t ci-XXXXXXXXXX
```

The `-d` flag instructs the command to create the directory.

The `-t` flag allows us to provide a template. Each `X` character will be replaced by a random character.
The more such characters the better your chances of having a unique directory. The rest of the template can and should
be use to make it clear what is the purpose of the directory. In the above example this directory was created for and by
the CI system.

The command will print the directory to the screen, but you can capture it to a variable and you can use it to
create your files in this temporary directory.

```
tmp_dir=$(mktemp -d -t ci-XXXXXXXXXX)
```

At the end of the process you will probably want to remove the directory.

Here is a full example:

{% include file="examples/ci.sh" %}

It will print the name of the directory that will look like this:

```
/tmp/ci-9p1TBXRJZK
```


## Date based directory

It can be also a good idea to include the date in the name of the directory.
Especially if we might keep it for later observation. In any case here is
an example on how to generate a temporary directory that has a fixed part,
a date-based part, and a random part:

{% include file="examples/ci-date.sh" %}

The directory name will look like this:

```
/tmp/ci-2019-01-11-11-48-34-KdQBLLObFw
```


## Other root directory

By default the temporary directory will be created inside the `/tmp` directory.
Sometimes we might want it to be in some other directory. For example I've created a tmp
directory in my home directory and wanted to place the temporary directories inside that
directory:

{% include file="examples/ci-other.sh" %}

The path to the new directory will look like this:

```
/home/gabor/tmp/ci-PWDTbA19TA
```


For further options you might want to check out the [documentation of mktemp](https://www.gnu.org/software/autogen/mktemp.html).
