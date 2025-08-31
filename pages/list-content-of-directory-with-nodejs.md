---
title: "List content of a directory with Node.js"
timestamp: 2015-02-02T09:47:01
tags:
  - fs.stat
published: true
books:
  - nodejs
author: szabgab
archive: true
---


Just as the `dir` command in MS Windows (or more specifically in DOS), or the `ls` command on Unix/Linux,
we would like to implement a Node.js script, that give a directory, can list the content of the directory with
some more information about each entry in the directory.


We already know [how to get information from the inode of a file or directory](/system-information-about-a-file-or-directory-in-nodejs),
so if we only need to generated all the entries in a directory and then call [fs.stat](http://nodejs.org/api/fs.html#fs_fs_stat_path_callback)
for each entry.

This script will accept (and even require) a path to a directory on the command line,
and then it will list the content of the directory. (Without recursion.)

{% include file="examples/node/read_dir.js" %}

If you have read the article about the [fetching system information for a single file](/system-information-about-a-file-or-directory-in-nodejs)
then you already know the first part of the script. The interesting new part is this one:

```javascript
fs.readdir(path, function(err, items) {
    console.log(items);

    for (var i=0; i<items.length; i++) {
        console.log(items[i]);
    }
});
```

Here we use the [readdir](http://nodejs.org/api/fs.html#fs_fs_readdir_path_callback) method of the [fs class](http://nodejs.org/api/fs.html),
that gets a path and a callback function as parameters. It will read the content of the directory into memory and when done it will execute the callback with 2 parameters.
The first one is the error object in case there was an error. The second one is a callback that will be called when the the operation has finished.
If there was an error then the first parameter will hold that information. If everything went well, then the second parameter will be an array with
all the items (files, directories, symbolic links, etc.) that were found in the directory.

At that point, inside the callback function we can either just print the whole array - if we just want to enjoy our success or we can iterate over
the list with a `for` loop and do something with each item. For example we could print each item.

The listing will contain everything, except of `.` which point to the current directory and `..` which represents the parent directory.

This is how it looked:

```
$ node examples/node/read_dir.js ~/work/code-maven.com/examples/

[ 'blocking-read-file.js',
  'node_hello_world.js',
  'node_hello_world_port.js',
  'non-blocking-read-file.js',
  'process_exit.js',
  'raw_command_line_arguments.js',
  'read_dir.js',
  'stats.js' ]
blocking-read-file.js
node_hello_world.js
node_hello_world_port.js
non-blocking-read-file.js
process_exit.js
raw_command_line_arguments.js
read_dir.js
stats.js
```


## Listing the details of each entry

Now that we know how to get the list of entries in a directory, and that we already know how to
[fetch the details about a file](/system-information-about-a-file-or-directory-in-nodejs)
we can combine the two.

{% include file="examples/node/list_dir_direct.js" %}

This code is quite straight forward. And it is also wrong as we'll see soon.

Inside the callback of the `readdir` method,
we have the `for` loop. In that for-loop, on every iteration we print out the name
of the current file (after we have attached it to the full path of the directory) mostly
for debugging purposes, and we call the `fs.stat`. That method in turn accepts a callback function.
In that function we print out the name of the file - this time as part of the result,
and then print out the size of the thing. (We could print out all the other
details as we did in the [other article](/system-information-about-a-file-or-directory-in-nodejs)
but the size will be enough for now.

The output:

```
$ node examples/node/list_dir_direct.js ~/work/code-maven.com/examples/

Start: /home/gabor/work/code-maven.com/examples//blocking-read-file.js
Start: /home/gabor/work/code-maven.com/examples//node_hello_world.js
Start: /home/gabor/work/code-maven.com/examples//node_hello_world_port.js
Start: /home/gabor/work/code-maven.com/examples//non-blocking-read-file.js
Start: /home/gabor/work/code-maven.com/examples//process_exit.js
Start: /home/gabor/work/code-maven.com/examples//raw_command_line_arguments.js
Start: /home/gabor/work/code-maven.com/examples//read_dir.js
Start: /home/gabor/work/code-maven.com/examples//stats.js

/home/gabor/work/code-maven.com/examples//stats.js
97
/home/gabor/work/code-maven.com/examples//stats.js
243
/home/gabor/work/code-maven.com/examples//stats.js
270
/home/gabor/work/code-maven.com/examples//stats.js
151
/home/gabor/work/code-maven.com/examples//stats.js
18
/home/gabor/work/code-maven.com/examples//stats.js
324
/home/gabor/work/code-maven.com/examples//stats.js
27
/home/gabor/work/code-maven.com/examples//stats.js
1382
```

The debugging printout printed the names as expected, but then inside the 
callback of `fs.stat()` we keep printing out the same filename.
comparing the results to the output of 

```
$ ls -l ~/work/code-maven.com/examples/
total 64
-rw-r--r--  1 gabor  staff    97 Jan 29 14:26 blocking-read-file.js
-rw-r--r--  1 gabor  staff   243 Jan 27 12:34 node_hello_world.js
-rw-r--r--  1 gabor  staff   270 Jan 27 12:34 node_hello_world_port.js
-rw-r--r--  1 gabor  staff   151 Jan 29 14:26 non-blocking-read-file.js
-rw-r--r--  1 gabor  staff    18 Jan 31 08:24 process_exit.js
-rw-r--r--  1 gabor  staff    27 Jan 29 14:54 raw_command_line_arguments.js
-rw-r--r--  1 gabor  staff   324 Jan 31 15:26 read_dir.js
-rw-r--r--  1 gabor  staff  1382 Jan 31 10:45 stats.js
```

The sizes seem to match the filenames, because these were printed in the same order
as we called `fs.stat()`, but for some reason the content of the `file`
variable was the same for every callback. This happens because the `file`
variable is just a simple global variable (from the point of view of the
callback) and by the time the first callback was executed, the `file` variable was
already assigned the last entry in the directory. 

So if we want to combine the name of the file and the result of the `fs.stat()` call
then we need to rely on the order of calls. But can we rely on that?
In this particular case of calling stat on items in a single directory,
this might work as we can expect the events to be handled one after the other, but
if the operation was more complex, and especially if there can be internal callbacks as well,
then suddenly we cannot rely on the order of callback calls to be the same as the order
of the initial execution was.

So we need to find a way to pass the `file` parameter to the internal callback.

## Generate callbacks

In this solution, instead of adding a hard-coded callback function
we will call a function named `generate_callback()` that
will generate a callback for us.

So every time we run `fs.stat()`, before `fs.stat()` is actually executed,
JavaScript will call the `generate_callback()` function with the current value of `file`.
The `generate_callback` will create a new function and will return that function. This
newly generated function will become the callback of the `fs.stat()` method.


{% include file="examples/node/list_dir_generate.js" %}

The result:

```
$ node examples/node/list_dir_generate.js ~/work/code-maven.com/examples/
Start: /Users/gabor/work/code-maven.com/examples//blocking-read-file.js
Start: /Users/gabor/work/code-maven.com/examples//node_hello_world.js
Start: /Users/gabor/work/code-maven.com/examples//node_hello_world_port.js
Start: /Users/gabor/work/code-maven.com/examples//non-blocking-read-file.js
Start: /Users/gabor/work/code-maven.com/examples//process_exit.js
Start: /Users/gabor/work/code-maven.com/examples//raw_command_line_arguments.js
Start: /Users/gabor/work/code-maven.com/examples//read_dir.js
Start: /Users/gabor/work/code-maven.com/examples//stats.js

/Users/gabor/work/code-maven.com/examples//blocking-read-file.js
97
/Users/gabor/work/code-maven.com/examples//node_hello_world.js
243
/Users/gabor/work/code-maven.com/examples//node_hello_world_port.js
270
/Users/gabor/work/code-maven.com/examples//non-blocking-read-file.js
151
/Users/gabor/work/code-maven.com/examples//process_exit.js
18
/Users/gabor/work/code-maven.com/examples//raw_command_line_arguments.js
27
/Users/gabor/work/code-maven.com/examples//read_dir.js
324
/Users/gabor/work/code-maven.com/examples//stats.js
1382
```

The variable `file` that is now seen by the callback function
holds the value of `file` when the function was generated
which is the name of the file the `fs.stat()` received as parameter.


## Nameless function generator

Finally let's look at a solution in which we have eliminated the
need to have an external function called `generate_callback`.

The function is still there, it just does not have a name.
Instead of declaring it separately, we have included it in
the expression in `fs.stat()`. I am not sure if I like this
or if I prefer the lengthier, but probably more readable version
with the `generate_callback` function.

{% include file="examples/node/list_dir_noname.js" %}

## Comments

Thanks!

It's worth noting though that for resolving the issue with the filename we could just replace "var" with "let" on line 12:
let file = path + '/' + items[i];

The closure here is just a workaround we had to use before ES2015.

<hr>

This answer doesn't answer how to scan the sub-directories too...

---
You would do that recursively using for loop in his fs.readdir block. You would just need to check the "file" type and run fs.readdir again if it's a directory.
---

I know, but you can do it too, and update the post and code as well, so that people can get benefit in both ways, it will improve your post as well. :-)

<hr>

You saved my life man! Thanks a lot!

<hr>

Thank you for sharing your coding practice.

<hr>

thanks alot ...@Gabor Szabo

<hr>

I can't tell if my comment actually posted, but what is the date on this article? There's some outdated code like `var`, so I wonder what else is outdated, as I'm just learning fs.

<hr>
hello, maybe we can use the let with the local scope in for loop?
also thanks a lot for good demonstrating the var global scope

<hr>

I made a node module to automate this task: [mddir][1]

# Usage

node mddir "../relative/path/"

To install: npm install mddir -g

To generate markdown for current directory: mddir

To generate for any absolute path: mddir /absolute/path

To generate for a relative path: mddir ~/Documents/whatever.

The md file gets generated in your working directory.

Currently ignores node_modules, and .git folders.

# Troubleshooting

If you receive the error 'node\r: No such file or directory', the issue is that your operating system uses different line endings and mddir can't parse them without you explicitly setting the line ending style to Unix. This usually affects Windows, but also some versions of Linux. Setting line endings to Unix style has to be performed within the mddir npm global bin folder.

# Line endings fix

Get npm bin folder path with:

```
npm config get prefix
```

Cd into that folder

brew install dos2unix

dos2unix lib/node_modules/mddir/src/mddir.js

This converts line endings to Unix instead of Dos

Then run as normal with: node mddir "../relative/path/".

### Example generated markdown file structure 'directoryList.md'

|-- .bowerrc
|-- .jshintrc
|-- .jshintrc2
|-- Gruntfile.js
|-- README.md
|-- bower.json
|-- karma.conf.js
|-- package.json
|-- app
|-- app.js
|-- db.js
|-- directoryList.md
|-- index.html
|-- mddir.js
|-- routing.js
|-- server.js
|-- _api
|-- api.groups.js
|-- api.posts.js
|-- api.users.js
|-- api.widgets.js
|-- _components
|-- directives
|-- directives.module.js
|-- vendor
|-- directive.draganddrop.js
|-- helpers
|-- helpers.module.js
|-- proprietary
|-- factory.actionDispatcher.js
|-- services
|-- services.cardTemplates.js
|-- services.cards.js
|-- services.groups.js
|-- services.posts.js
|-- services.users.js
|-- services.widgets.js
|-- _mocks
|-- mocks.groups.js
|-- mocks.posts.js
|-- mocks.users.js
|-- mocks.widgets.js

https://www.npmjs.com/package/mddir


