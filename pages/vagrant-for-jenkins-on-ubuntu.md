---
title: "Vagrant for Jenkins on Ubuntu"
timestamp: 2019-02-15T12:30:01
tags:
  - Jenkins
  - Vagrant
  - Ubuntu
published: true
author: szabgab
archive: true
---


A simple Vagrantfile you can use to set up Jenkins and start using it.


{% include file="examples/vagrant-jenkins-ubuntu/Vagrantfile" %}

* Create an empty directory.
* Copy the above file to it as <b>Vagrantfile</b>.
* Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) if you don't have them yet.
* cd to the directory and run <b>vagrant up</b>. It will take a while to download the image and then to install Jenkins in the image.
* Then on your computer browse to http://localhost:8080/  It will want to get a secret code.
* On the command line type int <b>vagrant ssh</b> this will ssh into the VirtualBox running Jenkins
* type <b>sudo cat /var/lib/jenkins/secrets/initialAdminPassword</b> to get the secret, copy that secret to the browser
* Install the defaults, create a user for yourself.
* At this point I got a blank page (seems to be some bug) so I switched back to the terminal and restarted the machine by typiing in <b>sudo reboot</b>.
* Once the machine started again you can reload the page in the browser and it will (most likely) show you the login page of Jenkins.

