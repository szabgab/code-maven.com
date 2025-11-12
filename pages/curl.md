---
title: Curl examples
timestamp: 2025-11-12T08:30:01
tags:
  - curl
  - http
  - httpbin
published: true
author: szabgab
archive: true
---

## Run httpbin locally

Start as:

```
docker run --rm -p 80:80 --name httpbin kennethreitz/httpbin
```

Then run the curl commands

```
curl
```

To stop the Docker container open another terminal and execute

```
docker container stop -t0 httpbin
```


## 301 MOVED PERMANENTLY

$ curl -i http://localhost/status/301
HTTP/1.1 301 MOVED PERMANENTLY
Server: gunicorn/19.9.0
Date: Fri, 26 Sep 2025 10:32:08 GMT
Connection: keep-alive
location: /redirect/1
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Content-Length: 0

## 303 SEE OTHER (redirect)

```
$ curl -i http://localhost/status/303
HTTP/1.1 303 SEE OTHER
Server: gunicorn/19.9.0
Date: Fri, 26 Sep 2025 10:06:22 GMT
Connection: keep-alive
location: /redirect/1
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Content-Length: 0
```

## 404 NOT FOUND

```
$ curl -i http://localhost/status/404
HTTP/1.1 404 NOT FOUND
Server: gunicorn/19.9.0
Date: Fri, 26 Sep 2025 10:08:19 GMT
Connection: keep-alive
Content-Type: text/html; charset=utf-8
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Content-Length: 0
```


