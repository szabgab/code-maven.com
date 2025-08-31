---
title: "HTTP Client request in Node.js (GET request and data from POST request)"
timestamp: 2015-02-03T09:30:01
tags:
  - http
  - request
  - GET
  - POST
published: true
books:
  - nodejs
author: szabgab
archive: true
---


When building a web application in raw Node.js you might use the [http](http://nodejs.org/api/http.html) class as we have
[started using Node.js](/getting-started-with-nodejs). Back then we only used the `response` object, but if we
are interested what the request was then we should also take a look at the `request` object we receive in the callback.


In this simple example of an `http server in Node.js` print out some of the values from the request object which is
an instance of the [http.ClientRequest](http://nodejs.org/api/http.html#http_class_http_clientrequest) class.

{% include file="examples/node/http_client_request.js" %}

I ran the above script using `node examples/node/http_client_request.js`
it printed `Browse to http://127.0.0.1:8081` so I browsed there
with my regular browser.

This is what was printed on the console:

```
GET
{ host: '127.0.0.1:8081',
  connection: 'keep-alive',
  'cache-control': 'max-age=0',
  accept: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36',
  'accept-encoding': 'gzip, deflate, sdch',
  'accept-language': 'en-US,en;q=0.8,he;q=0.6,ru;q=0.4' }
/
GET
{ host: '127.0.0.1:8081',
  connection: 'keep-alive',
  accept: '*/*',
  'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.94 Safari/537.36',
  'accept-encoding': 'gzip, deflate, sdch',
  'accept-language': 'en-US,en;q=0.8,he;q=0.6,ru;q=0.4' }
/favicon.ico
```

At first it confused me a bit, why do I have two GET request, but then I remembered, and looking more closely
I can also see it. The first request was indeed to `/`, (as you can above the second GET line), but then
another request was sent by my browser to the `/favicon.ico`. This is an automatic request my browser
send in the hope that it will be able to put this little image on the tab where I opened the page.

I don't want this extra confusion in my research, so I switched to the `curl` command that is available on Linux/Unix.

Let's start again:

I ran the server:

```
$ node examples/node/http_client_request.js 
Browse to http://127.0.0.1:8081
```

and opened another shell window where I sent my request:

```
$ curl http://127.0.0.1:8081/
```

Then switched back to the original console to see the response:

```
GET
{ 'user-agent': 'curl/7.37.1',
  host: '127.0.0.1:8081',
  accept: '*/*' }
/
```


From this point I was switching back-and-forth between the two consoles.

The second request included a path on the server and a parameter with a value:

```
$ curl http://127.0.0.1:8081/some/path?field=value
```

The printout on the other console was similar to the previous
printout, except of the last line that shows the `url`.

```
GET
{ 'user-agent': 'curl/7.37.1',
  host: '127.0.0.1:8081',
  accept: '*/*' }
/some/path?field=value
```


The last attempt was to send in a POST request using curl with some data:

```
$ curl --data "field=value" http://127.0.0.1:8081/
```


the output looked like this:

```
POST
{ 'user-agent': 'curl/7.37.1',
  host: '127.0.0.1:8081',
  accept: '*/*',
  'content-length': '11',
  'content-type': 'application/x-www-form-urlencoded' }
/
```

The first line shows that it was indeed a `POST` request,
the header had some extra fields, but the data itself was not included.

Of course, the data needs to be read in and processed in another way.

## Accepting HTTP POST request in Node.js

{% include file="examples/node/http_client_request_post.js" %}

This is another area where the non-blocking nature of Node.js is seen.
Instead of just reading the data from the request object we add a callback
method to the `data` event of the `request` object. This
will be called every time another piece of data arrives. Of course, if
all the data is only 11 characters as in our case, then this is not very
interesting, but if you are sending a lot of data then it is important
to read that in without blocking the rest of the site.

Now that we have a call-back waiting for data, we should finish our response
only after all that data has arrived. Hence  we also added a callback
for the `end` event of the `request` object and in that
callback we print to the console all the `data` that was sent by the client,
and finish our `response` by calling its `end` method.

Let's try this 

```
$ node examples/node/http_client_request_post.js 
Browse to http://127.0.0.1:8081
```

The regular GET request:

```
$ curl http://127.0.0.1:8081/
```

worked as earlier:

```
GET
{ 'user-agent': 'curl/7.37.1',
  host: '127.0.0.1:8081',
  accept: '*/*' }
/
```

the GET request with the path and the parameters:

```
$ curl http://127.0.0.1:8081/some/path?field=value
```

worked as well:

```
GET
{ 'user-agent': 'curl/7.37.1',
  host: '127.0.0.1:8081',
  accept: '*/*' }
/some/path?field=value
```

The question how does the `POST` request behave:

```
$ curl --data "field=value" http://127.0.0.1:8081/
```

and the result on the console is:

```
POST
{ 'user-agent': 'curl/7.37.1',
  host: '127.0.0.1:8081',
  accept: '*/*',
  'content-length': '11',
  'content-type': 'application/x-www-form-urlencoded' }
/
field=value
```

So indeed, this managed to collect the data that was sent by the client.


## Comments

Hi Gabor, It is actually a beautiful tuto, I really appreciate. But i would say, it is seem like to be a node http server tuto rather then a node http client.

<hr>

Its a great example to see how the legacy version of node consumed data. Thanks a lot

