# After Hello World - list containers


no running containers, but there is one on the disk:

```
$ docker container ls -a -s
$ docker container ls -as
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES               SIZE
f6239f10a6ad        hello-world         "/hello"            8 seconds ago       Exited (0) 7 seconds ago                       lucid_snyder        0 B (virtual 1.84 kB)
```

Older spelling for the same command:

```
docker container ps
docker ps
```

* I keep fortgeting what does that `-s` do, so I run:

```
$ docker container ps --help
```


