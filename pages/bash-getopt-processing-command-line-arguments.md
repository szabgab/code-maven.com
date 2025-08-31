---
title: "Bash: parsing command line arguments with getopt"
timestamp: 2019-06-17T07:30:01
tags:
  - getopt
published: true
books:
  - bash
author: szabgab
archive: true
---


In this example we have a function that can optionally! accept the following parameters:


```
-v
-d
--debug
--name VALUE
```


The call to <gl>getopt` defines the accepted names.
The `-o dv` defines that we accept two short switches `-v` and `-d`.
The `--long debug` defines that we accept the `--debug` switch.
The `--long name:` defines that we accept the `--name` option followed by some value.

Then we have a whole `while` loop to actually take out the values from the list on the comand line
and to assign the appropriate values to variables.
Either 1 to the variables representing the switches, or the actual value passed to the `--name` option.

At the end we need to call this function with the `args $0 "$@"` expression.

{% include file="examples/shell/cli.sh" %}

## An example calling it

```
$ ./cli.sh --name "Foo Bar" --debug -v

Foo Bar
1
1
```

```
$ ./cli.sh --wrong

getopt: unrecognized option '--wrong'
Incorrect option provided
```


## If condition in bash

I used to have this, in the above code:

```
[ $? -eq 0 ] || {
    echo "Incorrect option provided"
    exit 1
}
```

This is I think the shell-style meaning:

"Either the previous command is successful (exit 0)  or `||` do the block (echo and exit)".

Later I realized using `if` would make it much more readable so I changed it to:

```
if [ $? -ne 0 ]; then
    echo "Incorrect option provided"
    exit 1
fi
```

They both do the same.

