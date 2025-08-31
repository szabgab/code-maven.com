---
title: "Build Docker image in GitLab CI/CD pipeline"
timestamp: 2021-06-18T07:50:01
tags:
  - Docker
  - GitLab
published: true
author: szabgab
archive: true
show_related: true
---


When running a GitLab CI/CD pipeline you can use any public Docker image, but you can also build your own images and use them later on.
In this article we'll see how to do that.

Out of the several options we'll see setting up your own Runner and using Docker on it.


A Runner is any real or virtual box. (AFAIK it can be Linux, Windows, and Mac as well.) On this box there is an application provided by GitLab
that handles the runner. In a pipeline you can execute code directly on the runner, but in most cases it is better to use a Docker container on top
of the Runner for your regular CI system.

However, when building a Docker image you will want to execute the docker commands directly on the Runner.

## Create a Virtual Machine

I tried this once with a [Digital Ocean Droplet](/digitalocean) that already had Docker installed and once
on [Azure](https://azure.com) where I had to install Docker manually.

## Install Docker

Follow the [Docker installation](https://docs.docker.com/get-docker/) on the machine and also
the post installation needed on Linux to allow non-root user to run docker. Enable it for the user <b>gitlab-runner</b>.

## Install GitLab Runner

First thing is to [Install GitLab Runner](https://docs.gitlab.com/runner/install/).

I personally followed the instructions to [Setup Docker Runner on Digital Ocean](https://about.gitlab.com/blog/2016/04/19/how-to-set-up-gitlab-runner-on-digitalocean/)

Also see [using docker build](https://docs.gitlab.com/ee/ci/docker/using_docker_build.html).

## Register the runner and restart

```
sudo gitlab-runner register -n --url https://gitlab.com/ --registration-token $TOKEN --executor shell --description "ShellRunner" --tag-list shell-runner
sudo gitlab-runner restart
```

In order to run the CI jobs in a Docker container we will need another runner:

```
sudo gitlab-runner register -n --url https://gitlab.com/ --registration-token $TOKEN --executor docker --description "Docker Runner" --tag-list docker-runner --docker-image alpine:3.14.0
sudo gitlab-runner restart
```

The docker-image parameter sets the default image. I don't think it is very important what you set here as you should always explicitly define it in the .gitlab-ci.yml file anyway.


Edit the following file and comment out everything

```
/home/gitlab-runner/.bash_logout
```

[Container registry](https://docs.gitlab.com/ee/user/packages/container_registry/)

{% include file="examples/gitlab-docker/Dockerfile" %}

{% include file="examples/gitlab-docker/.gitlab-ci.yml" %}


