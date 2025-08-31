---
title: "Improve the compilation time of your project!"
timestamp: 2018-04-04T11:30:01
tags:
  - DevOps
published: true
author: szabgab
archive: true
---


In order to improve the speed of software development one needs to be able to create faster development cycles and provide a shorter feedback loop. One of the ways to improve the development cycles is to reduce the time it takes to compile the project - if it is in a language where compilation is necessary.

The Linux kernel has 20 million lines of C code and I've just compiled in in 36 minutes on an old 4-core machine. PostgreSQL has 1 million lines of code and most of the build farm machines report 8-12 minute build time.

<b>How long does it take to compile your software?</b>


For comparison here are two Open Source projects:

## How long does it take to compile the Linux kernel?

The Linux kernel has about 20 million lines of C code according to both the
[Linux counter](https://www.linuxcounter.net/statistics/kernel) and the
[OpenHub for Linux](https://www.openhub.net/p/linux).

The compilation time will largely depend on the the configuration you have, so this number
is not representative but I've just compiled it on an old 4-core machine and this is what `time` reported:

```
real    36m49.545s
user    130m15.245s
sys     9m35.052s
```

So it used the 4 cores very well and it took 36 minutes to compile the kernel.

## How long does it take to compile PostgreSQL?

According to the [OpenHub on PostgreSQL](https://www.openhub.net/p/postgres) it has about 1 million lines of C code.

Most of the machines in the [PostgreSQL build farm](https://buildfarm.postgresql.org/) report around 12-14 minutes. That includes both compilation and testing! Some machines took longer and a few ran in 8 minutes. I assume the differences are primarily due to the number of cores used in parallel.

## Some related articles

* [Reducing compilation times for D](https://medium.com/tripaneer-techblog/reducing-compilation-times-ca524484beeb)
* [Why is the new C++ visibility support so useful?](https://gcc.gnu.org/wiki/Visibility)

