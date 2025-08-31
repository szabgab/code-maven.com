---
title: "How to get system information of a file or directory in Node.js (stat)"
timestamp: 2015-01-31T11:30:01
tags:
  - stat
  - fs.Stats
  - isFile
  - isDirectory
  - size
published: true
books:
  - nodejs
author: szabgab
archive: true
---


The Unix/Linux `ls` command can provide all kinds of details about a file or a directory
or symbolic link or some other things that can be on the file-system. Specifically using the `-l`
flag it can show the type of thing we are listing (file/directory/symbolic link/etc), whether it
is readable, writable, executable etc.

In general, it can fetch information from the [inode](http://en.wikipedia.org/wiki/Inode) table,
which is not the Apple version of Node.js.

Before attempting to re-implement the `ls` unix command, let's see how can we fetch the details
of a single file-system entry using Node.js.


The [fs](http://nodejs.org/api/fs.html) library that comes with Node.js provides a non-blocking
method called [stat](http://nodejs.org/api/fs.html#fs_fs_stat_path_callback), that given
a path to something on he file-system, will fetch the information from the <b>inode</b> of that thing
and when done, will execute the callback provided to the method. It will path a
[fs.Stats](http://nodejs.org/api/fs.html#fs_class_fs_stats) object to the callback.

There is also a [synchronous version called statSync](http://nodejs.org/api/fs.html#fs_fs_statsync_path)
that will, return the [fs.Stats](http://nodejs.org/api/fs.html#fs_class_fs_stats) object, once the
data was read from the file-system.

In this script we can see how to use the asynchronous version of this method:

{% include file="examples/node/stats.js" %}

The expected use of the script is `node examples/node/stats.js path/to/file`.

For example I ran `node examples/node/stats.js examples` providing the 'examples'
directory as the parameter and got the following output:

```
examples

{ dev: 16777220,
  mode: 16877,
  nlink: 11,
  uid: 501,
  gid: 20,
  rdev: 0,
  blksize: 4096,
  ino: 32548075,
  size: 374,
  blocks: 0,
  atime: Sat Jan 31 2015 10:56:30 GMT+0200 (IST),
  mtime: Sat Jan 31 2015 10:52:13 GMT+0200 (IST),
  ctime: Sat Jan 31 2015 10:52:13 GMT+0200 (IST) }

    directory
    size: 374
    mode: 16877
    others eXecute: x
    others Write:   -
    others Read:    r
    group eXecute:  x
    group Write:    w
    group Read:     r
    owner eXecute:  x
    owner Write:    w
    owner Read:     r
    file:           -
    directory:      d
```

We can compare that with the output of the appropriate Unix `ls` command:

```
$ ls -ld examples
drwxr-xr-x  11 gabor  staff  374 Jan 31 10:52 examples
```

Let's take that script apart:

```javascript
var fs = require('fs');

if (process.argv.length <= 2) {
    console.log("Usage: " + __filename + " path/to");
    process.exit(-1);
}

var path = process.argv[2];
```

After loading the `fs` module, we check the number of [arguments passed on the command line](/argv-raw-command-line-arguments-in-nodejs).
If it is 2 or fewer (and I am not even sure fewer would be possible), that means the user has not give any command line parameters.
(If the user wrote `node examples/node/stats.js` then this number will be 2.) In that case we print out a usage-message that looks like this:

```
$ node examples/node/stats.js
Usage: /home/gabor/code-maven/examples/node/stats.js path/to
```

The global variable `__filename` (starting with two underscores) contains the full path to the current JavaScript file.

Then we call `process.exit()` to [leave the Node.js script](/how-to-exit-a-nodejs-script) early.
Before reaching the end of the file.

The last step in this part of the code is to fetch element 3 of the `argv` which is the value the user has passed on the
command line, and assign it to a variable called `path`.

## Calling fs.stat

Then we call the [stat](http://nodejs.org/api/fs.html#fs_fs_stat_path_callback) method, passing
the `path` variable and the callback. This callback function will receive and error-object - if there was an error,
and a [fs.Stats](http://nodejs.org/api/fs.html#fs_class_fs_stats) object.

```javascript
fs.stat(path, function(err, stats) {
```

The `Stats` object contains some data retrieved from the inode table (in our case it looked like this:)

```
{ dev: 16777220,
  mode: 16877,
  nlink: 11,
  uid: 501,
  gid: 20,
  rdev: 0,
  blksize: 4096,
  ino: 32548075,
  size: 374,
  blocks: 0,
  atime: Sat Jan 31 2015 10:56:30 GMT+0200 (IST),
  mtime: Sat Jan 31 2015 10:52:13 GMT+0200 (IST),
  ctime: Sat Jan 31 2015 10:52:13 GMT+0200 (IST) }
```

and it provides a few methods for more convenience.

Among the values that we got there `dev` is the device number. It might be interesting if you have
multiple disks or partitions mounted.

`mode` contains a lot of information, including the type of the thing (file/directory/symbolic link)
and the permissions on that thing.

`uid` is the user-id of the owner of this thing.

`gid` is the group-id of the owner of this thing.

`size` is, the size of the thing in bytes.

`atime`, `mtime`, and `ctime` are 3 different timestamps representing the last
access time, the last modify time and the create time of the thing.

Before checking out the value of `mode`, let's see a few helper functions:

`isFile()` will return `True` if the thing is a file.

`isDirectory()` will return `True` it the thing is a directory.

There are a few more such helper functions listed in [documentation of fs.Stat](http://nodejs.org/api/fs.html#fs_class_fs_stats).

The other values of the stat object can be accessed just as regular members of any JavaScript object.
For example it is easy to access the size of the file:

## Size of a file in Node.js

```javascript
console.log('    size: ' + stats["size"]);
```

## Mode and file access rights

[man 2 stat](http://man7.org/linux/man-pages/man2/stat.2.html) provides information on how to interpret
the values in `mode` which was 16877 in our case.

We need to use special bitwise masks on that number to check if specific bits are on or off in that number.
For example `mode & 1` will be 1 if the right-most bit in `mode` was on. Otherwise this will be 0.

`mode & 2` will be 2 if he second bit from the right was on, and 0 if it was not.

`mode & 4` will be 4 if he third(!) bit from the right was on, and 0 if it was not.

Luckily numbers, except of 0, are considered True in JavaScript. So we could use the
ternary operator `?:` to returns some interesting character if the expression is different from 0
and return `-` if the expression was 0.

That's how our output resembles (in the usage of `rwx-` characters) to the output of `ls -ld`.

Besides the read-write-execute flags, we can also extract the file-type from the the `mode`
value, but for those we have already seen a set of more readable convenience methods.

## Comments

I read the article several times, but I could not associate the same in my need, I need inside a folder to get the name of the last created file

<hr>

It is much easier to use stat-mode in order to get the user/group/others permissions https://www.npmjs.com/package/stat-mode

<hr>

Can anyone Answer me?
I have List of files in the folder. i need to read the file from the folder while if i met criteria , i have to come out from the function and update the document.Ultimately i dont need to read all the files when condition met. using Node.js?

<hr>

Group and Owner permissions check looks wrong. Group execute should be stats["mode"] & 8, write should be stats["mode"] & 16 and so forth.


