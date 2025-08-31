---
title: "Docker course: getting help"
timestamp: 2022-11-07T15:41:01
tags:
  - Docker
types:
  - screencast
published: true
books:
  - docker
author: szabgab
archive: true
show_related: false
---


{% youtube id="m270lPL8eaw" file="english-docker-course-getting-help.mkv" %}

In order to [get help with Docker](https://code-maven.com/slides/docker/docker-help-cli) you can use the following
commands:

```
docker --help
docker help run
docker help ps
docker help images
docker help rm
docker help rmi
```

If you type in on the command line:

```
docker --help
```

then you will see a list of the command available for Docker. You might need to scroll-up to see the beginning of the output
or on Linux and OSX you could run it through `less`

```
docker --help 2| less
```


You can ask for help by typing `docker help` and then the name of one of the commands so `docker help rmi` for example
and then it gives you some kind of an explanation of what does the `rmi` command do.

You will find a lot more detailed documentation on the web site of the [documentation of Docker](https://docs.docker.com/).
There you can search using the name of the command and find all kinds of documents.
For example the [reference page if docker rmi](https://docs.docker.com/engine/reference/commandline/rmi/).

That's basically how to get help, though you can just search on your [favorite search engine](https://duckduckgo.com/)


