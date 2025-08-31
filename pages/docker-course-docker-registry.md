---
title: "Docker course: Docker Registry"
timestamp: 2022-11-09T07:00:01
tags:
  - Docker
types:
  - screencast
published: true
books:
  - docker
author: szabgab
archive: true
show_related: false
---


{% youtube id="rkQc84L1qoI" file="english-docker-course-docker-registry.mkv" %}

In this episode we are discussing the [Docker Registry](https://code-maven.com/slides/docker/docker-registry).
(See all the [Slides](https://code-maven.com/slides/docker/))

A Docker Registry is a place where people can upload their Docker images so others can use those images.
There are private and public registries. The main public registry is the [Docker Hub](https://hub.docker.com/)
where you can upload public images for free and private images after certain payment.

The big cloud providers also have their own container registries which are integrated with their cloud offering.

For example there is the [GCR - Google Cloud Container Registry](https://console.cloud.google.com/gcr/),
the [ECR - AWS Elastic Container Registry](https://aws.amazon.com/ecr/) and the [Azure Container Registry](https://azure.microsoft.com/en-us/products/container-registry/#overview).
The smaller players also offer it, for example there is the [Digital Ocean Container Registry](https://www.digitalocean.com/products/container-registry).

In these registries you can search for various Docker images.

For example visit the [Docker Hub](https://hub.docker.com/) and search for <b>mongodb</b>. You'll find a number of images.
You can download them and use them and you will not have to worry yourself how to create a Docker image for many of the common services.

Then search for <b>Wordpress</b>. You'll find images that will make it easy to run Wordpress on your computer either locally or on a server.
You won't have to worry much about installation and configuration and relatively easily you'll be able to upgrade it to newer versions.


You can also create your account on [Docker Hub](https://hub.docker.com/) and upload your own Docker images.
As long as the images are public you don't have to pay and I think you can also have one private image, but if you'd like
to have more than there is some fee involved.

The idea would be that you create and upload an image and then later you, some other members of your team, or even on your production server
you can download use that image.

Docker Hub is for the general use, but if you use one of the cloud providers then probably you should also use their Docker registry.

## Set up your own registry

If neither of those choices are good for you, for example because you'd like to have all the images in-house, you can
[deploy your own registry server](https://docs.docker.com/registry/deploying/).
It can be on premise, in the offices of your company or you can put it on some server elsewhere.

That's all for now about Docker registries. We are going to see them later on as all the images we are using are based on some other image that is in the Docker hub.

## Hello World!

The next episode will cover the <b>Hello World!</b> of Docker containers.






