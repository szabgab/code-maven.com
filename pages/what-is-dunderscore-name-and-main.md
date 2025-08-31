---
title: "What does "if __name__ == '__main__'" do in Python?"
timestamp: 2022-12-07T18:30:01
tags:
  - __name__
  - __main__
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


You might have seen the following code snippet in many Python files and wondered what does that do and why would you need it?

{% include file="examples/python/name_main.py" %}

In a nutshell it allows a file to be used both as a stand-alone program (script) and as a module imported by some other stand-alone program.

Let's see the explanation.


## Loading a file as a module

A little background:

Let's say we have the following two files:

{% include file="examples/python/name_main1/mylib.py" %}

{% include file="examples/python/name_main1/myscript.py" %}

If we run

```
python mylib.py
```

it will print

```
In mylib
```.

This is not surprising we told it to do just that.

If we run

```
python myscript.py
```

it will print

```
In mylib
In myscript
```

This is probably not what we wanted. The print of the imported module was executed and it was executed before the print of our script.
Usually we don't expect anything to happen while we import modules. Definitely nothing to be printed to the screen.

It happened, because when Python imports a file (a module) it executes it at the time of import which means any code <b>outside</b> of
functions will be executed.

It is very rare that in module that we import there is any code outside of functions. So the better approach to write a module would be this:

## Having only functions in modules

{% include file="examples/python/name_main2/mylib.py" %}

{% include file="examples/python/name_main2/myscript1.py" %}

{% include file="examples/python/name_main2/myscript2.py" %}

Now we have two functions in our <b>mylib.py</b> file. One of them is the <b>display</b> function we would like to use
and the the other is the <b>destroy_harddisk</b> that you would probably not want to execute. I have not even implemented
it to make sure no one will run it and then come complaining.

If we run the first script

```
python myscript1.py
```

we only see

```
In myscript
```

This is not surprising as now, even though we imported the <b>mylib</b> module, we did not call any of its functions.

n order to see the text from the <b>display</b> function we need to call it:

If we run the second script

```
python myscript2.py
```

we see

```
In myscript
In mylib
```

This time the content of <b>mylib.py display</b> function is printed at the time when it is called.

However if we now run

```
python mylib.py
```

There is no out. So in order to facilitate the needs of the scripts that import the <b>mylib.py</b> we changed the behavior of the <b>mylib.py</b>
and "ruined" it.

What we would really like is to see the output of the <b>display</b> function when execute <b>python mylib.py</b>.


## Make both cases work

This is where the expression comes in handy.

{% include file="examples/python/name_main3/mylib.py" %}

{% include file="examples/python/name_main3/myscript1.py" %}

{% include file="examples/python/name_main3/myscript2.py" %}

Now if we run

```
$ python mylib.py
```

We get

```
In mylib
```

just as we got in the first case, and if we run <b>python myscript1.py</b> or <b>python myscript2.py</b> that will act as that did in the second case.

So now we have a file (mylib.py) that can be used both as a module and as a stand-alone program (script).

## How does __name__ == "__main__" work?

Let's take the first example and make it print the content of the variable `__name__`.

{% include file="examples/python/name_main4/mylib.py" %}

{% include file="examples/python/name_main4/myscript.py" %}


Running mylib:

```
python mylib.py
```

We get:

```
In mylib __name__='__main__'
```

So when you run the file as a stand-alone program the variable <b>__name__</b> contains the strange string <b>__main__</b>.

What if we run the program / script?

```
python myscript.py
```

We get the following:

```
In mylib __name__='mylib'
In myscript __name__='__main__'
```

Now we have two different variables called <b>__name__</b>. One of them in the file <b>mylib.py</b>. There it contains <b>mylib</b>
and one in <b>myscript.py</b> that contains <b>__main</b>.

Our focus should be the fact that the content of the variable in <b>mylib.py</b> depends on how it was used. When we used it
as a stand-alone script it had <b>__main__</b> in it and when we imported it as a module then it had <b>mylib</b> (the name of the file without the extension)
in it.

Now if you go back to the 3rd example to the code we are trying to understand that you can also see here:

{% include file="examples/python/name_main.py" %}

The condition checks the content of the <b>__name__</b> variable and calls the <b>display()</b> function
only if it contain <b>__main__</b> meaning that the file was used as a stand-alone program.

## When to use it?

Now that we know what does it do and how does it work, let's ask the question when to use it?

The answer is that it is actually rarely needed.

It can be used to allow a module to be self-testing so we would run the tests of the file when it is executed as a stand-alone program.
However these days it is much more common to put our tests in separate files and even if we include documents that need to be verified using
<b>doctest</b>, <b>pytest</b> can execute those without this construct.

It can be used to make a module also a stand-alone script, but it seems like a bad engineering practice that will backfire.

However it <b>must be used</b> when you use <b>multiprocessing</b> on Windows because that module works by loading your main script as a module.

There might be some other cases as well when it is useful or even required, but I think in general it is needed a lot less than it is actually used.

