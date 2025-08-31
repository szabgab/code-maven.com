---
title: "Reading a file with Node.js - blocking and non-blocking"
timestamp: 2015-01-29T11:45:01
tags:
  - fs
  - readFile
  - readFileSync
published: true
books:
  - nodejs
author: szabgab
archive: true
---


If we want to build a web-server using Node.js, or basically any application, then
one of the important things is to be able to read the content of a file.

Node provides the [fs](http://nodejs.org/api/fs.html) library to handle file-system related operations.
For example to read the content of a file.


## Read file in asynchronously (non-blocking)

The "normal" way in Node.js is probably to read in the content of a file in a non-blocking, asynchronous way.
That is, to tell Node to read in the file, and then to get a callback when the file-reading has been finished.
That would allow us to hand several requests in parallel.

For this we can use the [readFile](http://nodejs.org/api/fs.html#fs_fs_readfile_filename_options_callback)
method of the `fs` class.

{% include file="examples/node/non-blocking-read-file.js" %}

First we load the `fs` class using the `require` command. Then we call the `readFile` method
that gets 3 parameters: The name of the file ('DATA' in this case), the encoding of the file ('utf8' in the examples),
and a function. This function is going to be called when the file-reading operation has finished.
The function will get two parameters. The first is the information about any error conditions, the second is the actual
content of the file.

Once this is called Node starts to read the file in the background, but it also keeps executing our program. That is,
it will call the `console.log('after calling readFile');` and will print that text to the console.
Then, once the file has been read into memory, Node will run the function we provided to the `readFile` method
and that will print the content of the file.


## Read file in synchronously (blocking)

People coming from almost every other programming language and environment will find the synchronous file-reading
operation clearer. I am not sure when will you want to use synchronous operations in Node.js, but I see
that many of the asynchronous functions have a synchronous counterpart, so there might be a use.

For reading a file you can use the [readFileSync](http://nodejs.org/api/fs.html#fs_fs_readfilesync_filename_options)
method of the `fs` class:

{% include file="examples/node/blocking-read-file.js" %}

## Comments

The parameter really shouldn't be called 'DATA', should be 'filePath' or sth else self-explanatory.

---

really, it's brings some misunderstoods. It would be better name like 'test.txt', or './test.txt', for example, But despite, THanks a lot. Awesome tutorial for newbies

---

Thanks, good stuff!

---

Noteworthy to say, since both versions return the complete content of the file at once they only work as long as the result fits into a string. (At least when you specify a text encoding like utf8.) So usually that means everything works fine until your file hits 256 mb and none of these functions work anymore.

---

Thank you! Great quick read, exactly what I needed.

---

I'll give you an example of Synchronous operations being amazingly useful, simple building! NodeJS isn't only run on the server or busy powering platforms like Electron. It's also good for simple scripting. I want to write a simple script that pulls in 2 files and outputs them as one and don't want to leverage huge tools like Webpack, Gulp, or Grunt for something tiny and simple. So Synchronous NodeJS to the rescue!

---
That's orthogonal to async vs. sync; it's just as easy to do it async in scripts.
---

I guess you've never really experienced "call-back" hells yet. await makes things so much cleaner and easier, not only for yourself, but all current and future devs involved in the project.

---

Nice post, short and sweet. 👍🍓

---

" I am not sure when will you want to use synchronous operations in Node.js" depends what you are building.. if you are building a dev tool for instance then there is often no need to use the async option, just more code you have to write for no reason as there will only ever be 1 person running the code at any one time.

---

Explained in simple words and with simple code. Nice - thanks!

---
readFileSync and readSync are non-blocking read functions. when there is no data to read, they return an empty buffer. try readSync(0, Buffer.alloc(1), 0, 1, -1) to read 1 byte from stdin

---

Can you please explain, how many different files we can process if suppose we have 4 cors CPU?
I know it's a little bit off the topic, but I just wanted to clarify.

---

The use case is this - People coming from almost every other programming language and environment will find the synchronous file-reading operation clearer.

---

what if I wanted to save a token and reuse it with a callback function? could I use read/write for this case scenario?

---

Good info

---

Thank you very much for this post!!!!!!!!!!!!!

---

fs blocking is faster than async blocking in the long run.

---
If we read file in sync and call this API a thousand times can we see program API halting nature due to blocking operation?

---
it depends on where the file is, and what the file is, we can't do anything while reading this file in the sync mode.

---

Thanks Gabor! Thanks God!

---

You could have put out the explanations on when to use sync and when to use async.
Advantages and disadvantages etc..

---

This code is so outdated, I don't know why it keeps coming up at the top of Google searches for Node.

---
What's your alternative? Complaining without anything actionable is pointless. This is the most basic way to read a file in NodeJS.

---
Seems pretty good to me. What would be the better alternative?
