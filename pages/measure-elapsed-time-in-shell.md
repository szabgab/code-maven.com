---
title: "Measure elapsed time in Linux shell using time and date"
timestamp: 2019-01-25T07:30:01
tags:
  - time
  - date
published: true
author: szabgab
archive: true
---


There are two main cases:

If you have a command and you'd like to know how much it takes you can use the `time` command.  Measure time
externally.

If you have a script and you'd like to measure how much various parts of it take you can use the `date` command.
Measure time internally.


## Measure elapsed time internally in a script

This is the other type of elapsed time measuring.

{% include file="examples/shell/measure_time.sh" %}

The output:

```
It took 1 seconds to sleep of 1 second...
```


## Measure elapsed time externally

Let's say you have a command such as `run_this_thing` and you'd like to measure how long it takes to run.
You can run it as

```
time run_this_thing
```

This will run the program and after the program has finished it will print something that looks like this:

```
real  0m14.806s
user  0m0.089s
sys   0m0.019s
```

It tells us that the job took 14 seconds `real` time to run. This is what is sometimes referred to as wallclock time. This is the
time you could have measured with your personal stop-watch.

The `user` time is what the process spent in user mode (e.g. computing in memory).

The `sys` time (aka. system time) it the process spent using system calls. (e.g. the CPU time of accessing the
file-system, the screen, or the network, etc.), but excluding the time the Operatng System was waiting for the disk
or the network to send the data, or the screen to display it. Also excluding the time it was waiting for the Operating
Sytem to allocate CPU time to it.

All the time while the process was not actually using CPU but was waiting for something is in the `real` time.

So the above results mean that the process I ran was mostly waiting for some IO to finish. (In fact this was an ssh
command that executed something on a remote computer. So the computer I was running on hardly used its CPU. It was
mostly waiting for the other computer to finish its job and send a response.


On a single core (single cpu) system this would be the formula:

```
sys + user + IO_time = real
```


So you could calculate the IO_time from the 3 numbers given by `time`.

On a multi-core system however both `sys` and `user` contain the combined time spent on all of the cores.
This means that both sys and user might be higher than the real time.

e.g. this result on a 4-core system probably means that each core spent 1 sec in `user` mode and 1 sec in
`sys`. So each core was used for 2 seconds, but that happened in parallel, so only 2 seconds of your life
was used.

```
real  0m2.000s
user  0m4.000s
sys   0m4.000s
```

Of course this cannot really happen as there are other things running on your compuuter that take time so your process
won't be able to use 100% of each core.
So the real time will be longer. The following seems to be possible:

```
real  0m2.500s
user  0m4.000s
sys   0m4.000s
```

Here, the 2 seconds per each CPU were executed within a 2.5 seconds timeframe.


