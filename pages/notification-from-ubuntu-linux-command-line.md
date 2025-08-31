---
title: "Add notification to my command line on Ubuntu Linux"
timestamp: 2020-11-12T07:30:01
tags:
  - notify-send
published: true
author: szabgab
archive: true
show_related: true
---


IntelliJ shows me a notification on MS Windows when the tests are done. (At least if it is not in focus).
This helps me bring back my focus if I switched it away.

I would like to have a similar for my command line on Linux. Either running the commands with some prefix
or automatically on every command on the terminal. Maybe on every long running command.


```
notify-send Done "$command"
```

I even created a file called <b>not</b> with the following content:

```
#!/bin/bash
command=$*
#echo $*
$*
notify-send Done "$command"
```

I put it somewhere in my PATH and made it executable <b>chmod +x not</b>.

Now I can run

```
not command
```

and I'll get a notification when the job is done.

