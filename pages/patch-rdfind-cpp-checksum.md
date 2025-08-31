---
title: "Patch rdfind, a C++ project to avoid checksum checking"
timestamp: 2022-09-19T13:30:01
tags:
  - C++
  - cpp
  - rdfind
types:
  - screencast
published: true
author: szabgab
archive: true
show_related: true
---


Recently I was trying to clean up my backup disks and realized I have a mess.
So first I started to upload everything to Dropbox, but soon I realized I have lots of files in 2, 3, sometimes even 4 copies.
I was looking for a tool that will allow me to locate the duplicate files and found [rdfind](https://rdfind.pauldreik.se/).


{% youtube id="HJ9sHwZnOSQ" file="patch-rdfind-cpp-checksum.mp4" %}

It is nince. It first goes over the directory structure I give it on the command line and then starts to filter files.
* First it will eliminate all the files that have a unique size
* Then it will compare the first few bytes of the files that have the same size
* Then it will compare the last few bytes of the file that have the same size
* Finally, among the still remaining candidates for equality it will compare their checksum using md4 or sha1

The problem I had is that I have many huge files. Quite a few are larger than 1 Gb and many over 10 Gb. I have about 2TB data.

It takes a lot of time to go over all the files, especially computing the checksums takes a lot of time as the files need to be read.

Add to the injury that many of these files are still located on slow-to-access external disks.

I thought it would be better if I could skip the checksum step, but there was no such flag.

So what can I do.

First I [opened a ticket](https://github.com/pauldreik/rdfind/issues/118) explaining my issue, but then I thought, what if I
try to implement it?

I clones the source code. It seems it is written in C++. I've never written C++ and even with C I have very little experience.

```
git clone git@github.com:pauldreik/rdfind.git
```

## Try to compile

The next thing I had to find is how to compile the code. After a few failed experiments I ran

```
grep release *
```

and found the `release_new_version.txt` that contained the instructions:

```
git clean -xdf .
./bootstrap.sh
./configure
make dist-gzip
```


The first problem I encountered was a missing package. I had to install it:

```
sudo apt-get install nettle-dev
```


Then I bumped intor the following error when running <b>make</b>:

```
$ make
make  all-am
make[1]: Entering directory '/home/gabor/work/rdfind'
g++ -DHAVE_CONFIG_H -I.     -g -O2 -MT rdfind.o -MD -MP -MF .deps/rdfind.Tpo -c -o rdfind.o rdfind.cc
rdfind.cc: In function ‘Options parseOptions(Parser&)’:
rdfind.cc:225:30: error: ‘numeric_limits’ is not a member of ‘std’
  225 |     o.maximumfilesize = std::numeric_limits<decltype(o.maximumfilesize)>::max();
      |                              ^~~~~~~~~~~~~~
rdfind.cc:225:45: error: expected primary-expression before ‘decltype’
  225 |     o.maximumfilesize = std::numeric_limits<decltype(o.maximumfilesize)>::max();
      |                                             ^~~~~~~~~~~~~~~~~~~~~~~~~~~
make[1]: *** [Makefile:658: rdfind.o] Error 1
make[1]: Leaving directory '/home/gabor/work/rdfind'
make: *** [Makefile:537: all] Error 2
```

Luckily a little search for the error message brought me to [this page](https://www.mail-archive.com/debian-bugs-dist@lists.debian.org/msg1826627.html).
Not surprisingly I am not the first one to see this error. Better yet, apparently it has already been fixed in a branch.

So I using `git branch -a` I checked and saw that there is a branch called <b>devel</b>. I switched to that branch and ran the whole process again.
This time `make` worked and it create a file called `rdfind` in the root directory of the project.

Now that I knew I can compile and build the executable I started to look at the code.

First I wanted to find where it processes the command-line parameters so I'll be able to add a parameter called `-nochecksum`.

I searched for the string "argv" as that is the name of the variable that holds the command-line parameters in many languages.
Quite soon I found that is it in the `rdfind.cc` file.

{% include file="examples/rdfind-checksum.diff" %}

At the end I felt it is better to change the already existing `-checksum</hl` flag and allow it to receive the value "none"
to avoid the checsum calculations.

I was lazy and did not add any new tests, but it could be done later if the author of the code requests it.

After making the change I pushed out the code to my forked repository of the project. The GitHub Actions were triggered and I saw that
all the tests pass.

I was very pleasantly surprised by the ease of finding the instructions how to build the code, the existing tests and the ease to make
the adjustments.

We'll see if the Pull-Request is accepted.


