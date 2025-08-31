---
title: "Convert Python numpy array to in memory binary image using PIL or OpenCV"
timestamp: 2021-08-12T05:30:01
tags:
  - Numpy
  - PIL
  - OpenCV
  - imread
  - imwrite
  - BitesIO
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


OpenCV makes it very easy to read an image into memory and represent it as a Numpy array. Having a Numpy array makes it easy to manipulate the image
as various mathematical matrix transformations.

How can one save the image to disk and how can one create a binary object of it in memory.


## Read Image into a Numpy Array

In this example we take an image file and load it into memory using <b>imread</b>

{% include file="examples/python/opencv_read_image.py" %}


## Read/Write Image and convert to binary

Here we read the image from a file to a numpy array using OpenCV <b>imread</b>.

Then we make some simple manipulation, drawing a rectangle in the middle. We only use the fact that it is a Numpy array when
extract the <b>shape</b> of the image. We could have done other manipulations that don't have an implementation in OpenCV.

Then we save the image as another file using <b>imwrite</b>.

{% include file="examples/python/opencv_read_write_image.py" %}

Alternatively we could have converted the image into an in-memory set of bytes using <b>imencode</b> of OpenCV
and the <b>BytesIO</b> of the <b>io</b> package.


