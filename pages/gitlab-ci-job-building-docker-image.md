---
title: "GitLab CI job building a Docker image"
timestamp: 2020-11-29T17:30:01
tags:
  - GitLab
  - CI
  - Docker
description: "Use the Docker repository of GitLab to host the image you need to run all the other CI jobs."
published: true
books:
  - docker
author: szabgab
archive: true
show_related: true
---


[GitLab](https://gitlab.com/) allows you to use any Docker image to run your CI jobs. Sometimes you'll want to create your own Docker
image, store it in the [GitLab container registry](https://docs.gitlab.com/ee/user/packages/container_registry/) and use the.

In this article we'll review a GitLab CI job that creates the image and pushes it out to the container registry.


We are going to go over the GitLab CI config YAML file that was taken from the [Perl builder project](https://gitlab.com/ioanrogers/perl-builder)
of [Ioan Rogers](https://www.linkedin.com/in/ioanrogers/) and that you can find at the bottom of this page. Although this specific project creates
a Docker image to test [Perl code](https://perlmaven.com/), the idea can be used for any programming language.

First of all you might wonder why do we need to create an image, why not just use a base image and install everything during the CI process. The primary reason is
speed. Many time you need lots of prerequisites to run some applications. Doing that on every run of the CI system would be a lot of waste of time and resources.
By creating an image that already has many of the packages installed we can save time, money, and get feedback much faster.

The repository has two files in it. The <b>build.sh</b> shell file that [builds a docker image using Buildah](/build-docker-image-with-buildah) and the
<b>.gitlab-ci.yml</b> file we are discussing now.

It has two jobs: <b>buildah-build-master</b> will run on the mater branch and <b>buildah-build</b> on all the other branches. These are controlled by the
[only and except](https://docs.gitlab.com/ee/ci/yaml/#onlyexcept-basic) keywords. As the documentation suggest in improved way would be to use
the [rules](https://docs.gitlab.com/ee/ci/yaml/#rules) syntax.

## The difference

As I can see the only difference between the two is that the job on the master branch also adds the <b>latest</b> tag to the created image.

## The common part

They both use the [buildah Docker image](https://quay.io/repository/buildah/stable) from [quay.io](https://quay.io/), the Docker repository of Red Hat.

The name of the <b>stage</b>, does not really matter.

In the <b>before_script</b> part, that surprisingly happens before the <b>script</b> part both jobs authenticate with the Docker repository.
The environment variables <b>$CI_REGISTRY_USER</b>, <b>$CI_REGISTRY_PASSWORD</b>, and <b>$CI_REGISTRY</b> are all
[predefined variables](https://docs.gitlab.com/ee/ci/variables/predefined_variables.html) provided by GitLab.

So are the variables <b>$CI_REGISTRY_IMAGE</b> and <b>$CI_COMMIT_REF_SLUG</b> used in the other commands.

After going over it, this isn't a complex pipeline after all.

{% include file="examples/perl-builder/.gitlab-ci.yml" %}

