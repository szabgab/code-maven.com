---
title: "Save content of clipboard to file in Ubuntu Linux"
timestamp: 2023-01-10T09:00:01
tags:
  - xclip
  - clipboard
published: true
author: szabgab
archive: true
show_related: true
---


I used Google Forms for a survey and wanted to save the generated graphs. They have a "copy" button that copies the graph to the clipboard.
I was not sure what is really in the clipboard and how to save it. After some search and experimenting I found this command to be working:


```
xclip -selection clipboard -t text/html -o > out.html
```

It saved the content of the clipboard the <b>out.html</b>. The format looked like this:

```
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAC...
```

So there is an <b>png</b> image in base64 format.

If we open the HTML file in a browser we can see the image.

