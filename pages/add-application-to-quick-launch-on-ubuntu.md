---
title: "Add application to quick lanuch in Ubuntu"
timestamp: 2021-01-13T12:30:01
tags:
  - Ubuntu
  - Desktop
published: true
author: szabgab
archive: true
show_related: true
---


You might have installed an application by downloading a zip file and unzipping it. Maybe into the <b>/opt/</b> directory.
How can you run it from the GUI of Ubuntu?


For example when I downloaded [Postman](https://www.postman.com/) I unzipped it to be in <b>/opt/Postman</b>.

I could run it from the terminal by typing in <b>/opt/Postman/Postman</b> but I wanted to run it from the Desktop GUI of Ubuntu.

So I created a file called <b>~/.local/share/applications/postman.desktop</b> with the following content:

{% include file="examples/postman.desktop" %}

Then ran

```
chmod 664 ~/.local/share/applications/postman.desktop
```

It was not that simple, I fought with this a bit, I even logged out and in a few times as that was suggestied on some place,
but I think that was not necesseary I just had to get the fields in the file right.

Now I can press the "Windows key" on my keyboard, start typing "post..." and I can launch the app.

When it is running I could go to the menu on the left-hand side, right-click on the Postman icon and click on <b>Add to Favorietes</b>
so it will stay in that menu even when I quit the application.
