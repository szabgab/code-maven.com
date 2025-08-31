---
title: "Bash: get absolute path to current script"
timestamp: 2019-05-22T21:30:01
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


There can be many reasons why you'd want to get the exact location of your currently running script.
For example to calculate the [relative path](/bash-shell-relative-path) in a reliable way.

Luckily there is a command called `realpath` that will calculate and print the absolute path
of a given path.


Let's see how it works:

{% include file="examples/shell/absolute.sh" %}

`$0` is the name of the current script as it was executed. So if we run the script as `./examples/shell/absolute.sh`
then that will be the content of `$0`.

`realpath` prints the abosulte path.

`dirname` prints the directory name, leaving the last part of the path which is in this case the name of the
file.

Let's see a couple of examples:

```
$ ./examples/shell/absolute.sh

./examples/shell/absolute.sh
/home/gabor/work/code-maven.com/examples/shell/absolute.sh
/home/gabor/work/code-maven.com/examples/shell
```


```
$ cd examples/shell/
$ ./absolute.sh                                                      # run right where it is

./absolute.sh
/home/gabor/work/code-maven.com/examples/shell/absolute.sh
/home/gabor/work/code-maven.com/examples/shell
```

```
$ cd ../../sites/en                                                  # go to a cousin of the scripts directory
$ ../../examples/shell/absolute.sh                                   # run relatively from there

../examples/shell/absolute.sh
/home/gabor/work/code-maven.com/examples/shell/absolute.sh
/home/gabor/work/code-maven.com/examples/shell
```

```
$ ln -s ../../examples/shell/                                        # create a symbolic link to the directory
$ ./shell/absolute.sh                                                # run using the symlink

./shell/absolute.sh
/home/gabor/work/code-maven.com/examples/shell/absolute.sh
/home/gabor/work/code-maven.com/examples/shell
```

```
$ ln -s ../../examples/shell/absolute.sh                             # create a symlink to the script
$ ./absolute.sh                                                      # run using the symlink

./absolute.sh
/home/gabor/work/code-maven.com/examples/shell/absolute.sh
/home/gabor/work/code-maven.com/examples/shell
```

```
$ /home/gabor/work/code-maven.com/examples/shell/absolute.sh         # run with full path

/home/gabor/work/code-maven.com/examples/shell/absolute.sh
/home/gabor/work/code-maven.com/examples/shell/absolute.sh
/home/gabor/work/code-maven.com/examples/shell
```

```
$ export PATH=/home/gabor/work/code-maven.com/examples/shell:$PATH   # make sure the directory of the script is in the path
$ cd                                                                 # go home
$ absolute.sh                                                        # run without knowing where it is

/home/gabor/work/code-maven.com/examples/shell/absolute.sh
/home/gabor/work/code-maven.com/examples/shell/absolute.sh
/home/gabor/work/code-maven.com/examples/shell
```


As you can see in every case `$` was exactly as we invoked the script. Except of the last case where we invoked
it by name only and relied on the content of the `PATH` environment variable and the shell to find the script.
In that case <b>$0</b> already contained the full path.

However the 2nd and 3rd line of output were exactly the same in every case.

So we can rely on the `realpath` to consistently return the real full path of the script.
Even if we execute it via a symbolic link.


