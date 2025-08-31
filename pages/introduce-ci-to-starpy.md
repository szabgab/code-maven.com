---
title: "Introduce Continuous Integration (CI) to the starpy Python project"
timestamp: 2022-09-13T14:30:01
tags:
  - GitHub
  - GitHub Actions
  - CI
  - Python
types:
  - screencast
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


One of the first thing I do when start working on a project (either open source or in a corporation) is to make sure the
is a Continuous Integration system set up. In this video you will see how I added GitHub Actions to the
[starpy](https://github.com/Equal-Vote/starpy/) project.



{% youtube id="d6815sRIZ-Q" file="startpy-introduce-ci.mp4" %}

The points I made
* Make sure you have the python requirements listed in the `requirements.txt` file
* Make sure you can run `pytest` and it will find your tests. (test filenames start with `test_*`
* Having a README.md is also a nice thing with instruction how to set up an environment and how to run the tests.

This is the content of the `.github/workflows/ci.yaml` file from the project that configures GitHub Actions.

{% include file="examples/starpy/ci.yaml" %}

