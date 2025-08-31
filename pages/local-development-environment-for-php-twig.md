---
title: "Setup local development environment and run tests of PHP Twig"
timestamp: 2023-03-19T10:00:01
tags:
  - PHP
published: true
books:
  - php
author: szabgab
archive: true
show_related: true
---


I believe that removing obstacles from contribution to an open source project is one of the keys to getting more contributors.

Having a good description of the contribution process and the culture of the development team is crucial, so is making it easy for a new potential developer to set up the local development environment and run the tests of a project locally.

It took me a while to find a PHP project that was simple enough for me to set up on a single Docker image, but after some trial and error I found the [Twig](https://twig.symfony.com/) project.

Funnily, only now, after managing the setup and staring to write this post did I realize that it is part of the [Symfony](https://symfony.com/) project.


Anyway, I won't bother you with all the failed attempts I had till I get to this:

## clone

Clone the [Git repository of Twig](https://github.com/twigphp/Twig)

```
git clone git@github.com:twigphp/Twig.git
```


## Docker container

Start a plain Ubuntu-based docker container in interactive mode and map the current working directory to the /opt directory inside the container.

My host system is itself an Ubuntu Linux machine. The command should also work on macOS.

I have not tried it, but I think MS Windows users will have to replace the "-v$(pwd):/opt" part by ```-v %cd%:/opt</code> if using cmd or by <code>-v ${PWD}:/opt</code> if using PowerShell.


```
docker run -it --rm --workdir /opt -v$(pwd):/opt ubuntu:22.10 bash
```

## Install PHP and tools

First we update the list of available Ubuntu packages.

Then we install <b>tzdata</b>. Normally it would ask questions during installation. The two environment variables provide the values to these questions.

Finally we install the command line version of php (no web server is needed for this project), [composer](https://getcomposer.org/) which is a package management system for PHP and <a 
href="https://phpunit.de/">PHP Unit</a>, the testing framework of PHP.

```
apt-get update
DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
apt-get install -y php-cli composer php-curl phpunit
```


## Install dependencies

The projects uses <b>composer</b> to manage its dependencies so this is how we install them.

```
composer install
```

## Run tests

Finally we can run the tests.

```
phpunit
```

## Test results

As I write this post the tests fail with the following:

```
Time: 00:01.136, Memory: 36.00 MB

There were 2 failures:

1) Twig\Tests\Cache\FilesystemTest::testWriteFailMkdir
Failed asserting that exception of type "RuntimeException" is thrown.

2) Twig\Tests\Cache\FilesystemTest::testWriteFailDirWritable
Failed asserting that exception of type "RuntimeException" is thrown.

FAILURES!
Tests: 1663, Assertions: 4399, Failures: 2, Skipped: 4.

Legacy deprecation notices (3)
```

At this point I could use the editors and IDEs I have on my host system to edit the files of the project and then rerun the tests, but that I'll leave for someone else.

## Quit the docker container

It is simple to exit from the Docker container. Because we used the ```--rm</code> flag when we started the container, Docker will automatically remove it.

```
exit
```


## Clean the git workspace

Running the composer and phpunit command created some files on the disk, the following command can remove them.
I had to use <b>sudo</b> here as Docker created those files as user root.

```
sudo git clean -dxf
```

In case you were wondering which files and folders were added by those two commands, this was the output of the git clean command:

```
Removing .phpunit.result.cache
Removing composer.lock
Removing vendor/
```

## Conclusion

I hope this will help someone set up the development environment.

As I think this information should be part of the project I'll open an issue pointing to this article and offering to send a Pull-Request to add the content of it to their documentation.


