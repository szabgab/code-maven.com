---
title: "at - running a command at some time in the future in Linux (relative time or absolute time)"
timestamp: 2018-11-14T07:30:01
tags:
  - at
published: true
author: szabgab
archive: true
---



## Install "at" on Ubuntu

```
sudo apt-get install at
```

## Commands in a file - relative time

Save your commands in a file. e.g.   <b>run.sh</b> will look like this:

```
date > a.txt
whoami >> a.txt
```

Then schedule it to be execute a minute later:

```
at now + 1 minute < run.sh
```


## Run without file - relative time

```
echo "date > b.txt" | at now + 1 minute
```

A minute later you can check your file system. You'll see a new file called "b.txt" with the date in it.


## Run without file - absolute time

```
echo "date > c.txt" | at 04:58
```

At 04:58 the file c.txt will be created with the timestamp in it.

