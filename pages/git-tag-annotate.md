---
title: "The difference between annotated and simple git tags"
timestamp: 2019-05-01T21:00:01
tags:
  - git
  - tag
  - tags
published: true
books:
  - git
author: szabgab
archive: true
---


`git tag`

`git tag -a annotation -m "some message"`

The latter has its own annotator person and date and it can include a messge provided by the -m flag.


```
$ mkdir experiment
$ cd experiment/
$ git init .
Initialized empty Git repository in /home/gabor/experiment/.git/
```


```
$ touch README
$ git add .
$ git commit -m "add readme"
[master (root-commit) ab44956] add readme
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 README
```

```
$ echo "Hello World" > README
$ git add .
$ git commit -m "add hw"
[master 1f619d4] add hw
 1 file changed, 1 insertion(+)
```

```
$ git tag simple
$ git tag -a annotated -m message
```


```
$ git show HEAD
commit 1f619d4acb900ddfa1d69bbc7d0d0a59b3a184ee
Author: Gabor Szabo <gabor@twiggle.com>
Date:   Tue Apr 30 14:04:12 2019 +0300

    add hw

diff --git a/README b/README
index e69de29..557db03 100644
--- a/README
+++ b/README
@@ -0,0 +1 @@
+Hello World
```


```
$ git show simple
commit 1f619d4acb900ddfa1d69bbc7d0d0a59b3a184ee
Author: Gabor Szabo <gabor@twiggle.com>
Date:   Tue Apr 30 14:04:12 2019 +0300

    add hw

diff --git a/README b/README
index e69de29..557db03 100644
--- a/README
+++ b/README
@@ -0,0 +1 @@
+Hello World
```


```
$ git show annotated
tag annotated
Tagger: Gabor Szabo <gabor@twiggle.com>
Date:   Tue Apr 30 14:04:28 2019 +0300

message

commit 1f619d4acb900ddfa1d69bbc7d0d0a59b3a184ee
Author: Gabor Szabo <gabor@twiggle.com>
Date:   Tue Apr 30 14:04:12 2019 +0300

    add hw

diff --git a/README b/README
index e69de29..557db03 100644
--- a/README
+++ b/README
@@ -0,0 +1 @@
+Hello World
```

