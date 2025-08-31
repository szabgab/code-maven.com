---
title: "tmux a terminal multiplexer"
timestamp: 2018-09-16T07:30:01
tags:
  - tmux
published: true
author: szabgab
archive: true
---


`tmux` is great to keep a session on a remote computer alive even when you get disconnected because of a network failure
or because you need to move from one network access point to another.

The interactive process you ran on the remote machine keeps running.

The editor you opened on the remote machine stays open. Even if you are in the middle of a cut-and-paste,
when the connection is lost, you can still reconnect and you don't lose anything.

It can provide you with multiple buffers and split-windows to do more than one operation at the same time via a single
`ssh` connection.

Here is my modest configuration file and some command I use.


## My Configuration file

{% include file="examples/tmux.conf" %}

## Start using

* ssh to remote machine (use Putty if your desktop runs Windows)
* Save the above file in `~/.tmux.conf`
* Install `tmux` if it is not installed yet. e.g. `sudo apt-get install tmux`

* Start tmux by running `tmux`
* `Ctrl-a Ctrl-d` - detach from the tmux session (then you can close your ssh session with `Ctrl-d` keeping the tmux session alive
* Next time when you connect to the server, run `tmux a` to attach to the existing session

## Buffers

* `Ctrl-a c`    Create another buffer
* `Ctrl-a 0`    Jump to buffer 0
* `Ctrl-a 1`    Jump to buffer 1
* ...
* `Ctrl-a ,`    Set the name of the buffer
* `Ctrl-a w`    Select buffer (list view)
* `Ctrl-a s`    Select buffer (tree view)
* `Ctrl-a f`    Select buffer search (ENTER on empty search to see full list)
* `Ctrl-d` or `exit` will close the buffer

## Windows

Each buffer can be split up into windows.

* `Ctrl-a "` Split window vertically
* `Ctrl-a %` Split window horizontally
* `Ctrl-a (arrows)` switch to another window
* `Ctrl-a x` Close current window


## Ctrl-a
* `Ctrl-a Ctrl-a` is a `Ctrl-a` (jump to the beginning of the line)


## Help

* `Ctrl-a ?` list keyboard binding. The `bind-key` is Ctrl-b by default but we have configured it to be `Ctrl-a`.
* `ESC ESC` pressed twice will leave the help window
* `Ctrl-s` Search in help window

## Multiple sessions

I never needed to run two `tmux` session on the same remote machine, but sometimes I forgot that I already have one running and instead of using `tmux a` to attache to an existing one I ran `tmux` that created a new one.

If I recognize it immediately I can just quit it (e.g. with `Ctrl-d`) and then get into my regular session.

If, however I start working and get disconnected, when I reconnect I might want to decide which one to connect to.

From the outside (after `ssh` connection was established, but before you attach to `tmux`, you can run:
`tmux list-sessions` that will, well, list the sessions.

```
0: 1 windows (created Mon Jul 23 04:52:55 2018) [135x61]
3: 1 windows (created Mon Sep 17 04:27:08 2018) [135x61]
```

Then you can attach yourself to any of the existing session:

`tmux a -t 0`

## Copy Paste in tmux

See the article about [select-copy-paste in tmux](http://www.rushiagr.com/blog/2016/06/16/everything-you-need-to-know-about-tmux-copy-pasting-ubuntu/).

## Comments

One of my favorite features of tmux that you did not mention is the `copy-mode` that makes you interact with the terminal history as if you were in an editor. You can search backwards, select and copy, and then paste into the same window/pane or in a different window. Much faster than using a mouse.

---

How do you do that?

---

See e.g.: http://www.rushiagr.com/blog/2016/06/16/everything-you-need-to-know-about-tmux-copy-pasting-ubuntu/

But basically you just enter it by «Hotkey»[ and you can then traverse the buffer in readonly mode, search it, mark it, and copy it into the tmux copy buffer. You can then paste from the tmux copy buffer (e.g. in another pane or window) with through «Hotkey»] .
