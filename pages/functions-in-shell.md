---
title: "Functions in Linux shell (bash)"
timestamp: 2019-01-17T20:30:01
tags:
  - shell
  - bash
  - function
  - return
published: true
author: szabgab
archive: true
---


## Define and call a function in Bash

{% include file="examples/shell/hello_world_function.sh" %}


## Return value from shell function

{% include file="examples/shell/return_from_function.sh" %}


## Parameter passing to functions in shell

{% include file="examples/shell/parameter_passing.sh" %}

## Early return from shell functions

{% include file="examples/shell/early_return.sh" %}


See also [Returning Values from Bash Functions](https://www.linuxjournal.com/content/return-values-bash-functions)


## Empty shell functions

{% include file="examples/shell/empty.sh" %}

This does not work, but gives this error:

```
./empty.sh: line 3: syntax error near unexpected token `}'
./empty.sh: line 3: `}'
```

{% include file="examples/shell/empty_with_colon.sh" %}


## A Bash function can be called only after declaration

```
# qqrq    # ./func.sh: line 2: qqrq: command not found

function qqrq()
{
   echo "hello"
}

qqrq
```


