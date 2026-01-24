---
title: "Resize images on the command line using image magick"
timestamp: 2019-04-21T13:30:01
tags:
  - convert
  - identify
  - ImageMagick
published: true
author: szabgab
archive: true
---


## Install on Ubunutu

```
sudo apt-get -y install imagemagick
```


```
identify  image.png
file      image.png
```


## Convert image

```
convert image.png -resize 300x400 new_image.png
```


See also [Batch Resize Images using Linux Command Line and Imagemagick](https://guides.wp-bullet.com/batch-resize-images-using-linux-command-line-and-imagemagick/).

