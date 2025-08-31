---
title: "Static Site Generator"
timestamp: 2023-01-29T11:30:01
tags:
  - Exercises
description: "Create a Static Site Generator. It is easy and fun."
published: true
author: szabgab
archive: true
show_related: true
---


There are plenty of Static Site Generator (SSGs) already, but it is also a fun project to implement as an exercise.


A few of the most popular SSGs are
* [Jekyll](https://jekyllrb.com/) written in Ruby
* [Hugo](https://gohugo.io/) written in Go
* [Docusaurus](https://docusaurus.io/)

Jamstack has a [collection of 347 SSGs](https://jamstack.org/generators/) with various details categorized by language.

## Description

<b>Version 1</b>: The user writes Markdown files and the proccsor generates HTML pages.

<b>Version 2</b>: The Markdown files can have some meta data at the top of the file. E.g called "front matter" Similar to what [DEV.to](https://dev.to/) allows.

Start implementing one of the fields and then one-by-one add the additional fields.

```
---
title: The title of the post
published: false
author: Name of the author
description: A short description of the article.
tags: some, words, or, even, multi word expressions
published_at: 2023-01-29T11:30:01
series: some-name
---

Here comes the content of the article.
```

This information is displayed on the web page.

The <b>title</b> is going to be both the HTML <b>title</b> tag in the head and the <b>h1</b> element of the page.

The articles that have <b>published: true</b> are actually published. The ones that have <b>published: false</b> are considered drafts.

The <b>published_at</b> field can be used to create a page listing all the articles in the order the were published.

The generated front page could display the 3 most recently published articles.

The <b>description</b> can be the content of the HTML <b>meta</b> tag called <b>description</b>. (Look at the source of the current page.)

The <b>tags</b> can be used to crete pages, eg. <b>t/some</b> listing all the articles that have the same tag. There can also be a page called <b>/tags</b> listing all the tags and the number of articles with that tag.

<b>Version 3</b>:

Add a config file e.g. <b>config.yaml</b> that will contain some configuration information about the whole site. e.g.

```
title: The title of the site (on the main page)
front_limit: 3    (The number of articles to show on the front page)
```

<b>Version 4</b>:

Find other interesting features of the other processors list above.


