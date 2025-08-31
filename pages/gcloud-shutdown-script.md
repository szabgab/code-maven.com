---
title: "Google Cloud shutdown script"
timestamp: 2019-05-17T07:30:01
tags:
  - GCP
  - shutdown
published: true
author: szabgab
archive: true
---


When you shut down a compute intance manual via the console, using gcloud, or when an a preemptible instance is
automatically shut down, you can arrange for a script to be executed.

In normal shutdown situation the script has 90 seconds to run, in preemptible automatic shutdown it has 30 seconds to
run before the computer is really shut down.


In order to try this

* Make sure your instance can access the internet.
* ssh to the instance and run the following command to verify: `curl -s https://httpbin.org/get?time=$(date +%s)`
* Follow the [instructions to add a shutdown-script](https://cloud.google.com/compute/docs/shutdownscript)
* start the instance, shut it down, start it again
* check if /root/out.txt has been generated and if its content is similar to what the original curl returned.

The shutdown-script:

```
while true; do curl -s https://httpbin.org/get?time=$(date +%s) >> /root/out.txt ; sleep 5; done
```



