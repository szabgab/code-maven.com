# Simple docker commands


Empty state, no images:

no running containers

```
$ docker container ls

CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

no local containers at all (including not running, and showing the size)

```
$ docker container ls -as

CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```

not even images

```
$ docker images

REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
```

Commands

```
$ docker ps
$ docker ps -as    list all the containers available locally  (incl the size)
$ docker images    list images
```


