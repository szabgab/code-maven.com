# Run PostgreSQL in Docker


```
docker run --name pg1 -e POSTGRES_PASSWORD=secret -d postgres
```

```
docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED              STATUS              PORTS               NAMES
8bfa343f4f3e        postgres            "docker-entrypoint.s…"   About a minute ago   Up About a minute   5432/tcp            pg1
```

* Run PostgreSQL in a Docker container and expose it to the local macine via the standard 5432 port.
* Here we picked a specific version of postgres.
* We also set the credentials.

```
docker run -d --name pgserver -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=secret -e POSTGRES_DB=mydb -p 5432:5432 postgres:18
```

* Access using the `psql` client that comes inside the same image.
* We use the `$HOSTNAME` of our host computer.

```
docker run --rm -it postgres:18 psql "host=$HOSTNAME port=5432 dbname=mydb user=myuser password=secret"
```

This shows a prompt where you can type in various SQL commands.

```
mydb=# SELECT CURRENT_TIME;
mydb=# SELECT CURRENT_DATE;
```

With `Ctrl-D` quit the client.

with the following command shut down the server:

```
docker container stop pgserver
```


