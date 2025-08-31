---
title: "JavaScript and jQuery on GitHub pages"
timestamp: 2018-06-19T17:30:01
tags:
  - Markdown
  - GitHub
  - JavaScript
  - jQuery
published: true
author: szabgab
archive: true
---


If you have just [started with GitHub pages](/getting-started-with-github-pages) you might be wondering how can you serve dynamic content. Well, you cannot really as the pages are static.
However this should not stop you from writing in JavaScript and ending up with a <b>Single Page Application</b>.

The first step in that direction is to see how to add JavaScript and jQuery to the pages.


Actually, after we went through some experimental steps it is quite straight forward. After all we can embed any HTML in our Markdown files so we can also embed <b>script</b>
tags. If this is enough for you, you can now go ahead and start adding JavaScript code to your pages.


## Step-by-step guide

If you are less of a JavaScript maven, then you might want to follow use step-by-step.

<h3>Embedded JavaScript</h3>

In the first example we create a Markdown file called `js.md` In that Markdown file we put an HTML `div` element with an id "text".
Later in that file we add a `script` tag and inside we write some simple JavaScript code. This code will locate the element that has the id "text", or `div`
element, and inside the element it will put the text that appears on the right-hand side of the assignment.

The main thing you need to remember here is that the JavaScript code must come at the end so by the time it is executed the DOM is ready. Otherwise the JavaScript code will not find the HTML element.

{% include file="examples/github/js.md" %}

<h3>jQuery loaded from external file</h3>

Our next step is to use [jQuery](http://jquery.com/) instead of vanilla JavaScript.
For this we only need to load jQuery from its CDN.
If we are already loading an external JavaScript file, I though we can also move our code to an external file.
So I created the `demo.js` file loaded it using another `script` tag.

This time we can put the `script` tags anywhere we like as the jQuery callback function will be only executed when the DOM is ready.
The only limitation is that we need to load our code <b>after</b> we have loaded jQuery itself.

{% include file="examples/github/jquery.md" %}

In our jQuery code we have an anonymous callback function that will be called when the HTML was loaded and the DOM is ready. That's what `$().ready` does.
Inside the function we use the `$("#text")` expression to locate the element with id "text" and then we use the `html` method to set the content of the element.
(It is the same as innerHTML in vanilla JavaScript.)

{% include file="examples/github/demo.js" %}

<h3>Loading JSON data from server</h3>

Finally, we would like to get some data from the server. As we cannot run anything on the server we cannot get dynamic data,
but we can store the data in JSON files and load them using the Ajax methods provided by jQuery.

In this example the Markup file is effectively the same as in our previous examples.

{% include file="examples/github/json.md" %}

In the jQuery code we use the `getJSON` method to fetch the `data.json` file from the server.
This means, first the HTML file that was generated from the Markdown file will be loaded. Then the browser will load jQuery followed by our code.
Then, once everything is ready, our code runs and loads the JSON file from the server.

The first parameter of `getJSON` is the URL of the JSON file we would like to load. The second parameter is an anonymous callback function that will be executed when we get the response from the server. Then the jQuery will call our anonymous function and it will pass the content of the JSON file after it was converted to a JavaScript object.

`console.log(data);` was only added for debugging.

In the last JQuery code, in `$("#text").html(data["text"]);` the first part `$("#text")` will locate the element with the id "text".
The `html` method will set the content of the element to the value we pass to it which in our case is `data["text"]`, the value of the "text" key that arrived from the JSON file.

{% include file="examples/github/json.js" %}

This is the `data.json`

{% include file="examples/github/data.json" %}

## Conclusion

Once you tried it and made it work, it seems to be quite straight forward to embed or include JavaScript and jQuery code.
We now need to turn to more complex tasks.


