---
title: "Bash set -x to print statements as they are executed"
timestamp: 2019-07-20T11:30:01
tags:
  - set
  - -x
  - +x
published: true
books:
  - shell
author: szabgab
archive: true
---


Setting the `-x` tells Bash to print out the statements as they are being executed.
It can be very useful as a logging facility and for debugging when you need to know which statements were execute and
in what order.



It can be enabled on the command line or on the sh-bang line by providing `-x` or by the `set -x` statement.

It can be disabled using the `set +x` statement.

See this example:

{% include file="examples/shell/set-x.sh" %}

and the output it generates:

```
$ ./examples/shell/set-x.sh

+ name=Foo
+ echo Foo
Foo
+ set +x
42
+ language=Bash
+ echo Bash
Bash
```

