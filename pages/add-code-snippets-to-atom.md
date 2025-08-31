---
title: "Add code snippets to Atom - the text editor"
timestamp: 2015-06-03T14:30:01
tags:
  - Atom
published: true
books:
  - atom
author: szabgab
archive: true
---


Snippets are a great feature of any editor or IDE and in [Atom](https://atom.io/)
they are quite simple to use.


## How to use a snippet in Atom

In a file you start typing the "prefix" of an existing snippet.
Atom will show you a list of snippets that match the text you started to write.
If you stop typing you can select one of the entries using the up and down arrow.

<img src="/img/atom_snippet_use.png" alt="Atom snippets in use" />

When you press TAB or ENTER, Atom will insert the code snippet in the place where you started
to type.

There are many snippets that come with Atom pre-installed and you can easily create
your own snippets as well.

## Add your own snippet to Atom

You own snippets need to be defined in the `snippets.cson` file which is located
in your home directory. For me it was in the `~/.atom/` directory, though I don't
even have to know that, if I open the "Atom" menu, it has an entry to `Open Your Snippets`
that will open the `snippets.cson` in your favorite editor.

<img src="/img/atom_snippet_editor.png" alt="Atom menu to open snippet editor" />

In that file you need to add an entry like this


```
'.text.html':
  'HTML 5':
    'prefix': 'html'
    'body': '''
    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
        <title></title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/handlebars.js/3.0.3/handlebars.min.js"></script>
        <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>

        <link href="style.css" rel="stylesheet">
      </head>
      <body>

      </body>
    </html>
'''
```

This will work for html files.

The first string describes the 'scope' of where this will work.

Each file-type has a scope and each file extension is mapped to a scope.
Specifically the scope of the HTML files is `text.html.basic`
and the following extensions are considered HTML files:
`htm, html, kit, shtml, tmpl, tpl, xhtml`

I know this because I opened the `Settings` (Actually the `Atom / Preferences` menu option)
and among the `Packages` looked for the one handling HTML files. This is how it looks like:

<img src="img/atom_html_file_type.png" alt="HTML file type in Atom" />


## Comments

Exactly what I was looking for to bet a long ad code snippet working. Thanks..

---

How can i stop auto-complete to mess with my snippets? When i tab, it does code completation instead of my snippet! Is it possible to do bind it in another key?

---

Thank you! This was helpful. Do you know of a community site where snippet examples and shared? Maybe a github repo?

---

This was super-helpful! Thank you!!

