---
title: "Docker course: Why use Docker?"
timestamp: 2022-09-30T08:01:01
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


{% youtube id="CLr_VFMZf7E" file="/english-docker-course-why-use-docker" %}

Hello and welcome back to the Code-Maven Docker course. My name is Gabor Szabo.

In this episode we are going to ask the question <b>Why to use Docker at all?</b>

Remember this is the place where you can find the [slides](https://code-maven.com/slides/docker/)
and I ma going directly to the page where we are discussing [Why to use Docker?](https://code-maven.com/slides/docker/why-use-docker).

One of the biggest problems that software development encounters is the different types of environments where we run our software.

So there are the developers who develop the application on some desktop system which is usually either Windows or Mac. Sometimes Linux, but usually
it is either Windows or Mac and then there might be some QA people who are checking the software - Quality Assurance (QA) and they might install
it on some environment which might resemble more the actual production environment, but it's still different from the production environment.
Which is probably some Linux server somewhere in the cloud and which has different capabilities.

The Operating System is different of course, the computers have different capabilities, have different rights, different rights to transfer data and so on.

So these differences make it really hard to make sure that the software that was running on the developer's machine will actually behave well
on the production server as well.

In addition there is what we usually call the "<b>dependency hell</b>". An application depends on something and then another part of the same application
depends on the same thing, but might depend on a different version of that thing. So there is a common library let's say.

How can you run these two parts of the application on the very same server?

So this issue is really, really difficult. One of the solutions is of course to force everyone to use the same exact version, but that
usually means that people use the old version of something.
A much better way is to use some kind of a virtualization like Docker that allows that allows us to separate the various parts of the application
and each application (each part) can declare and use its own dependencies and can move forward with the dependencies as they feel fit. At their speed.
So that's another thing.

And the third thing that's really hard in many development companies or many companies is what we call on-boarding of new employees or new developers.

In a reasonably large application to set up an environment, a development environment, might take days or weeks even and it might have been documented,
maybe people need to go around and ask other people how to setup things and usually most of the people who get in these companies they will have a long
long time, maybe months or years till they figure out all kinds of issues that don't work on their environment because they did not set it up the
way it should have been set up. Or the ways other set up.

Docker, or in general virtualization can help us solve all of these problems. So the question of on-boarding.

So Docker and in general containerization or virtualization, but specifically Docker can allow us to create a standard environment
in which we develop the code, check the code (quality assurance), and deploy the code. And then the differences, well they won't disappear,
but they will be much smaller.

The same with on-boarding people. Once we have the standardized environment we can run on it, we can just tell the people to just
download this standardized environment and run it.

They still have plenty of things to set up. Maybe their editor or IDE or all kinds of other things, but at least they don't have to waste
so much time and energy by setting up their environment.

So that's about the <b>Why Docker</b> and we can go on now trying to figure out what Docker is.

