---
title: "Live Crystal Shardbox development with Johannes Müller (straight-shoota)"
timestamp: 2021-06-23T21:30:01
tags:
  - Crystal
  - Shardbox
types:
  - screencast
published: true
books:
  - crystal
author: szabgab
archive: true
show_related: true
---


Live [Crystal](https://crystal-lang.org/) [Shardbox](https://shardbox.org/) development with
[Johannes Müller](https://www.linkedin.com/in/johannes-m%C3%BCller-b4929786/) ([straight-shoota](https://github.com/straight-shoota))

The resulting [Pull Request](https://github.com/shardbox/shardbox-web/pull/9)


{% youtube id="hlC88df4qqM" file="crystal-shardbox-with-johannes-muller-2021-06-23.mp4" %}

* [0:00 Welcome, a bit of background.](https://youtu.be/hlC88df4qqM?t=0)
* [1:10 Johannes introduces himself.](https://youtu.be/hlC88df4qqM?t=70) he works at [Manas Tech](https://manas.tech/)
* [3:30 Gabor introduces himself.](https://youtu.be/hlC88df4qqM?t=210)
* [6:00 Gabor is trying to explain what does Shardbox do.](https://youtu.be/hlC88df4qqM?t=360)
* [14:00 Explaining the Shardbox catalog.](https://youtu.be/hlC88df4qqM?t=840)
* [20:55 Explaining the Shardbox core.](https://youtu.be/hlC88df4qqM?t=1255)
* [22:00 Schema overview](https://youtu.be/hlC88df4qqM?t=1320)
* [39:30 Explaining about the code of Shardbox core](https://youtu.be/hlC88df4qqM?t=2370)
* [48:25 Setting up the development environment - PostgreSQL in Docker](https://youtu.be/hlC88df4qqM?t=2905)
* [58:50 Install Crystal dependencies for the Shardbox core (till 1:14:30)](https://youtu.be/hlC88df4qqM?t=3590)
* [1:16:20 Build the worker](https://youtu.be/hlC88df4qqM?t=4580)
* [1:22:40 Start setting up the Shardbox web application](https://youtu.be/hlC88df4qqM?t=4960)
* [1:29:15 We have Shardbox running on my computer!](https://youtu.be/hlC88df4qqM?t=5355)
* [1:33:50 Change the Jinja templates to add links to the licenses](https://youtu.be/hlC88df4qqM?t=5630)
* [1:36:45 Change the search route to accept the new parameter](https://youtu.be/hlC88df4qqM?t=5805)
* [1:57:00 Showing the query on the search result page](https://youtu.be/hlC88df4qqM?t=7020)
* [2:03:00 Commit the changes, send pull-request.](https://youtu.be/hlC88df4qqM?t=7380)
* [2:09:10 Plans for Shardbox](https://youtu.be/hlC88df4qqM?t=7750)



Schema overview is in this file: db/schema-overview.svg in the [shardbox-core repository](https://github.com/shardbox/shardbox-core).

The <b>catalog</b> directory in the [catalog](https://github.com/shardbox/catalog) repository contains the manually mapped shards.

## PostgreSQL in Docker

Start running the Docker container:

```
docker run -v$(pwd):/opt --name shardbox -e POSTGRES_PASSWORD=Secret -d postgres
```

Connect to the container:

```
docker exec -it shardbox bash
```

In the container:

```
cd /opt
apt-get update
apt-get install make
PGUSER=postgres TEST_DATABASE_URL=postgres://postgres:Secret@localhost/shardbox_test make test_db
```

At the end of the session working on sharbox you can stop the container:

```
docker stop shardbox
```

Packages we had to install (on the Ubuntu host)

```
sudo apt-get install libsass-dev
sudo apt-get install postgresql-client
sudo apt-get install libgit2-dev
```

Get the IP address of the Docker container:

```
docker inspect shardbox
```

Use that IP address in the following commands:

We checked if we can access the database using psql:

```
psql postgres://postgres:Secret@172.17.0.2/shardbox_test
```

Running the tests of shardbox-core:

```
export TEST_DATABASE_URL=postgres://postgres:Secret@172.17.0.2/shardbox_test
export SHARDS_OPTS=--ignore-crystal-version
# make test # this did not work
crystal spec
```


Build the worker

```
make build
```

Setting up for development database:

```
export DATABASE_URL=postgres://postgres:Secret@172.17.0.2/shardbox_test
```

Create a [Personal access token](https://github.com/settings/tokens) with a name that you can easily recognize, e.g. "Shardbox Development Token" using the following rights:

```
repo
   x public_repo

user
   x read:user
   x user:email
```

```
export GITHUB_TOKEN=...
./bin/worker
./bin/worker import_catalog ../shardbox-catalog/catalog/
```

Importing the whole catalog can take a lot of time so we copied a single file from the catalog
and ran on it. I would think a flag to limit the number of shards to be imported would help here.

```
mkdir catalog/
cp ../shardbox-catalog/catalog/Web_Servers.yml catalog/
./bin/worker import_catalog catalog/
```

One can also update the metrics:

```
./bin/worker update_metrics
```


## Building the web applicaton in shardbox-web

```
SHARDS_OPTS=--ignore-crystal-version make build
```

Only the web application:

```
SHARDS_OPTS=--ignore-crystal-version make bin/app
```

Run the web application

```
./bin/app
```

Format the source code:

```
crystal tool format
```


<!--
Scheduled for <span id="localdate" x-schedule="2021-06-23T16:00:00+03:00"></span>

<a class="btn btn-lg btn-success" href="https://us02web.zoom.us/meeting/register/tZEuceuprT8iGNLbQHGEeE10-rDF0HNSh-pJ">Register here</a>

Check out all the other [live](https://code-maven.com/live) events and the calendar where you'll be able to see the time given in your time-zone.
-->


