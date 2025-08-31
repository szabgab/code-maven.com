---
title: "Nano the simplest editor for Linux"
timestamp: 2018-03-11T13:30:01
tags:
  - nano
  - ls
  - cat
published: true
books:
  - linux
author: szabgab
archive: true
---


If you are serious about working on Linux, especially as a system administrator or DevOps engineer then you'd better
learn [vim](https://www.vim.org/) as that is the power editor on Linux. However it has a long and rather steep learning
curve. If you are just getting started with Linux on the command line I'd recommend you first start using Nano, a much simpler
editor that comes installed with Ubuntu and probably with other distributons as well.


I assume you have logged in and you see the prompt:

![](/img/vb1/linux_login_1.png)

## Create file with Nano

Type in:

```
$ nano hello.txt
```

This will open a text editor in the terminal showing some control options at the bottom:

![](/img/vb1/nano-1.png)

Type in some text. e.g.

```
Hello World!
How are You?
```

In order to save the document click on `Ctrl-o` (See "Write Out" at the bottom of the screen.)
It will offer to write the content with the name "hello.txt".

![](/img/vb1/nano-2.png)

Press ENTER.

The file is now saved. We can quit Nano.
Press `Ctrl-X` (see at the bottom for the key-bindings).

This will bring us back to the prompt. We can now list the content of the directory using `ls`.
You'll see something like this:

![](/img/vb1/nano-3.png)

We can also display the content of the file using the `cat` command:

![](/img/vb1/nano-4.png)

The same way you can edit any other file.

## Edit file

You can also edit an existing file.

Just type in

```
$ nano hello.txt
```

again and you'll be back in the editor.


## Exercises

Play around with the editor.

* Create a new file.
* Edit an existing file.
* Exit and check with `cat` that the changes were saved.
* Edit and existing file, make some changes, but exit without saving. Verify (using cat) that the changes were not saved.
* Cut and Paste a line of text. (Paste = Uncut in Nano)
* Search for some text in the document.

