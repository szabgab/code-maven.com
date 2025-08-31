---
title: "Exercise: parse hours log file and create time report"
timestamp: 2015-10-30T08:20:01
tags:
  - exercises
  - projects
types:
  - screencast
published: true
books:
  - ruby
  - python
  - javascript
  - php
author: szabgab
---


Exercise: Parse hours log file and create time report.


<slidecast file="beginner-perl/exercise-create-time-report" youtube="ICyJWvVAts4" />

When I was running class-room Perl training courses I've was logging how my course progresses and created
log files like this:

{% include file="examples/data/timelog.log" %}

Every row starts with the timestamp when the specific activity started and then the name of the activity.
Empty rows separate the dates.

Some of the activities are the names of the lectures, such as <b>Introduction</b> and <b>Scalars</b>.
Others are the names of the names of the activities: <b>Exercises</b>, <b>Solutions</b>, <b>Break</b>, <b>Lunch Break</b>,
and <b>End</b> marks the end of the training day.

A course lasts several days. In our sample file we have two days.

Once I had these log file I wanted to generate two reports.

One of them was to display the same data, but showing from-to timestamps and removing the <b>End</b> entry.
It would look like this:

```
09:20-11:00 Introduction
11:00-11:15 Exercises
11:15-11:35 Break
...
```

The other one would show the accumulated time spent on various activities
and the lectures detailed.

```
Lectures:  210 minutes 22%
Solutions:  95 minutes  9%
Break:      65 minutes  6%
...


Lectures: 
Introduction:  23 minutes 2%
...
```

This is the exercise, to implement the code that will take the log file and generate the reports.


## Tools
* 

## Solutions

* 



