---
title: "ps does not show name of the shell script only -bash or bash - Linux"
timestamp: 2019-08-12T07:30:01
tags:
  - ps
  - bash
published: true
author: szabgab
archive: true
---


Recently, on a CentOS box I've noticed that when I run `ps -ef` or `ps axuw` some of my scripts don't show
up. I also checked this on Ubuntu 19.04 with similar results.

TLDR: add `#!/bin/bash` as the first line of your Bash script.

I ran a little experiment.


Created a script called <b>hello.sh</b> with the following content:

{% include file="examples/shell/hello.sh" %}

Made it executable: `chmod +x hello.sh` and ran it:

```
./hello.sh &
```

I tried to see if I can find the process using ps and grepping for the name of the process, but it did not show up.

```
ps -ef | grep hello
```

Then I did the same but this time grepping for the process ID. (That's why I printed it in my experimental script.)

```
ps -ef | grep 12345
```

This time I saw the process and the name of the process was `-bash`.

## sh-bang line

Usually in Linux/Unix the first line of each script should point to the command that will be able to interpret the code
in the file. It is called [sh-bang](https://en.wikipedia.org/wiki/Shebang_(Unix)).

I've added it to the script (and renamed it becasue the web site can only have one file with the same name):

{% include file="examples/shell/hello_again.sh" %}

Making this executable: `chmod +x hello_again.sh` and runing this the same way: `./hello_again.sh`.
This time the full name showed up in the output of `ps`.

## Running with bash

I tried also running it with `bash` like this:

```
bash hello_again.sh
```

On Ubuntu it seems it showd up with the full name, but as I recall in CentOS it had the same result as the first
version, showing up only as `-bash`.

