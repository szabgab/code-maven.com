---
title: "Testing a Docker image created by GitLab CI"
timestamp: 2021-08-16T15:30:01
tags:
  - GitLab
  - CI
  - Docker
published: true
books:
  - gitlab
author: szabgab
archive: true
show_related: true
---


We have already see how to set up a GitLab Runner and how to [build a Docker image in a GitLab pipeline](https://code-maven.com/build-docker-image-in-gitlab-pipeline).

Now we are going to see how to test the image.


For this we need a little project, this is our directory layout:

```
.
├── app.py
├── Dockerfile
└── .gitlab-ci.yml
```


The application that we would like to add to the Docker image is a really small Python Flask application:

{% include file="examples/gitlab-test-docker-image/app.py" %}

The Docker image is also not very complex:

{% include file="examples/gitlab-test-docker-image/Dockerfile" %}


## GitLab CI pipeline

The interesting part is the GitLab pipeline:

{% include file="examples/gitlab-test-docker-image/.gitlab-ci.yml" %}

There are two jobs.

The build job will build the image and upload it to the Docker registry of GitLab.

The test-image job will start the newly built image as a [GitLab CI service](https://docs.gitlab.com/ee/ci/services/). GitLab will automatically map the ports that are opened in the image
and the "alias" field can used to define a hostname for the service. One could also add a command to be executed on the docker container,
but in our case that's not necessary as we have it inside the Dockerfile.


Then we have the "image" field that tells GitLab what image to use for the CI job and finally we have simple "script" tag that uses <b>curl</b>
to access the web application running in our container that was created from the image we just built.

At this point you could write any types of test that would access the application from the outside. You could also launch other services, for example a database server and thus you
can have an environment that resembles your production system.



One caveat that I think I bumped into at a client, is that you might have created the GitLab username and/or the project name with mixed case letter and I using the $CI_PROJECT_NAMESPACE
and variable $CI_PROJECT_NAME will retain the case, but as I recall the Docker registry did not like that. However now thinking back, that might have been a totally different issue.
In any case, let me leave this warning here.
