---
title: "Building a web client (a crawler) using Node.js"
timestamp: 2015-02-11T21:30:01
tags:
  - http
  - http.get
published: true
books:
  - nodejs
  - javascript
author: szabgab
archive: true
---


Building a web server, or a web application, as we have started in the [first example](/getting-started-with-nodejs) can be interesting,
but so is building a web crawler. You know, the thing that downloads pages, and does something interesting with them.

Let's start with something simple.


The [http](http://nodejs.org/api/http.html) class we have seen earlier provides several methods for this.
We are going to look at the [http.get](http://nodejs.org/api/http.html#http_http_get_options_callback) method
that provides a simple even if limited interface.

{% include file="examples/node/crawl_01.js" %}

The first part of the code is just checking if the user has supplied a URL
[on the command line](/argv-raw-command-line-arguments-in-nodejs).

Then once we have `url` we call `http.get` providing the requested url and a callback.
That callback will be executed with a [response object](http://nodejs.org/api/http.html#http_class_http_serverresponse).

Let's see this script with various parameters.

Actually, let's start without any command line parameter:

```
$ node crawl_01.js 
Usage: /Users/gabor/work/articles/code-maven/examples/node/crawl_01.js URL
```

OK, so it tells us we need to supply a URL

```
$ node crawl_01.js http://code-maven.com/
Got response: 200
```

That looks good.

Let's ask for a page that does not exist:
```
$ node crawl_01.js http://code-maven.com/x
Got response: 404
```

That looks correct, we got a [http 404](http://en.wikipedia.org/wiki/HTTP_404) as expected, but then, oh.
It got stuck. No matter how long I waited it would not end the script.
Well, actually after a minute or so, it stopped, but I only noticed this because I went to prepare a tea for myself.
This is not what we want, is it?

At first I thought this is some problem with my server so I tried something else:

```
$ time node crawl_01.js http://google.com/
Got response: 302
```

The [http 302](http://en.wikipedia.org/wiki/HTTP_302) seems ok, but after that the script got stuck as well.

So the problem is not in my server.
I was not sure how to solve this so I decided to move on. After all, when we get a successful response, we still would like to get the content of
the request. Being everything asynchronous, the content has not necessarily arrived yet when the callback was executed.
We need to use the `response object` and add some code to consume the data received.

## Consuming the data

{% include file="examples/node/crawl_02.js" %}

Once a connection was established and the server gave some response, Node.js executed the callback function passing
an object representing the response. This can be found in the `res` variable.

We attached two callbacks to this object.  `res.on('data', function(chunk) { ... ` will be called
every time a chunk of the data sent by the server arrives. If the page was small this might be happen at once,
but if the page is large, it might take some time (even a few seconds?) to get all the data. In the meantime
we can do something else. So this function will be called every time some more data has
arrived. The parameter passed to the function will contain the current chunk of data.

We have created a variable called `content` and will append the current chunk to this variable.

Of course we assume here that the size of the page fits in the memory, which is quite a reasonable assumption
for an html page.

The second callback is attached to the event when the responses has finished consuming all the data:
`res.on('end', function() { ...`

Without this could not be sure if we have received all the data the server wanted to send.
We just print 'end' to the console and we print the size of the `content` we have received from the server.

Let's run this script now:

```
$ node crawl_02.js http://code-maven.com/
Got response: 200
end
20558
```

So the front page of the [Code Maven](/) site has 20,558 bytes.

```
$ node crawl_02.js https://perlmaven.com/
Got response: 200
end
18487
```

Apparently the front page of the [Perl Maven](https://perlmaven.com/) site is smaller.

What about the pages that got stuck?

```
$ node crawl_02.js http://code-maven.com/x
Got response: 404
end
7641
```

And it is not stuck any more!

```
$ node crawl_02.js http://google.com/
Got response: 302
end
261
```

And this was not stuck either.

Apparently, earlier, the script was still expecting us to consume the response and that's the reason
it was waiting till some timeout happened. Though now it is unclear to me why was it not stuck when
we got 200 response.

## Is it really chunk-by-chunk?

There are two lines commented out in the script. If we remove the `//` from the first one,
enable `console.log('chunk ' + chunk.length);` and run the script again:

```
$ node crawl_02.js http://code-maven.com/
Got response: 200
chunk 1235
chunk 12672
chunk 1408
chunk 1408
chunk 1408
chunk 1408
chunk 1026
end
20558
```

we can see that we get the data in several pieces.

## The content of 302

If we remove the second pair of `//`, enabling `console.log(content);`
then we'll see the content of the page.

For example:

```
$ node crawl_02.js http://google.com/
Got response: 302
chunk 261
end
261
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>302 Moved</TITLE></HEAD><BODY>
<H1>302 Moved</H1>
The document has moved
<A HREF="http://www.google.co.il/?gfe_rd=cr&amp;ei=abcdVK1234GG8Qftxx1234">here</A>.
</BODY></HTML>
```

Goole.com is redirecting to the local chapter of Google.

## Conclusion

This is a good start for a crawler, but we have a lot more to do, and there are actually a few,
crawlers written in Node.js that provide higher abstraction.

## Advanced crawlers

For more advanced crawlers we'll have to look at one of the following projects:
[node-simplecrawler](https://github.com/cgiffard/node-simplecrawler),
[node-crawler](https://github.com/sylvinus/node-crawler), and
[spider](https://github.com/mikeal/spider).


