---
title: "DevOps vs. DevOps Engineer"
timestamp: 2021-06-21T15:30:01
tags:
  - DevOps
published: true
books:
  - devops
author: szabgab
archive: true
---


The name [DevOps](https://en.wikipedia.org/wiki/DevOps)  was coined in 2009 and it covered
"a set of practices intended to reduce the time between committing a change to a system and the change being placed into
normal production, while ensuring high quality".


The intention of the naming was to indicate the cooperation between Development and Operations including QA, Security and every other discipline in an organization
that touches the product or service the company builds.

However, in many organization instead of introducing and enhancing these practices a job title called DevOps Engineer was created.
In other places the <b>operations team</b>, or the <b>external system team</b> was renamed to be <b>DevOps team</b>.
So today you will see lots of job ads looking for DevOps Engineers.
The task of the people in these positions is very similar to what system administrators used to do, but now they are expected to also understand "the cloud",
the various cloud-based infrastructures and systems. They are also expected to know a lot more "scripting" than it was used to expected from system administrators.
The quotes around "scripting" is due to the fact that it is actually programming using one of the dynamic languages (e.g. perl, python, ruby, groovy) or in the unix shell.
However compiled languages are also in use, for example Go.

In many cases the real problem the DevOps movement tried to solve was not addressed.
The Developers and now the "DevOps team" are separate silos.
The developers write some code and then throw it over the virtual wall to the "QA team" to test or to the "DevOps team" to deploy.

One of the push-backs I get when I say that DevOps should not be a job-title, but definitely should not be a team,
is that "who will then do the work DevOps do now, the developers?".

Well, partially yes.

Partially it is a different organization structure. Instead of "developers", "devops", "qa", "infosec" teams, we have
teams that correspond to products (or services) that contain the expertise from the various fields.

We don't expect the developers to learn all that is to learn about the various cloud infrastructures or how to maintain
a database server, but we probably expect more involvement than used to be.

We probably also need to have an <b>Infrastructure team</b> that provides the shared tools for all the service-oriented-teams
to do they work. From development through deployment to maintenance of the service.

## What can be done?

I can tell you how I am trying to help improve the speed of development and the speed of value creation.

I help introducing automation - starting from the proper use of version control and branching through test automation,
containerization, Continuous Integration (CI) and sometimes even Continuous Deployment (CD).

The real value isn't in the installation and configuration of the respective tools.
The real value is getting the team used to think about the whole process from the change to the source code till the
deployment of that code on the server or on the computer of the client.

