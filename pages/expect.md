---
title: "What is Expect"
timestamp: 2015-10-05T08:30:01
tags:
  - Expect
published: true
author: szabgab
archive: true
---


[Expect](https://en.wikipedia.org/wiki/Expect) is tool to automate interaction with an application providing a CLI (Command Line Interface).
This can be anything you would type in on the command line and where you could C<expect> some answer.

Normally when you are using the command line you type in some command. That command prints out something.
You know that the command has finished by the appearance of the prompt. Then you know you can type in
something new to do something else. For example:


<h3>Local shell</h3>

```
air:data gabor$ ls -l
total 8
-rw-r--r--  1 gabor  staff  1999 Aug  3 07:45 feeds.url
air:data gabor$ 
```

In this case the prompt is `air:data gabor$`

<h3>Remote shell</h3>

You can use the same to execute commands on a remote machine via ssh. For this you'd type in `ssh server`
and (assuming you have public key authentication) you'd wait for the prompt of the other machine.

```
air:data gabor$ ssh server
Welcome to Ubuntu 14.04.3 LTS (GNU/Linux 4.1.0-x86_64-linode59 x86_64)

 * Documentation:  https://help.ubuntu.com/

0 packages can be updated.
0 updates are security updates.

Last login: Sun Oct  4 19:28:43 2015 from 102.13.217.111
gabor@server:~$ 
```

When accessing the remote server we will have to wait more time for the response. We will get all kind of output, but
we (people) know that we can start typing by the fact that the prompt we <b>expect</b> on the remote machine appears.

<h3>Remote shell with username/password</h3>

If I did not have public key authentication set up with the remote server, it would have asked me for my username and password:

The interaction would look something like this:

```
air:data gabor$ ssh server
Username: gabor
Password: *******
...
gabor@server:~$ 
```

Where 'gabor' and the text hidden by the stars was typed in by me. The ... represent the same text as we saw in the previous example.

So after typing in `ssh server`, how did I know I need to type in my password? What was I really <b>expecting</b> when I typed
in `ssh server`? I was expecting the text `Username:`. Then after I typed in my username and pressed ENTER, I was expecting
the text `Password:` to appear. Then once I typed in my password, I knew some text will appear, but I was really expecting the
remote prompt `gabor@server:~$`. That's what indicates me (a person) that I got in the remote machine and I can type in commands there.

<h3>CLI applications in general</h3>

In general every CLI application works the same way. We type in something. The applications does something and prints some response.
We will know that it has finished doing its job when a special string appears. In some cases this can be a 'standard' prompt.
In other cases it can be some random data.

<h3>bc as a CLI</h3>

You might know `bc` which is a command line calculator. Let's see an interaction with bc (running on the remote server):

```

gabor@server:~$ bc
bc 1.06.95
Copyright 1991-1994, 1997, 1998, 2000, 2004, 2006 Free Software Foundation, Inc.
This is free software with ABSOLUTELY NO WARRANTY.
For details type `warranty'. 
19+23
42
exit
0
quit
gabor@server:~$ 
```

I typed in `bc`. It printed out some "banner". After a while it stopped printing. Then I typed in `19+23` and pressed enter.
It printed 42. Then, when I wanted to leave the application I typed in `exit` and pressed ENTER. I was <b>expecting</b> to see the prompt
of my shell, but instead of that I saw 0. (Apparently you cannot exit bc by typing in `exit`.)
Then I typed in `quit` and pressed ENTER again. I knew I left the application when the prompt
`gabor@server:~$` appeared.

In this case, within the application, there was no prompt at all. The first time I knew I can type my math expression when the end of the banner appeared.
First time when I tried this I learned that it will print a banner ending with the word 'warranty'. From that point on I was <b>expecting</b>
this word. If it did not appear I'd be confused thinking there is some problem with `bc`.

Then I typed in `19+23`. This time, not knowing what the answer is going to be, I was <b>expecting</b> some number to appear.
Though I was not very surprised when it gave [the answer](https://en.wikipedia.org/wiki/Phrases_from_The_Hitchhiker's_Guide_to_the_Galaxy#The_number_42).

Then when I wanted to leave, at first time my expectation was not met.

## What if something goes wrong?

In the above interaction almost everything was perfect. Just as we <b>expected</b>. (Except when we typed in `exit` and it returned 0.)
In the real world however all kinds of things can go wrong and we have to handle those situations as well. For example what if we try to
access the remote server using `ssh` but the server is down or it is otherwise busy. The ssh client might quite and our own local shell
would print our local prompt without giving any error message. It might give some error message and then show the local prompt. Or it might just wait.
And wait. As humans, after a while we would conclude that the remote server is not responding, press Ctrl-C and leave `ssh`.

Even if the remote server works it can have several different responses when we try to access it. If we have the appropriate private-key/public-key pair
it will let us in and we'll see the remote banner and remote prompt. Otherwise it will prompt for a `Username:` and a `Password:`. 
In other cases it might assume the same username we have on our local system and prompt only for `Password:`.

When writing an automated script we'll have to make sure it can handle all these cases and probably all kinds of other cases I have not thought about.

## What is Expect then?

So `Expect` is a tool that will help us automate the interaction with any application that has a Command Line Interface (CLI).

There are a number of implementation of Expect in a number of programming languages. Their features and their usage differs from each other,
but in general they try to provide an easy automation of CLI apps.

* [Original expect in Tcl](http://www.nist.gov/el/msid/expect.cfm)
* [Expect in Perl](https://metacpan.org/pod/Expect)
* [pexpect in Python](https://github.com/pexpect/pexpect)
* Ruby rexpect</a>


