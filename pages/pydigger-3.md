---
title: "Working on PyDigger with Upasana Shukla - part 3"
timestamp: 2021-06-20T21:30:02
tags:
  - live
  - Python
types:
  - screencast
published: true
author: szabgab
archive: true
show_related: true
---


In this [live pair programming](/live) session
[Upasana Shukla](https://www.linkedin.com/in/upasana-shukla/) and myself were working on the
[PyDigger](https://pydigger.com/) project.


{% youtube id="uG6G92t7JV8" file="pydigger-with-upasana-shukla-2021-06-20_1920x1080.mp4" %}

The source code of the [cwd context manager](https://code-maven.com/slides/python/cwd-context-manager).

[MongoDB aggregation get counts of key value pairs](https://stackoverflow.com/questions/16492891/mongodb-aggregation-get-counts-of-key-value-pairs)

* [0:00 Hello - Our code is now deployed!](https://youtu.be/uG6G92t7JV8?t=0)
* [1:50 Updating the local Git of Upasana and trying to remember what we did last time.](https://youtu.be/uG6G92t7JV8?t=110)
* [8:00 Discussing the new and proper way of using Docker-compose override.](https://youtu.be/uG6G92t7JV8?t=480)
* [16:50 Get inside the docker container (exec) to run our program.](https://youtu.be/uG6G92t7JV8?t=1010)
* [20:00 Trying to understand why config.yml is needed and why is it missing.](https://youtu.be/uG6G92t7JV8?t=1200) [#50](https://github.com/szabgab/pydigger.com/issues/50)
* [26:10 After fixing that we encounter the missing dev.yml. Because we change directory in the process and don't change it back.](https://youtu.be/uG6G92t7JV8?t=1570)
* [27:10 Explaining about context managers in Python, creating one for chdir.](https://youtu.be/uG6G92t7JV8?t=1630)
* [37:15 Remove the temporary directory when we are done with it using a context manager.](https://youtu.be/uG6G92t7JV8?t=2235)
* [46:30 Let's figure out why the --url parameter did not have the expected impact and how to run the fetch.py properly. Let's also update the README file.](https://youtu.be/uG6G92t7JV8?t=2790)
* [50:00 Start collecting the flake8 results](https://youtu.be/uG6G92t7JV8?t=3000)
* [55:00 Trying to figure out why the flake8 code does not get executed.](https://youtu.be/uG6G92t7JV8?t=3300)
* [1:02:30 Add the --package command line option](https://youtu.be/uG6G92t7JV8?t=3750)
* [1:09:50 Finally we have Flake8 results!](https://youtu.be/uG6G92t7JV8?t=4190)
* [1:12:50 Adding the Flake8 results to the datastructure and store it in MongoDB.](https://youtu.be/uG6G92t7JV8?t=4370)
* [1:16:15 Trying to run mongo, the MongoDB client inside the container.](https://youtu.be/uG6G92t7JV8?t=4575)
* [1:24:30 Deleting (dropping) the MongoDB database](https://youtu.be/uG6G92t7JV8?t=5070)
* [1:25:50 Describing this in the README](https://youtu.be/uG6G92t7JV8?t=5150)
* [1:28:00 Start looking at the web page to see the newly collected Flake8 report.](https://youtu.be/uG6G92t7JV8?t=5280)
* [1:37:00 Trying to figure out the right MongoDB query](https://youtu.be/uG6G92t7JV8?t=5820)
* [1:55:00 Cleaning up making sure tests are passing and the previous code still works.](https://youtu.be/uG6G92t7JV8?t=6900)

