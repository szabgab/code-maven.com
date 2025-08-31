---
title: "Google Load Balancer"
timestamp: 2019-01-01T07:30:01
tags:
  - CodeMaven
published: false
author: szabgab
archive: true
---



Setup an f1-micro server, copy echo.py, install virtualenv

sudo apt-get update
sudo apt-get install python-virtualenv
virtualenv -p python3 ~/venv3
source ~/venv3/bin/activate
pip install flask


Add to the crontab of root the following:

@reboot /home/gabor/venv3/bin/python /home/gabor/echo.py 5000

TODO: install a more roboust webserver for this or run uwsgi


Create a snapshot of the server
Create an image from the snapshot
Create an "Instance Template" that can create an instance of f1-micro using the above image.


Create an instance group

Networks Services - create a load balancer that uses the instance group.


{% include file="examples/load-balancer/web.py" %}

{% include file="examples/load-balancer/monitor.py" %}
