---
title: "Python: split command line into pieces as the shell does - shlex.split()"
timestamp: 2019-01-14T07:30:01
tags:
  - shlex
  - split
published: true
author: szabgab
archive: true
---


Sometime, for example when you use <b>subprocess</b> you might want to run an external program avoiding the
invocation of the shell. For that you need to have the external command in pieces, not in a single long string.

So what if you have the command as a string?


You could use the regular `split` method of strings with space as the delimiter,
but that would not give you the right results if some of the pieces contain spaces.

For example if this is the command line:

```
'./bin/application --source /some/directory --target /other/dir --verbose -d --name "Foo Bar"'
```

The solution is to use the `split` method of the `shlex` module.

In this example we use both. The `str.split()` and the `shlex.split()`

{% include file="examples/python/split_command_line.py" %}

The results are here:

```
['./bin/application', '--source', '/some/directory', '--target', '/other/dir', '--verbose', '-d', '--name', '"Foo', 'Bar"']
['./bin/application', '--source', '/some/directory', '--target', '/other/dir', '--verbose', '-d', '--name', 'Foo Bar']
```


For more details read the documentation of [shlex](https://docs.python.org/library/shlex.html).

Oh and jut to be clear, if you want your code to accept command line parameters then you don't need to worry about this
as the shell will already split up the parts and python will store them in `sys.argv`.
Then you need to use something to parse that list. For example [argparse](/python-argparse).

