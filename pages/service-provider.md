---
title: "Service Provider"
timestamp: 2018-07-02T13:00:01
tags:
  - CodeMaven
published: true
author: szabgab
archive: true
---


There are several ways to structure an Engineering organization. One of the traditional ways is to create Service Provides.
For example the QA department or team. The IT department. The Information Security (InfoSec) department.

These are similar to other functions of the organization: Marketing, Sales, HR, Legal, Finance etc.

These days some organizations also have dedicated DevOps teams.


Organization that is structured this way emphasize the collective expertise in one subject that belongs to one team.
Usually they see the people inside one team more interchangeable. They have a high level of expertise in their field,
but usually have limited understanding of other parts of the organiation.

The development team in such organization would only handle development of the product. Then it would usually hand over a version of the product to the QA team that would check it, open bug reports and return the task to you. You'd then go back-and-forth between the development team and the dedicated QA team.

Once QA is done, you'd go to the InfoSec team so they check the product for vulnaribilities. They would probably check the product both as a black box, but they might also look at the source code to look for security issues. Then you have a back-and-forth ping-pong with this team as well.

Once the InfoSec team gives it's green light, you'd go to to the IT Operations team, or these days you'd go to the DevOps team to ask them to deploy the product.

Each of these interactions is time consuming.
As you are not the only development team waiting for the various other team, in each interaction there are going to be queues.
There is going to be fighting for priority etc.
Each of these interactions is an opportunity for misunderstanding and for information loss.


