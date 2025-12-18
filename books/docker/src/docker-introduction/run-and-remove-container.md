# Run and remove container using the `--rm` flag


```
$ docker run --rm busybox echo hello world
```

After the above command finished check it:

```
$ docker container ls -a
```

The container was not left around.

