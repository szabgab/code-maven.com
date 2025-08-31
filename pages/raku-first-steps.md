---
title: "First impression with Raku"
timestamp: 2020-08-22T22:00:01
tags:
  - Raku
  - Rakudo
  - Docker
  - dir
  - shell
published: true
books:
  - raku
author: szabgab
archive: true
---


I think it is time I take a fresh look at [Raku](https://www.raku.org/).

I have some background with the language from several years ago, but I am sure it changed since then and in any case I'll try to newly explore it.



## Using Docker

I know Raku is rather new an I did not want to bother with installations, so I though I'll go the modern way and use [Docker](/docker).
For this to work first you need to [Download Docker Desktop](https://www.docker.com/get-started).

Then I can run the following:

```
$ docker run --rm -it rakudo-star
```

This will download (for the first time when I run this) the rakudo-star image and then run it. The `--rm` tells Docker to
remove the container once I am done with it. `-it` means to enter interactive mode.

## Interactive Hello World

The interactive mode immediately lands us inside the Raku interactive shell (aka. REPL) using a single greater-than sign as the prompt.
There I can type in:

```
> say "Hello World!"
```

and also

```
> "Hello World!".say
```

They both work.

Actually, because it is an interactive shell, it is enough to type in the string:

```
> "Hello World!"
```

## dir

I was not sure what to do next so I fell back to my Python background and typed ```dir</code>. (OK, I know that here I don't have to type in the parentheses for the function call to work.)

Actually I was surprised by the result:

```
> dir
("mnt".IO "bin".IO "proc".IO "sbin".IO "tmp".IO "usr".IO "media".IO "lib".IO "opt".IO "srv".IO "lib64".IO "etc".IO "root".IO "home".IO "var".IO "sys".IO "dev".IO "boot".IO "run".IO ".dockerenv".IO)
```

This is the content of the root directory of the Docker container.

## shell

I am not sure what was I thinking but then I also tried to call `shell` and it worked!

```
shell("ls -l")
```

## help

At this point I ran out ideas so I tried typing in `help`

```
===SORRY!=== Error while compiling:
Undeclared routine:
    help used at line 1
```

I guess there is no excuse. I'll have to find a tutorial and some documentation.

## Version

Then I quite the interactive shell by typing `exit`.

```
$ docker run --rm rakudo-star raku -v
This is Rakudo version 2020.01 built on MoarVM version 2020.01.1
implementing Perl 6.d.
```

Hmm, that seems to be a bit old. I was under the impression that Rakudo Star is released every 3 months. I guess I was mistaken.

## Hello World on the command line

```
$ docker run --rm rakudo-star raku -e 'say "Hello World!"'
```

## Hello World in a file

I've created a file called <b>hello_world.raku</b>:

{% include file="examples/raku/hello_world.raku" %}

Then ran it as:

```
docker run --rm -v $(pwd):/opt rakudo-star raku /opt/hello_world.raku
```

The `-v $(pwd):/opt` parameter tells Docker to map the current directory on my own computer
to the `/opt` directory inside the Docker image. Then on the command line I passed in

```
raku /opt/hello_world.raku
```

That will execute the given file and I got:

```
Hello World
Hello Raku
```

Great, so things are working quite smoothly. It is time to dig out my old course material and see what still works and
what I need to improve.

If you are interested in Docker I have a [Docker course](/docker)

