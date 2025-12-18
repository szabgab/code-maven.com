# Run an interactive sesson using the -it flags

```
docker run -it busybox
```

Inside the docker container try various linux commands, but do NOT exit the container.

```
# pwd
# ls -l
# uptime
# echo hello world
```

* `-i` makes the sessin interactive.
* `-t` allocates a pseudo TTY so we can actually see something.



