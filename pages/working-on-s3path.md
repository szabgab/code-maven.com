---
title: "Working on s3path the Python File-System/Path like interface for AWS S3 with Lior Mizrahi"
timestamp: 2021-04-27T15:30:01
tags:
  - S3
  - AWS
  - Python
types:
  - screencast
published: true
books:
  - python
archive: true
show_related: true
---


Recording of a [live](/live) pair programming even in which [Lior Mizrahi](https://www.linkedin.com/in/lior-mizrahi-b894aa26/)
introduces his [s3path](https://github.com/liormizr/s3path) project and then we fixed an issue.


{% youtube id="Oww2d4X1lSk" file="s3path-lior-mizrahi_1920x1080.mp4" %}


[pathlib](https://docs.python.org/library/pathlib.html)

[pull-request 62 - add missing_ok parameter to the unlink method](https://github.com/liormizr/s3path/pull/62) fixing [issue 61](https://github.com/liormizr/s3path/issues/61).


[pull-request 63 - gitignore pyproject.toml](https://github.com/liormizr/s3path/pull/63).

Setup environment

```
python -m
pipenv install  --python python3 --skip-lock --dev

pipenv shell
```


