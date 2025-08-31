---
title: "Docker"
timestamp: 2018-12-07T09:30:01
tags:
  - Docker
published: true
author: szabgab
archive: true
---


Check out the [Docker Course](/docker).


Build a Docker image

```
docker build -t NAME .
```

List Docker Images

```
docker images
```

List Running Docker Containers

```
docker ps
```

List All Docker Containers, includig the ones that were stopped

```
docker ps -a
```

Run a docker image in an interactive mode and open /bin/bash

```
docker run -it IMAGE /bin/bash
```

Run the Docker image called IMAGE as the container called NAME in an interactive mode.
Attach the current working directory in the host filesystem to the /opt in the container.

```
docker run -it -v $(pwd):/opt --name NAME IMAGE
```

List all the docker containers in quiet mode - CONTAINER IDs only

```
docker ps -aq
```

Remove docker container by DOCKER ID

```
docker rm DOCKER_ID
```

Combine the above two and remove all exited (stopped) the Docker containers:

```
docker rm $(docker ps -aq)
```




```
docker run -it  -d -p 8080:80 sudoku  /bin/bash
```

Attach to running container based on CONTAINER ID that can be listed by `docker ps -a`.

```
docker attach CONTAINER_ID
```

Then we can exit the container.


## Docker Hub

Once we have a Dockerfile in our GitHub project we can configure Docker to host our public image.
For this we need to register on the [Docker HUB](https://hub.docker.com/). In there we need
to click on Create/Create Automated Build in the menu. If we have not linked our GitHub account yet then we need
to do it now. (See [Configure automated builds on Docker Hub](https://docs.docker.com/docker-hub/builds/)
for further details.)


## Digital Ocean

The docker-machine command allows us to use VPS-es on various cloud service providers, for example on [Digital Ocean](/digitalocean). There is an article on [Docker for Digital Ocean](https://docs.docker.com/machine/examples/ocean/).

```
$ docker-machine create --driver digitalocean --digitalocean-access-token xxxxx docker-sandbox
```

Where xxxx is the Access token you generate in your Digital Ocean account. docker-sandbox is an arbitrary name that will be used as the name of the VPS on Digial Ocean.

```
$ docker-machine ls
$ docker-machine ip docker-sandbox
$ docker-machine inspect docker-sandbox
```

There all Run locally and lists the machne we have in the cloud and maybe also locally or inspect the configuration of one of the machines.

```
docker-machine env docker-sandbox
```

```
eval $(docker-machine env docker-sandbox)
```


