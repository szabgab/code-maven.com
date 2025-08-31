---
title: "Build docker image with buildah"
timestamp: 2020-11-23T07:30:01
tags:
  - Buildah
  - Docker
description: "Buildah makes it easier to build a Docker image."
published: true
books:
  - docker
author: szabgab
archive: true
show_related: true
---


Creating a Docker image using [Buildah](https://buildah.io/)

We are going to go over a script that was taken from the [Perl builder project](https://gitlab.com/ioanrogers/perl-builder)
of [Ioan Rogers](https://www.linkedin.com/in/ioanrogers/) and that you can find at the bottom of this page.

While some of the commands are Perl specific, they only deal with the installation of Perl-based packages.
You can easily replace them with similar commands installing the packages of the project you work on.


<img src="/img/buildah.png" alt="Buildah logo" />

First of all you need to [install buildah](https://github.com/containers/buildah/blob/master/install.md).

I was lucky as Ubuntu has it in it a single command away.


## Download a Docker image

Download a Docker image from [Docker Hub](https://hub.docker.com/) if necessary, create a container and echo the name of the container.
If we run this again, it will create a new container and echo the name of that one.

When I ran this command I got a container called <b>perl-working-container</b>.

Running it a second time gave me <b>perl-working-container-1</b>.

The script, at the bottom calls this only once and assigns the output to a variable called <b>ctr</b>. (It probably stands for container.)

```
buildah from docker.io/perl:5.30
</cide>

## List containers

```
buildah containers
```

## Remove container

The following command helped me get rid of the extra container.

```
buildah rm perl-working-container-1
```

## List images

I used the following command to list all the images. Apparently the list of Docker images is handled separately by Buildah
as the regular `docker images` did not list the one I got using `buildah images`.

```
buildah images
```

## Configure Buildah Docker


The config command allows setting a number of configuration options such as the author of the image, what is the working directory,
and an environment variable.

```
buildah config
```

## Buildah Run

Then there is a Bash function definition of a function called <b>brun</b> that probably stands for <b>buildah run</b>
that will execute the run command of buildah, which seems to be analogous to the <b>RUN</b> command of Dockerfiles,
with the name of the container and with various additional parameters.

```
function brun() {
  buildah run $ctr -- "$@"
}
```

Then come the various calls to `brun`

```
brun cpanm App::cpm
```

[cpanm](https://metacpan.org/release/App-cpanminus) is the package installer of Perl (similar to pip for python or npm for NodeJS) and
this command installs the distribution that supplies the [App::cpm](https://metacpan.org/release/App-cpm) module which is another package
installer for Perl.

Then using this the new `cpm` command we install a number of other Perl modules from [CPAN](https://metacpan.org/).

Then we clean the caches of apt, the Debian/Ubuntu package manager:

```
brun apt-get clean
```

and remove the caches of the two Perl package managers so they won't take up space in the new Docker image.

```
brun rm -rf /root/.cpanm /root/.perl-cpm
```

## buildah commit

The last command in the script bakes the whole thing together into a Docker image using the image name and tag that were set up at the beginning of the shell script.

```
buildah commit --rm $ctr "$image:$tag"
```

## The original script

{% include file="examples/perl-builder/build.sh" %}

