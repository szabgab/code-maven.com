---
title: "Docker course: container vs. image"
timestamp: 2022-10-02T09:03:01
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


{% youtube id="OIWd6jZrYBc" file="/english-docker-course-container-vs-images" %}

Welcome back to the Code-Maven Docker course.

In this video we are going to learn about the difference between <b>Docker containers</b> and <b>Docker images</b>.

When people are talking about Docker, they usually use word container, but there are basically two main things: containers and images.

They are very similar, but slightly different.

The [slides](https://code-maven.com/slides/docker/) as usual and jumping right to the current slide:
[Docker container vs. image](https://code-maven.com/slides/docker/docker-container-image).

So the big difference, or the way you could express this is basically that they are the same thing in different phases in their life.

<b>A container can be seen as the run-time version of an image.</b>

So when you create something, at the end you create an image and you store it on the disk and when you use it, it becomes a container.
It is called a container.

So basically just like a Linux image, like an ISO file, for a Virtual Machine and that's frozen, you can save it on the disk
and then when you start running it, it becomes a container.

It's a copy of the image, but when it is running.

If you are thinking in programming terms then some people like to compare it to the class and the instance.
In Python it is the class object and the instance object in other languages it's class and instance.

The class is the definition of the things, and the instance is what being used during the runtime.
So this is sort of the same with containers and images.

If it wasn't clear now, that's ok. You can come back and understand it later and I am sure as we go along
it will be clearer, much clearer later on.

So thank you for listening and goto the next video.





