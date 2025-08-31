---
title: "Ajax request for JSON data with vanilla JavaScript"
timestamp: 2015-03-31T16:00:01
tags:
  - XMLHttpRequest
  - JSON.parse
published: true
books:
  - javascript
author: szabgab
archive: true
---


One of the cornerstones of modern web application is the behind-the-scenes, asynchronous data communication between
the server and the JavaScript code running in the browsers. While in Ajax, the X stands for XML, in reality many applications
send data formatted as JSON. In most cases it is more convenient than sending XML.


In order to make this example simple, I've created a JSON file on the server and we will ask the server for that file.
In more real world situation, the server would generate this JSON file on-demand based on information in its database,
but currently we are only interested in the part that is in the browser.

{% include file="examples/js/data.json" %}

We have an HTML page, with an `h1` element we are going to fill with the value of the "title" key, and we also
have a `div` element for which we'll construct a whole HTML snippet.

{% include file="examples/js/ajax.html" %}

[view](examples/js/ajax.html)

The JavaScript code looks like this:

{% include file="examples/js/ajax.js" %}

All the code that is relevant to sending the asynchronous request was placed in a function called `ajax_get`.
This function expects two parameters. The first one is the URL we request. It can be a URL like `http://somesite.com/some/page`,
or it can be without the hostname just `/some/page` if we want to send the request to the same server where our JavaScript
code came from. In either case we can also send parameters by attaching them after the requested URL. Something like this:
`http://somesite.com/some/page?fname=Foo&lname=Bar`

The second parameter is expected to be a function which will be called when the response arrives from the server.

In our example we expect the response to be a valid JSON string.

Just to quickly go over the function: First we create an `XMLHttpRequest()` object. Then we attach a function
call to `onreadystatechange` attribute of the object. This function will be executed when the successful response arrives.
Then we call `open`, this is where we use the `url` and finally we `send` the request. This will finish our function
call and our application can go on doing its business until...

Until the server responds, at which point the function that was attached to `onreadystatechange` will be called.
Inside the function we check if this was really a successful request and then we look at the `responseText` attribute
that will contain the response as plain text. In this example we paste it to the console, just to make it easier to see
what do we get back. Then there is the `try-catch` block wrapping the call to `JSON.parse`.
This can save you quite some time if and when the server returns a string that is not properly formatted JSON string.
(For example an extra or a missing comma.) Then comes the interesting part `callback(data)` we call the function
`ajax_get` got as the second parameter and we pass the data to it already as a JavaScript object.

That's about the implementation of the `ajax_get` function, but how should we use it?

```javascript
ajax_get('/try/examples/js/data.json', function(data) {
    document.getElementById("title").innerHTML = data["title"];
});
```

We call the `ajax_get`, pass to it a url (in this example relative to the current server), and we also pass
a function that accepts a single variable. This is the callback function and the parameter will have the
data we received from the server. Then we can access attributes of this JavaScript object as we access any other JavaScript object
and we set the `innerHTML` of the HTML element with the id "title".

That's how we can use the ajax request.

## Building up the HTML

In our example code we have a longer function though. After setting the title element, there is a demonstration on how
to create and html string from various parts of this data object. This is not really necessary for this example, but
I am going to use this opportunity to show a more convincing reason to use Handlebars that I had in the
[introduction to Handlebars](/introduction-to-handlebars-javascript-templating-system)

## Comments

Awesome

---

how do you fetch and render the entire json file content instead of fetching individual element values? i was thinking about something like below...

document.getElementById("TEXTAREA_ID").innerHTML = `${data}`;

but it doesnt work...
---
Cross-Origin Request Blocked: The Same Origin Policy disallows reading the remote resource at https://www.google.fr/. (Reason: CORS header ‘Access-Control-Allow-Origin’ missing).

---

why xmlhttp.readyState == 4, and xmlhttp.status == 200 ?

---

Good Question, see here https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/readyState

This should give you an idea why.

