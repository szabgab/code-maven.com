---
title: "Setup local development environment for R-yaml"
timestamp: 2023-03-20T07:30:01
tags:
  - R
published: true
books:
  - R
author: szabgab
archive: true
show_related: true
---


One of the participants in [Open Source Development Course](https://osdc.code-maven.com/) uses R for her research work. So we decided that in one of the meetings we'll try to explore how to set up local development environment for one of the R-based packages using Docker.

Disclaimer: none of the participants had any experience in contributing to open source projects in R so we might have totally misunderstood how one should set up an environment.


First we looked for a project to play with. Checked the [r projects](https://github.com/topics/r?l=r&o=desc&s=stars), then looked at the [awesome-R](https://github.com/qinwf/awesome-R) list and found [r-yaml](https://github.com/vubiostat/r-yaml/). We thought a library dealing with YAML files will be simple to install and test.

One thing we noticed quite quickly is the [the compile target was missing from the Makefile](https://github.com/vubiostat/r-yaml/issues/125). That's however is a minor issue in the documentation.

Then we spent quite a lot of time figuring out why things are failing. After about an hour of failures we felt it would be better to [open an issue](https://github.com/vubiostat/r-yaml/issues/126). Within a few minutes, maybe half an hour we got a response that solved the problem.

So here is how one could create a local development environment in a Docker container:

## Clone the repo

```
git clone git@github.com:vubiostat/r-yaml.git
cd r-yaml
```

## Start Docker container

Start a Docker container using an image based on R version 4.2.3 that was listed on [Docker Hub](https://hub.docker.com/_/r-base).

Give the container a name "r-yaml" to make it easy to reuse it.

Designate the internal /opt folder as the workdir.

Map the current working directory to the internal /opt

I have not tried it, but I think MS Windows users will have to replace the <b>-v$(pwd):/opt</b> part by <b>-v %cd%:/opt</b> if using cmd or by <b>-v ${PWD}:/opt</b> if using PowerShell.

Run bash in the container.

```
docker run -it --name r-yaml --workdir /opt -v$(pwd):/opt r-base:4.2.3 bash
```

## Install RUnit

Inside the container install the R dependency.

```
Rscript -e 'install.packages("RUnit")'
```

## Install the external dependencies

```
apt-get update
apt-get install -y texlive-latex-base texlive-fonts-extra texlive-latex-recommended texlive-fonts-recommended
```

## Run the tests

```
make check
make test
```

## Exit from the container

```
exit
```

This will also stop the container.


## Restart the container

We can restart the stopped container:

```
docker container start -i r-yaml
```



## Remove the container

If we don't need the container any more we can remove it (after we exited and it was stopped).

```
docker rm r-yaml
```


## Clean the environment

```
sudo git clean -dxf
```

This will print:

```
Removing build/
```

## Conclusion

I hope this description will help someone else setting up the environment. I'll also suggest to include this, or something similar in the README file of the project.

This certainly helped me and next time it will be easier to set up a development environment for an R-based project.


