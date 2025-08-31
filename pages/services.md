---
title: "Services provided by Gabor Szabo at Code Maven"
timestamp: 2020-07-28T07:30:01
tags:
  - Git
  - CI
  - Jenkins
  - Automation
  - Docker
description: "All the services provided by Gabor Szabo, author of the Code-Maven site"
published: true
author: szabgab
archive: true
show_related: true
---


I provide various services to improve the development process, aka. velocity of an engineering team.

The various teams at my clients have different needs. I can offer one or more of the following services.
Usually they all include a large amount of training. Either via formal [courses](/courses) or
ad-hoc on the job training.

I can offer my servicaes on-site (as the situation allows) in Israel or on-line if we can match our working hours.

Spoken languages: English, Hebrew, Hungarian.


## Introducing or improving Version Control (Git)

One of the most basic things every development, QA, automation, and DevOps team needs is a good Version Control System (VCS).
Today the de-facto standard is Git, but you can use other systems as well.

Using a VCS properly can give certain superpowers to its users, for example the power to easily go back in time.
The possibility to experiment without fear.
The ease of reasoning about changes in the past.
A record of history.
Accountability.

However, if we don't set it up properly, if we don't have good procedures, if we don't invest enough time and practice in the VCS
then many people will feel it as a burden and some are even going to be afraid of it.

As far as I know many people who come out from the various hi-tech bootcamps and even university degrees lack the knowledge and the practice of a VCS.

In my experience many companies have teams that don't use any Version Control System or they could improved their development process a lot
by improving the way they use it.

* I can help setting up a Version Control System.
* I can train the team members to use it properly.
* Decide on a branching strategy that fits the team.
* Provide on-going support to the team for the time when they encounter special cases.


## Introducing testing and test automation

Many teams I've encountered lack any form of automated tests.
Having even a minimal test suite can increase the safety and velocity of the team by a lot.

By finding the problems sooner we can greatly reduce the time it needs to fix those problems and
the cost of fixing them. This is what many in the industry call "left shift", that we move various
steps of verifications to earlier stages of the development process which is usually represented in an image
to be moving from left to right.

I can help the team to start writing unit, integration, and acceptance tests.
Various types of functional tests and what many people call regression tests.

Your actually programming language usually does not make a difference. For unit-testing you'd probably use
the same language but for higher level tests you might use some simpler language such as Python.

I have already helped teams with projects in Perl, Python, PHP, Java, C#, C, C++, JavaScript.
Do you use any of these or do you use some other language that will be interesting to tackle?

Sometimes I help the development teams, other times the QA team or a dedicated Automation team.

## Setting up Continuous Integration (CI)

Even if you only have a single automated test it is already worth to set up a Continuous Integration system.

I can help you on-premise systems such as Jenkins, TeamCity, Bamboo, or cloud-based CI services such as Travis-CI, or Circle-CI.

You might also want to use the CI system that comes with your Git servers such as GitLab or Bitbucket.

All of these services help you with integration with various 3rd party services and standardized tools, but you still need
a lot of customization to support your needs.

## Standardized development, testing, and production environments

In order to have a good CI system we'll have to have standardized development, testing, and production environments.

In many organizations they way environments are set up isn't well documented and it travels from mouth-to-mouth.

This wastes a lot of time and creates a lot of frustration.

It is also one of the biggest obstacles to set up a Continuous Integration system.

The first step here is to collect the requirements to set up a development and testing environment.
Document it. First in free-text documents, then in the standard way of your programming language for
describing requirements.

Then automate the creation of the environments. Probably with one of the <b>Configuration Management</b>
tools such as Ansible, Puppet, or Chef.

Another step would be to create Docker Containers.

## Containerization - Docker

In order to make it easy to set up a development environment and a CI system we might opt to create Docker containers
for various parts of your product or service.

I can help creating the first Docker images and teach your team how to maintain and improve them.

First we will go through the steps outlined above to create a standardized environment and create a Docker image from that.

## Cloud systems

Many companies are moving some or all of their systems to the "cloud". This usually means one of the big ones:
Amazon AWS, or Google GCP, or Microsoft Azure, but it might be one of the others like Linode or Digital Ocean.

The first step usually is to rent Virtual Private Servers (VPS-es) and moving the application there.
That involves configuration of networks, security, load balancers etc.

Then next step is when the company starts to embrace various higher-level services of the cloud providers.
e.g. managed databases and the so-called serverless services. (Amazon Lambda, Google functions, etc.)

I can help with some of these step, but they can be valuable only if the company already has a good Version Control Strategy,
good testing strategy and standardized development and testing environment. Without that moving to the cloud will
just create more difficulties without solving any of the problems.

## Continuous Delivery or Continuous Deployment (CD)

CD refers to the possibility to make the changes in the code-base available to testers or even to end-users very frequently.

Basically it means you make production releases very frequently.

In the extreme cases like Amazon, this means deploying some new part of the system at a sub-second interval.
(Yes, they change their system more than once every second. I know it is crazy.)
Smaller and saner organizations (eg. GitLab) have 300 deployments a day. That is every 5 minutes.

For this to work you'll have to have a working CI system you can trust and probably you'll also need to have cloud based system.
Though it is also possible to have CD systems for in-house projects that use only on-premise systems for which there is no need
for any cloud component.

There are various strategies to mitigate the risks involved with such frequent deployments. The general consensus is that
once you have implemented to strategies your risk while using CD is much lower than what you had earlier when you
released/deployed/delivered once every few months.

I can help with this process, but remember this depends on all the other pieces working.

However, if that is your goal then the best strategy is to set up the whole system from version control
till deployment as soon as possible for a very small part of the system and then enhance it step-by-step
continuously improving your process.

## Training

In every case my work has the most value if during or after the implementation I can pass all the knowledge to
the in-house teams. This can be done in formal [training courses](/courses), with hands-on experience,
on-the job training, pair-programming, or ongoing support.

