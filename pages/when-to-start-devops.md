---
title: "When to introduce DevOps to your organization?"
timestamp: 2019-07-24T07:30:01
tags:
  - DevOps
published: false
author: szabgab
archive: true
---


There are plenty of articles on how to introduce DevOps, but few address the issue of when to do it?


* Should it be started after we have the first version of our product on the market?
* Should DevOps be started when we have the first mockup of the product?
* When we start writing code?

The word DevOps or DevSecOps or DevTestSecOps cover a lot of things and have many meanings depending on who you ask.

The key ideas, in my opinion, are <b>fast feedback loop</b>, <b>self-service employees</b>, and <b>automation</b>.
If I can add two more then: <b>communication</b> and <b>cooperation</b>.

## Fast feedback in the development process

If you could chose when do you get feedback to your work, would it be sooner or later?
If you make a mistake, would you like to know about right away, or is it ok to learn about it 6 months later?

Common sense, and many research agree that the sooner we get feedback the better.

There are several reasons for this.

One is that developers need to keep many thing in mind and they have to jump between different areas of the software, not to mention when they need to jump between project. Each such jump is called a
"context switch" and every time the developers need to do that they need to fill their brain with the information about the current part of the project or the current project.
In order to do this they will quickly forget many parts of the previous area. If you report a problem after such switch, the switching back will cost a lot of time.

If the bug is reported several months later, the same developer might be on a different project or might have even left the company.
Then a new person has to learn this area of the project that will take a lot of time which means it will cost a lot of money.

Another huge cost might be if the developers build on the mistake. This might mean that fixing the problem will require changes in a lot of other code as well.
Obviously this will take a lot of time and cost a lot of money.

The common push-back is "we don't want to frequently disturb our developers with problems", but this is false.
Developers usually prefer to work in one area of the code instead of jumping back-and-force.

Who and when can provide you feedback to your software?

* Some of the end-users will report bugs if they believe that you actually care and that you will fix the issues in a reasonable time.
* You can also have internal testers, people who will try to use the software as end-users do and report the problems to you. This usually gives a faster feedback, but you have to pay these people.
* You can have automated tests on various levels and you can run them on every commit/push to get even faster and more accurate feedback. For this you'll need a Continuous Integration system and the developers will have to write tests.
* You could even let your engineers work in pairs or in mobs in which case the feedback can be even faster than running the tests.

How to make sure your software does not deteriorate?


If you have a shrink-wrap product, one that the clients download to the computer and install, you might be facing a very long 


[Where to start with DevOps?](https://www.reddit.com/r/devops/comments/5vhgw6/where_to_start_with_devops/)

[DevOps for Startups: 5 tricks for successful adoption](https://hackernoon.com/devops-for-startups-5-tricks-for-successful-adoption-ef4d563d0b05)

