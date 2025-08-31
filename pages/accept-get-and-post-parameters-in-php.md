---
title: "Accept GET and POST parameters in PHP - use htmlspecialchars"
timestamp: 2018-04-02T16:30:01
tags:
  - $_GET
  - $_POST
  - htmlspecialchars
published: true
books:
  - php
author: szabgab
archive: true
---


Once we know how to [create output from our PHP code](/php-development-environment-on-centos) we also need to see how
to accept input.


In HTTP there are two ways to send parameters to the server. Using a `GET` method the parameters are in the URL after a `?` character. Using the `POST` the parameters are sent in the body of the request.

Accordingly PHP has two separate ways to access these parameters. Via the [$_GET](http://php.net/manual/en/reserved.variables.get.php) and [$_POST](http://php.net/manual/en/reserved.variables.post.php) variables.

## GET

In this example we have a small HTML snippet that makes the browser display an entry box and a button. In the opening of the `form` tag we explicitly said we would want the browser to use the `GET` method to send the parameters. We actually don't have to set this explicitly as this is also the default, but it is clearer this way.

After the HTML form there is a PHP snippet that takes a string and using the `.` concatenation operator, concatenates the value if the `$_GET` associative array for the the "person_name" key. We used this key as this is the "name" of the input field we are interested in.

{% include file="examples/php/get_params.php" %}

If we visit the page we see:

![](/img/php-echo-before.png)

That "Hello" at the bottom is there because our PHP code will run no matter what. So even when  `$_GET["person_name"]` it will still be displayed.

Once we type in our name ("Foo" in this case) and click on the "Echo" button, we will see that the page now shows "Hello Foo"
and we can also see as the parameters was passed in the URL that can be found in the address bar.

<img src="/img/php-echo-get.png"">

## What is htmlspecialchars

What is htmlspecialchars and why do we need it? The user can enter any characters in that form. For example the user can type in "&lt;Foo&gt;". If we printed the characters back as we have received them we would print back `&lt;Foo&gt;`. That however would be invisible as that looks like an unknown HTML tag.

Without htmlspecialchars it would look like this:

![](/img/php-echo-without-htmlspecialchars.png)

You can see the parameter in the URL, but not on the page.

If we clicked on "view source" for this page we would see:

![](/img/php-echo-without-htmlspecialchars-source.png)

As you can see in the source we see the text as we typed it in, but
that does not show up on the web page.

In order to make sure the browser can display every character as we typed them in
we need to call `htmlspecialchars` on every value we get from the users.


With htmlspecialchars it would look like this:

![](/img/php-echo-with-htmlspecialchars.png)

aka. What we expected.

Now if we look at the source of that page we'll see this:

![](/img/php-echo-with-htmlspecialchars-source.png)

We received back special strings that represent the less-than and greater-than characters
so our browser will know it has to display them instead of interpret them as HTML.

## POST

In order to see how the POST method works we changed the source code of our PHP file in two places from 
GET to POST. In the HTML form and in the variable name.

{% include file="examples/php/post_params.php" %}

If we look at the page with our browser it will look exactly the same as what we had when had GET there.
The difference can be seen after we typed in the name and clicked on "Echo".

The content of the page is still the same, but now the URL does not contain the parameters.

![](/img/php-echo-post.png)



