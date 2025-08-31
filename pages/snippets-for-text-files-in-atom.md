---
title: "Snippets for text files in Atom - the text editor"
timestamp: 2015-06-03T13:30:01
tags:
  - Atom
published: true
books:
  - atom
author: szabgab
archive: true
---


Plain text files, with an extension of `txt` have a scope `text.plain` in the configuration
of the Atom editor.


If you'd like to create a snippet, you need to put it in the `text.plain` as in the next example:

```
'.text.plain':
  'Copyright information':
    'prefix': 'copyright'
    'body' : 'Copyright (c) 2015 Foo Bar'
```

The second line is the human readable description of the snippet.
On the 3rd line we define the "prefix" that will trigger the snippet.
The 4th line shows the content of the snippet. The string that eventually needs to be inserted.

## Multiple snippets for text files

If you'd like to add another snippet in the same scope, you should include it within the same tree:

```
'.text.plain':
  'Copyright information':
    'prefix': 'copyright'
    'body' : 'Copyright (c) 2015 Foo Bar'

  'x.y.z.':
    'prefix': 'xyz'
    'body' : 'add x and y and z'
```

Now you can type either 'copyright' or 'xyz' and invoke the respective snippet.


## Multiline snipptes

If you'd like to have a snippet insert more than one line, you need to use 'raw'
strings with triple-quotes. For example like in the next snippet:


```
'.text.plain':
  'xyz':
    'prefix': 'xyz'
    'body' : '''
    add x
    and y
    and z
    '''
```
