# Run, stop, resume container

Start a new container and using `--name` give it an explicit name so it will be easy to find it.

```
$ docker run --name demo -it busybox
```

Create file and list it

```
# echo "hello world" > foobar.txt
# cat foobar.txt
```

Then exit the container:

```
# exit
```

List the containers, and observe that the one we had is stopped.

Restart the same container:

```
$ docker container start -i demo
```

Check that the file we created in the previous session is still there.

```
# cat foobar.txt
```

