---
title: "Docker course: Hello World"
timestamp: 2022-11-10T22:01:01
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


{% youtube id="ePuRkT0QUrE" file="english-docker-course-hello-world.mkv" %}

Finally we get to the point where we actually start to use Docker.

On Linux and macOS open the Terminal, on Windows open the Command Prompt (click on the Windows button on your keyboard, type in "cmd" and press ENTER).
I'd also recommend you enlarge this window so you will see more content.

Type in the following command:

```
docker run hello-world
```

At this point Docker will try to start a <b>container</b> using the latest version of the image called <b>hello-world</b>.
If this is the first time you try to do this, you won't have this images on your computer so you will see a warning:

```
Unable to find image 'hello-world:latest' locally
```

Then Docker will automatically try to download the image from the [Docker HUB](https://hub.docker.com/) and will let you know about this:

```
latest: Pulling from library/hello-world
```

It shows you some progress and that it managed to download it:

```
2db29710123e: Pull complete
Digest: sha256:c77be1d3a47d0caf71a82dd893ee61ce01f32fc758031a6ec4cf1389248bb833
Status: Downloaded newer image for hello-world:latest
```

Then it will start a Docker container based on the <b>hello-world:latest</b> image.

This will print some text on the screen starting with

```
Hello from Docker!
```

The full output will look similar to this:

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
2db29710123e: Pull complete
Digest: sha256:c77be1d3a47d0caf71a82dd893ee61ce01f32fc758031a6ec4cf1389248bb833
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

Once the text is printed to the screen the container will stop running.

This is not a very sophisticated image, it can only print this text and has no further functionality.

## After Hello World - check the status

Before going on and trying to do more complex things with other images, let's look around to see what happened on the hard-disk of our computer.

Run

```
docker ps -as
```

This will show you a report with a number of columns. The <b>-a</b> tells it to show <b>all</b> the containers and the <b>-s</b> told it to include the <b>SIZE</b> column.

This list all the containers that have ran and are still around on your disk.

IF this is a clean computer where you only ran the above command then this is more or less what you will see.

In the first column you will see the <b>CONTAINER ID</b>. This will be different as it is the ID of the container
which is the runtime version of the image. It changes from run to run.

The 2nd column is the name of the <b>IMAGE</b> which is <b>hello-world</b> as that's what we used.

<b>COMMAND</b> is the command that was executed inside the container. This was the default command baked in the image.

<b>CREATED</b> is the time when the container was created.

<b>STATUS</b> is, well the status of the container. Currently it reports that this container has stopped running.

<b>PORTS</b> is not interesting now.

<b>NAME</b> holds the name of the <b>container</b>. If the user does not provide a name, and we did not provide a name, than docker will pick a random name created from two random words.

<b>SIZE</b> is how much space the container takes up on the disk.

The command:

```
docker ps -as
```

The output:

```
CONTAINER ID   IMAGE        COMMAND   CREATED         STATUS                     PORTS  NAMES          SIZE
20dc20bcac8f   hello-world  "/hello"  31 minutes ago  Exited (0) 31 minutes ago         jovial_bouman  0B (virtual 13.3kB)
```


## docker ps

If I ran <b>docker ps</b> without the extra parameters then it would only show the titles as the command without the <b>-a</b> (all) flag only shows the currently running containers and ours has already finished running.

```
docker ps -a
```

shows all the containers that are running and all the containers that have stopped but have not been deleted yet.



## docker images

If you type in

```
docker images
```

you will see the list of images on your computer.

```
REPOSITORY              TAG                IMAGE ID       CREATED         SIZE
hello-world             latest             feb5d9fea6a5   14 months ago   13.3kB
```

Here you can see the images that were downloaded or that were created locally.

You remember as we ran the <b>docker run ...</b> command docker told us that it cannot find the images locally and so it downloaded the image called <b>hello-world</b> with the <b>latest</b> tag.

In the first column you can see the name of the image. The second column is the tag. In this case it is <b>latest</b>.

The <b>IMAGE ID</b> is a short version of the unique ID of the image.

<b>CREATED</b> shows when was the image created. In our case this is an image that was created 14 month ago.

<b>SIZE</b> is the size of the whole image.

As you can see this is a really, really small image. Basically just the text we saw.


We can see that there are images and containers which are the runtime copies of the images.

## Run Hello World again

```
docker run hello-world
```

This time it does not say that it can't find the image, and it does not need to download the image as we already have it locally.
It only prints the text starting with <b>Hello from Docker!</b>.

Now we take a look at the status of the containers:

```
docker ps -as
```

The result will look something like this:

```
CONTAINER ID   IMAGE        COMMAND   CREATED        STATUS                    PORTS NAMES             SIZE
f4b4ef0de525   hello-world  "/hello"  7 seconds ago  Exited (0) 6 seconds ago        focused_margulis  0B (virtual 13.3kB)
20dc20bcac8f   hello-world  "/hello"  8 minutes ago  Exited (0) 8 minutes ago        jovial_bouman     0B (virtual 13.3kB)
```

Now we have two lines. The second line is the same as we had earlier, except of the CREATED and STATUS columns that shows relative time and that has changed.

As you can see the <b>CONTAINER ID</b> is different in the two rows and the <b>NAMES</b> are different, but the <b>IMAGE</b> and the <b>COMMAND</b> are the same.

If we list the images using <b>docker images</b> we can see that the list of images has not changed. We still has that single image on our computer.

## Remove container

The last thing we would like to see now is how to get rid of these containers that were created and saved on the disk.

We can use the <b>CONTAINER ID</b> to remote a container.

```
docker rm 20dc20bcac8f
```

If we run again

```
docker ps -as
```

Then you can see that only one line remained:

```
CONTAINER ID   IMAGE        COMMAND   CREATED        STATUS                    PORTS NAMES             SIZE
f4b4ef0de525   hello-world  "/hello"  27 seconds ago  Exited (0) 26 seconds ago      focused_margulis  0B (virtual 13.3kB)
```

We can also remove the other container in the same way after which there are no more containers left on the system as you can verify by running <b>docker ps -as</b> again.

## Remove a Docker image

The image is still there as you can see by running <b>docker images</b>.

In order to remove that we can use the <b>rmi</b> command:

```
docker rmi hello-world
```

```
Untagged: hello-world:latest
Untagged: hello-world@sha256:c77be1d3a47d0caf71a82dd893ee61ce01f32fc758031a6ec4cf1389248bb833
Deleted: sha256:feb5d9fea6a5e9606aa995e879d862b825965ba48de054caab5ef356dc6b3412
Deleted: sha256:e07ee1baac5fae6a26f30cabfe54a36d3402f96afda318fe0a96cec4ca393359
```

If we run again <b>docker images</b> then we can see it is gone.

## Next

Next we are going to see a slightly more complex example using the <b>busybox</b>, but before you go there I'd recommend you try the commands you just saw.

