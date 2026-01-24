---
title: "Working on PyDigger with Upasana Shukla"
timestamp: 2021-05-24T13:30:01
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


{% youtube id="X5xqXwhaASg" file="pydigger-with-upasana-shukla-2021-05-23_1920x1080.mp4" %}

* [0:00 Hello, showing dev.pydigger.com that was a temporary place for the Docker based setup.](https://youtu.be/X5xqXwhaASg?t=0)
* [1:50 Docker compose](https://youtu.be/X5xqXwhaASg?t=110)
* [4:00 Issues. Explaining flake8 and mypy.](https://youtu.be/X5xqXwhaASg?t=240)
* [6:25 Decide on Driver-Navigator again; Setting up the Python virtual environment again.](https://youtu.be/X5xqXwhaASg?t=385)
* [10:08 Looking at the the CI (GitHub Actions) to see how we run the tests](https://youtu.be/X5xqXwhaASg?t=608)
* [12:00 Running the tests with the flake8 flag and running through the issues.](https://youtu.be/X5xqXwhaASg?t=720)
* [17:00 Using a variable that does not exist. Digging through git history understanding what we did last time.](https://youtu.be/X5xqXwhaASg?t=1020)
* [24:30 Development configuration (dev.yml)](https://youtu.be/X5xqXwhaASg?t=1470)
* [30:45 Using](https://youtu.be/X5xqXwhaASg?t=1845) `git stash` and then `git checkout` older version to find how we broke the code. Upasana showing her total control of git.
* [40:06 We found the bug. Now let's check it and the clean up more of the issues reported by flake8.](https://youtu.be/X5xqXwhaASg?t=2406)
* [47:30 Add flake8 testing to the CI system as well.](https://youtu.be/X5xqXwhaASg?t=2850)
* [49:00 Looking at the flake8 configuration in setup.cfg and explaining about them.](https://youtu.be/X5xqXwhaASg?t=2940)
* [50:44 How Gabor likes to indent code](https://youtu.be/X5xqXwhaASg?t=3044)
* [55:10 Explain about sys.path](https://youtu.be/X5xqXwhaASg?t=3310)
* [1:01:15 The stats page is broken. Explaining why.](https://youtu.be/X5xqXwhaASg?t=3675)
* [1:02:28 Buy my books and support my work!](https://youtu.be/X5xqXwhaASg?t=3748)
* [1:04:15 Getting back to the flake8 ticket collecting this information about all the projects.](https://youtu.be/X5xqXwhaASg?t=3855)
* [1:07:40 Telling about the idea of showing the images (gravatars) of all the authors of the packages.](https://youtu.be/X5xqXwhaASg?t=4060)
* [1:11:10 Flake8 it is](https://youtu.be/X5xqXwhaASg?t=4270)
* [1:12:20 Explaining __name__ == '__main__'](https://youtu.be/X5xqXwhaASg?t=4340)
* [1:16:50 Adding logging](https://youtu.be/X5xqXwhaASg?t=4610)
* [1:36:20 Now that we know how to use the myflake8 module we can start thinking how to run it on the source code of other projects.](https://youtu.be/X5xqXwhaASg?t=5780)
* [1:37:30 Download a zip file using requests to a temporary directory and then unzip it.](https://youtu.be/X5xqXwhaASg?t=5850)
* [1:56:30 Wrapping up](https://youtu.be/X5xqXwhaASg?t=6990)

