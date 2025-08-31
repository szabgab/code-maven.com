---
title: "Getting started with Node.js"
timestamp: 2015-01-28T12:40:01
tags:
  - require
  - http
published: true
books:
  - nodejs
author: szabgab
archive: true
---


Having seen the beginning of a number of tutorials about Node.js, I thought I should also start with the simple "Hello World" example.


Before you can get started, you'll probably need to install [Node.js](http://nodejs.org/), but I don't want to
bog you down with such details. It was straight forward for me on OSX, and I have not tried it on other operating systems yet.

## Hello World

{% include file="examples/node/hello_world.js" %}

In the first line of this example we load the [http](http://nodejs.org/api/http.html) library that provides all the necessary to tools
to run a simple, non-blocking web server.

Then we create a server object using the [createServer](http://nodejs.org/api/http.html#http_http_createserver_requestlistener) method of the `http` class we have just loaded.
This method receives a single parameter which is a function. Whenever a user will access our web-site this function will be called
receiving two parameters. The first one representing the current `request` and the second one representing the current `response`.

In this example we don't care what the user asked for (hence we don't look at the request object), we just give an answer.
First we set the response header which is the [200 OK HTTP status code](http://en.wikipedia.org/wiki/List_of_HTTP_status_codes)
meaning "everything is fine". Then we send back the actual content of our page, and finally we call the `end()` method
of the response object signaling the end of our response.

We took the server object that was created by the `createServer` method and assigned it to the `s` variable.
Then we called the `listen` method of this object launching the server.

Because Node.JS is non-blocking, this did not block our script, it just told the "event-loop" of Node.js to really start listening on
port 8080. The last line in the example was just a simple output to our console, (the command line where we run this code),
to notify the user where to point the browser.

Once I typed this in I was happy and ran my code:

`node examples/node/hello_world.js`

the output?

```
Listening on http://127.0.0.1:8080/

events.js:72
        throw er; // Unhandled 'error' event
              ^
Error: listen EADDRINUSE
    at errnoException (net.js:905:11)
    at Server._listen2 (net.js:1043:14)
    at listen (net.js:1065:10)
    at Server.listen (net.js:1139:5)
    at Object.<anonymous> (/Users/gabor/work/articles/code-maven/examples/node/hello_world.js:9:3)
    at Module._compile (module.js:456:26)
    at Object.Module._extensions..js (module.js:474:10)
    at Module.load (module.js:356:32)
    at Function.Module._load (module.js:312:12)
    at Function.Module.runMain (module.js:497:10)
```

It is lovely that it printed the "Listening ...." line on the console, but why did it crash?

It took me a while to figure out that I had another web server running and listening on port 8080 already.

I think it would have been much more useful if the exception included at least a hint about this being the problem.

Anyway, I changed the port number in `s.listen(8081);` and run the code again:

`node examples/node/hello_world.js`

It printed the following on the console and then waited.

```
Listening on http://127.0.0.1:8080/
```

But why does it say it is listening on port 8080 while I told it to listen on 8081?

Oh, of course, the number 8080 appeared in two places of the code, and I have changed only one.

This violates one of the cornerstones of programming called [DRY - Do Not Repeat Yourself](http://en.wikipedia.org/wiki/Don%27t_repeat_yourself).
It would be better to keep the port number in some variable, and then use that variable in both places.

The new code is almost the same:

{% include file="examples/node/hello_world_port.js" %}

We run this:

`node examples/node/hello_world_port.js`

If I open a browser now, and point it to http://127.0.0.1:8081/ it will show "Hello World".


