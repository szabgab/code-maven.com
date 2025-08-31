---
title: "What ports are open on Linux - which application uses which port"
timestamp: 2019-04-23T18:30:01
tags:
  - netstat
  - top
  - htop
  - ps
published: true
author: szabgab
archive: true
---



```
htop
```

To see what interesting processes are running:

```
ps axuw
```


[find out what ports are open](https://www.cyberciti.biz/faq/how-do-i-find-out-what-ports-are-listeningopen-on-my-linuxfreebsd-server/)

```
netstat --listen
```

```
sudo netstat -tulpn
```


