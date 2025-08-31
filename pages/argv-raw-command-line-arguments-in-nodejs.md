---
title: "argv - raw command line arguments in Node.js"
timestamp: 2015-01-29T16:00:01
tags:
  - process
  - argv
  - __filename
published: true
books:
  - nodejs
author: szabgab
archive: true
---


People coming from the JavaScript client-side development world did not have to deal with the command line,
but if you write a server side application, then you have good chances you'll have to reach the Linux/Unix
command line. (And if you are not lucky then you might even need to deal with command line on MS Windows.)

Node.js provides an easy way to access the raw data passed on the command line.


Normally on the command line you could pass all kinds of values:

A list of names: `node app.js file1 file2`

Key-value pairs:  `node app.js --port NUMBER --dir PATH`

Flags, without a value: `node app.js --debug --verbose`

You might also want to be able to provide short names: `node app.js -d -v`

And you would also like to be able to combine all these: `node app.js -dv --port NUMBER --dir PATH  file1 file2`

By default Node.js provide an object called [process](http://nodejs.org/api/process.html#process_process_argv)
that has an element called [argv](http://nodejs.org/api/process.html#process_process_argv) which is an
array holding the list of everything provided on the command line:

{% include file="examples/node/raw_command_line_arguments.js" %}

Note: you don't even have to load `process` at it is in your process by default.

Running this command: `node examples/node/raw_command_line_arguments.js -dv --port NUMBER --dir PATH  file1 file2`

will print out this:

```
[ 'node',
  '/Users/gabor/work/code-maven.com/examples/node/raw_command_line_arguments.js',
  '-dv',
  '--port',
  'NUMBER',
  '--dir',
  'PATH',
  'file1',
  'file2' ]
```

Note:

The first element is always `node` itself.

The second element is always the file being executed.

The rest of the elements are the values supplied on the command line after the name of the file being executed.

Basically this is the list of all the values that were typed in on the command line.

You can loop over the array using `for` or `forEach` and extract the values.
This might work well in the most simple cases, but once the parameters become complex, it will
be better to use a higher level library.

I found a [minimist](https://www.npmjs.com/package/minimist),
[nomnom](https://github.com/harthur/nomnom), and
[yargs](https://github.com/chevex/yargs)
(the successor of [node-optimist](https://github.com/substack/node-optimist))
just to name a few.

I don't have an opinion them yet, but I guess one I'll need something complex, I'll have to
check them out.

## A useful snippet for command line scripts

When you don't need to process lots of command line options, but you still would like to make sure
the user provides a value on the command line you can use the following snippet:

{% include file="examples/node/argv.js" %}

In this example we check if the number of elements in the `process.argv` array is less then or
equal to 2. I don't know if it can be ever less than 2, but if it is only 2, then we know the user
has not supplied any parameter on the command line. Then we print out the string "Usage: ",
followed by the name of our file (`__filename` contains the name of the current file) followed by
some indication of what we expect. Instead of " SOME_PARAM" you might want to add some more descriptive
string there. For example "MACHINE_NAME" if you are expecting the name of a machine, or "URL" if you
are expecting a URL.

Then we [exit](/how-to-exit-a-nodejs-script) the code, as without that parameter there is no point in executing the rest of the code.

The rest of the code, can be of course anything you want. In our case we only have 
`console.log('Param: ' + param);` to indicate we reached that point.

This is how the execution works:

```
$ node argv.js 
Usage: /home/gabor/code-maven/examples/node/argv.js SOME_PARAM
```

```
$ node argv.js hello
Param: hello
```

## Comments

thanks for awesome and simple entry guide

<hr>

Just used this to troubleshoot a problem in someone else's code. One of the arguments wasn't being passed correctly on the command line. Thanks!
