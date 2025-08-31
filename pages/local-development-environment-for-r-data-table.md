---
title: "Local development environment for the data.table R project"
timestamp: 2023-03-20T11:30:01
tags:
  - R
published: true
books:
  - R
author: szabgab
archive: true
show_related: true
---


After the partial success with the [development environment for R-yaml](https://code-maven.com/development-environment-for-r-yaml) we tried another R package
called [data.table](https://github.com/Rdatatable/data.table). Eventually we managed to run the tests of this too.


This one actually had a lot of details in the README, but some parts were still missing, or at least were assumed to be obvious, which was not the case for us.

## Clone the repo

```
git clone git@github.com:Rdatatable/data.table.git
cd data.table
```

## Start Docker container

```
docker run -it --name data-table --workdir /opt -v$(pwd):/opt r-base:4.2.3 bash
```

## Install external dependencies we'll need

```
apt-get update
apt-get install -y pandoc curl libcurl4-gnutls-dev texlive-latex-base texlive-fonts-extra texlive-latex-recommended texlive-fonts-recommended
```

## Install R packages

```
Rscript -e 'install.packages(c("knitr", "rmarkdown", "pandoc", "curl", "bit64", "bit", "xts", "nanotime", "zoo", "R.utils", "markdown"))'
```


## Run the build

```
R CMD build .
```

## Run check on the generated file

In the README they mention <b>data.table_1.11.5.tar.gz</b>, but probably due to a change in the version number, now we have <b>data.table_1.14.9.tar.gz</b>

We can run this

```
R CMD check data.table_1.14.9.tar.gz
```

But if the README is updated with this then it will be out of date soon. Instead there could be an explanation that one needs to look at the generated file.
Alternatively this command would pick up the current file, assuming there is only one of them.

```
R CMD check $(ls -1 data.table_*)
```


## Exit the Docker container

```
exit
```


## Restart the Docker container

```
docker container start -i data-table
```


## Remove Docker container

```
docker rm data-table
```


