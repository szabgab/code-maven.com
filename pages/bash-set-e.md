---
title: "Bash set -e to stop script on failure"
timestamp: 2019-07-20T12:00:01
tags:
  - set
  - -e
  - +e
published: true
books:
  - shell
author: szabgab
archive: true
---


Normally if one of the commands executed by a shell script fails it set an exit code different from 0, but the script
will not stop. In some cases this might be the proper behavior, but in many cases, especially in a CI system
you'll probably want your shell script to fail of one of its commands failed.

The `-e` tells Bash to stop immediately if one of the statements it executes has an exit-code different from 0.


## Exit code

Every command you run on the command line of Linux has an exit code. 0 indicates success. Any other number is a failure.
The variable `$?` contains the exit-code of the previous command.

E.g. a successful command:

```
$ ls
...  (the content of the directory)

$ echo $?
0
```

A failed command:

```
$ ls some-place-that-does-not-exist
ls: cannot access 'some-place-that': No such file or directory

$ echo $?
2
```


## Shell script without -e

In this script we have 3 commands. The 2nd fails, but it does not bother the main script. It keeps working and
executes the 3rd command.

{% include file="examples/shell/no-set-e.sh" %}

```
$ ./examples/shell/no-set-e.sh
Start
ls: cannot access 'some-incorrect-path': No such file or directory
Still working


$ echo $?
0
```

Not only that, but the whole script indicates success (its own exit code is set to be 0) even thought some part of it
have failed.



## Shell script with -e

We can set the `-e` either on the sh-bang line or with the `set -e` command.
We can turn it off using the `set +e` command.

{% include file="examples/shell/set-e.sh" %}

```
$ ./examples/shell/set-e.sh
Start
ls: cannot access 'some-incorrect-path': No such file or directory

$ echo $?
2
```

Here, as you can see, after the 2nd command fails, the whole script stops and the exit-code of the script is set
to a non-zero number indicating failure.


