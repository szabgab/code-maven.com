---
title: "Bash shell always succeed with ||: suffix"
timestamp: 2021-02-23T09:30:01
tags:
  - ||
  - :
  - ||:
published: true
books:
  - shell
author: szabgab
archive: true
show_related: true
---


Trailing <b>||:</b> on Bash commmands look strange, but they are useful.


If you put that expression at the end of another expression then, even if the first expression fails the whole expression will still succeed,
the exit code will be set to 0, and the code will keep running.

See [set -e to stop script on failure](/bash-set-e) and [set -x to print statements as they are executed](/bash-set-x)

{% include file="examples/good.sh" %}

```
$ ./examples/good.sh
+ ls examples/good.sh
examples/good.sh
+ echo 0
0
```

{% include file="examples/bad.sh" %}

```
$ ./examples/bad.sh
+ ls examples/no_such_file.txt
ls: cannot access 'examples/no_such_file.txt': No such file or directory
+ echo 2
2
```

{% include file="examples/bad_without_e.sh" %}

```
$ ./examples/bad_without_e.sh
+ ls examples/no_such_file.txt
ls: cannot access 'examples/no_such_file.txt': No such file or directory
+ echo 2
2
```

{% include file="examples/bad_saved.sh" %}

```
$ ./examples/bad_saved.sh
+ ls examples/no_such_file.txt
ls: cannot access 'examples/no_such_file.txt': No such file or directory
+ :
+ echo 0
0
```

## Explanation

There are two separate pieces of syntax here:

```
||  This is the OR operator.
:   This is a dummy command which will always succeed (return code 0)
```


