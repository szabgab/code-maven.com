---
title: "Setup for Learning Ansible"
timestamp: 2018-03-18T10:30:01
tags:
  - Ansible
published: true
books:
  - ansible
author: szabgab
archive: true
---


In order to Learn Ansible you'll need to be familiar with at least the basics of Linux on the command line and you'll need to have a few Linux boxes to experiment with.


## Minimum Linux knowledge

* File-system operations: creating, listing, moving, removing, editing files.
* Using ping, ssh, sudo
* Configuring Nginx

You can use the [Linux mini-series](/linux) of articles to learn these.

## Linux boxes to experiment with

You'll need 3 (or more) Linux machines for each setup to use as host and one machine (either Linux or OSX) to run Ansible.

Your Options: Having a local installation or using machines in the cloud.

## MS Windows

If you have MS Windows on your computer:

Option one is to create 4 Virtual Machines on the computer you work on. 1 where you'll install and run Ansible and 3 to act as hosts you manage.

Option two is to create 1 Virtual Machine on the computer you work on and use 3 VPS (Virtual Private Server) in the cloud. On the local Virtual Machine you'll install and run Ansible. You will manage the 3 VPS-es.

## OSX or Linux

If you run Linux or OSX then it can be used as the machine where you install and run Ansible so you only need the 3 host machines. Those can be either local, inside Virtual Box, or they can be remote. Using some VPS.

## Virtual Linux boxes locally

IMHO The best option is to create the 4 Linux boxes in a VirtualBox image locally. That will allow you to use them anywhere and they don't cost you anything.
Follow the [Linux mini-series](/linux) explaining how to install Ubuntu Linux on VirtualBox and how to configure the network. If you already have a Linux Box in VirtualBox then start reading how to [setup two Virtual Linux boxes](/setup-2-ubuntu-boxes-in-virtualbox-to-communicate-with-each-other).

## Virtual Private Server (VPS)

As for cloud-based VPS, there are several providers. One I use often is [Digital Ocean](/digitalocean).

Visit [Digital Ocean](/digitalocean) using this ref-code. If you don't have an account yet, sign up. The ref-code is supposed to give you $10 credit which is plenty as you can run a VPS by the hour and pay only $0.007/hr. I might be mistaken, but as I understand at this point you'll either need to pay $5 via PayPal or provide a Credit Card that will be only charged after you run out of the $10 initial credit.

If you don't have yet, create an [ssh Private/Public pair](/generate-and-deploy-ssh-private-public-keypair) on the machine you'll use to run Ansible. (Either your Linux machine or OSX notebook, or the VirtualBox you have created for this.) 

