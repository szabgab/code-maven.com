---
title: "Creating a file on a mounted volume in Docker as the external user (and not as root)"
timestamp: 2023-04-26T21:00:01
tags:
  - Docker
published: true
books:
  - docker
author: szabgab
archive: true
show_related: true
---


For a long time I had this problem that I did not know how to solve:

When you run Docker on a linux host, mount an external folder, all the files created in the docker will be owned by user <b>root</b> on the host file-system.

Finally I think I understood how this works and found a solution. At least a partial solution for Ubuntu and CentOS-based images.


## The Problem

Here is the problem again:

I run docker and mount the current folder as /opt inside the container:

```
$ docker run -it --rm -w /opt -v$(pwd):/opt ubuntu:23.04 bash
```

When inside the container I create a file and then exit the container:

```
# touch hello
# exit
```

If I look at the ownership of the file on my host computer (which is also Ubuntu):

```
$ ls -l hello
```

I get:

```
-rw-r--r-- 1 root root 0 Apr 26 20:35 hello
```

The file is now owned by user <b>root</b>.

## Solution

Add the <b>--user ubuntu</b> parameter to the command:

```
$ docker run -it --rm -w /opt -v$(pwd):/opt --user ubuntu ubuntu:23.04 bash
```

Inside the container create a file and exit:

```
$ touch world
$ exit
```

Outside, on the host, check the ownership:

```
$ ls -l world
-rw-r--r-- 1 gabor gabor 0 Apr 26 20:38 world
```

It is now owned by <b>gabor</b> which is my regular user.

## Explanation

In Linux each user has a user id. The user <b>root</b> has the id 0 on every Linux machine and I guess also on macOS, but I have not checked it.
So both on my host computer and inside the Docker container the user <b>root</b> has the same id.

When I ran docker in the first example (without passing the <b>--user</b> parameter), inside the container I became user <b>root</b>.
Any file I created then got the userID 0 as its owner. This is also the user <b>root</b> outside, so that's why the file is owned by
root on the host system.

The first real user on Ubuntu (and I think in general on every Linux and Unix system) will get the id 1000. So the user ID of my
user "gabor" on my host computer has the ID 1000. I could verify this by running the <b>id</b> command on my computer.

The Docker image 23.04 also comes with a default real user account which is called <b>ubuntu</b> and it also has the ID 1000.
When in the 2nd example I used the <b>--user ubuntu</b> flag I entered the container as user <b>ubuntu</b>. If I ran the <b>id</b> command there
I'd see:

```
$ id
uid=1000(ubuntu) gid=1000(ubuntu) groups=1000(ubuntu),4(adm),20(dialout),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev)
```

showing that this user in the container also has the ID 1000.

I found out about this by listing all the users using the <b>cat /etc/passwd</b> command. It is the last row.

So when I created a file on the mounted volume the file was created as user ubuntu (id 1000) inside the container.
However on my host machine that id belongs to my regular user, so my computer sees that file as own by user gabor (id 1000).

Just as if I created it as my regular user on the host computer.

This solves the problem.

## Notes and warnings

If on the host system your ID is not 1000, then this will not work, but you can create a user in the container with the ID you have
and use that username. (See below for CentOs.)

Now that inside the container I am user <b>ubuntu</b> I don't have the privileges of user <b>root</b> so I cannot make changes
to any of the system files. In particular I cannot install any extra software using <b>apt</b>. However, there are at least two ways to solve that.
See [Docker as both a regular user and as root (with and without sudo)](/docker-as-regular-user-and-as-root).

## CentOS

After a little pause I though I'll try CentOS as well.

I ran

```
$ docker run -it --rm -w /opt -v$(pwd):/opt  centos:7 bash
```

and then inside the container

```
# cat /etc/passwd
```

This showed that all the user IDs are below 1000, they are all system-related users. So I need to create a user.

I created a </b>Dockerfile</b> with the following content:

```
FROM centos:7
RUN useradd centos
```

That RUN command will create a user with the username <b>centos</b>:

Built my own images:

```
$ docker build -t mycentos .
```

Ran docker using that images:

```
$ docker run -it --rm -w /opt -v$(pwd):/opt --user centos mycentos bash
```

Inside the containe I first checked the id then created a file, then exited:

```
$ id
$ cat /etc/passwd
$ exit
```


Outside I checked:

```
$ ls -l cent
-rw-rw-r-- 1 gabor gabor 0 Apr 26 22:26 cent
```

It looks fine.

## Conclusion

On Ubuntu there is already a user called <b>ubuntu</b>, on CentOS there is no user, but we can create one easily.
I assume on any other image you would either already had a user or you could create one.

