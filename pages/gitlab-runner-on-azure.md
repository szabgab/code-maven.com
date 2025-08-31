---
title: "GitLab runner on Azure"
timestamp: 2021-07-11T10:30:01
tags:
  - GitLab
  - Azure
  - CI
published: false
author: szabgab
archive: true
show_related: true
---



Create an account on [Azure](https://azure.com)

Create a Virtual machine (I used a Standard_B1 with 1 vcpu and 1 Gb memory that costs $7.59 / month)
I have added my public key in order to make it easy to ssh to the box.
Once it was ready I logged in:

```
ssh azureuser@20.106.137.104
```

Inside I can run "sudo" commands without providing a password. In fact I don't even have a password for any of the users on this machine.


<a href="/build-docker-image-in-gitlab-pipeline"></a>


