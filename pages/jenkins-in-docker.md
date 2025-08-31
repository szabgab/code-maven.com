---
title: "Running Jenkins in Docker"
timestamp: 2020-10-03T19:50:01
tags:
  - Jenkins
  - Docker
description: "Running Jenkins in Docker"
published: true
books:
  - jenkins
author: szabgab
archive: true
show_related: true
---


In this example we'll see how to run a single-node Jenkins system in Docker.


I found this article about [the official Docker image](https://www.jenkins.io/blog/2018/12/10/the-official-Docker-image/)
that lead me to the [jenkins/jenkins](https://hub.docker.com/r/jenkins/jenkins/) image.

## Launch the first time

```
docker run -d -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 --name jenkins_master --rm jenkins/jenkins:lts
```

* This will run The container in the background (as a daemon) because of the <b>-d</b> flag.
* It will make the <b>/var/jenkins_home</b> of the container to a Jenkins volume called <b>jenkins_home</b>. If the volume does not exist it will create it. We need the volume to have persistence between re-launches.
* <b>-p</b> maps the ports
* <b>--name jenkins_master</b> will call Docker container jenkins_master. You can of course use any other name, but we'll need this name later on. Internally Jenkins refers to this node as "master" regardless of the name of the container you choose here.
* <b>--rm</b> tells Docker to remove the container when we stopped running it.

<h3>Copy secret</h3>

Once it launched we need to copy the one-time secret created by Jenkins, so type in:

```
docker container cp jenkins_master:/var/jenkins_home/secrets/initialAdminPassword .
```

(There is a separate dot at the end!)

The take the content of the file:

If your host is Linux/OSX use:

```
cat initialAdminPassword
```

If your host is Windows user:

```
type initialAdminPassword
```

It will print a string that looks like this: 2cead49b41fa41888c78d06be80fd5e7


Open this page in your browser: [http://localhost:8080/](http://localhost:8080/), that's where Jenkins will live.

<h3>Paste the string you got into the window.</h3>

Then select the <b>Install default plugins</b>, it will take some time to install the plugins.

It will then ask for the initial user. Give it whatever you like.

At this point you can use Jenkins and you have a single node called "master".

<h3>Create initial user</h3>

Probably a good idea to have a username/password pair that you won't forget. E.g. your own name.


Try to run the [Hello World pipeline](/jenkins-pipeline-hello-world)

## See the container running

```
docker ps
```


## To stop the Jenkins server

When you are done using the Jenkins server you might want to shut down the container so it won't use your CPU.

```
docker container stop jenkins_master
```

Because we used the --rm flag this will also remove the container. However the volume where we have all the data will remain.

To see the container is gone type in

```
docker ps -a
```

## List volumes

To see that the volume exists type in:

```
docker volume ls
```


## Start Jenkins again

In order to start the Jenkins server again type in the same command as you typed in when you first launched it above.
In our case this command:

```
docker run -d -v jenkins_home:/var/jenkins_home -p 8080:8080 -p 50000:50000 --name jenkins_master --rm jenkins/jenkins:lts
```

You can change basically any of the options now, for example you can use a different name for the container or you can decide
to map the server to another port. The only thing that must remain the same is the content of the <b>-v</b> flag and the name of the
base image. That will ensure we use the already existing volume that has all of our installations and configurations.

## Upgrading Jenkins

When there is a new release Jenkins (in its UI) will notify you and will suggest to upgrade it. That's probably useless in our case
as that would only upgrade in the currently running container, but we use the <b>--rm</b>  flag so our container will be removed when we shut down the application.

It is better to updat the image we are using.

```
docker pull jenkins/jenkins:lts
```

I just upgraded this way from Jenkins 2.249.1 to Jenkins 2.263.1.

## Plugins

Apparently the plugins that were installed on the first run were stored in the persistent volume we created so they survive the stop and re-start of the Docker
container and even the upgrade of the Docker image.

Once in a while Jenkins will notify you (on its UI) that new versions of the plugins are available. You can upgrade them via the UI.
The upgrades will also be persistent in the volume.


## Enjoy

