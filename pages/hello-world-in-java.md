---
title: "Hello World in Java"
timestamp: 2018-01-03T20:30:01
tags:
  - java
  - javac
published: true
books:
  - java
author: szabgab
archive: true
---


The standard way to get started with any language is to write a program that will print "Hello World". Here is the one for Java.

For other languages see the [Hello World exercise](/exercise-hello-world).


## Install Java

You can [download Java](https://java.com/en/download/) in two main forms.

The JRE - Java Runtime Environment (Java Virtual Machine JVM) is needed to run a pre-compiled
Java application.

The JDK - Java Development Kit (Java Compiler javac) includes the compiler that converts source files with .java extension to compiled files with .class extension. It also include the Runtime Environment.

For develpment you'll need the JDK. The users of your code will only need the JRE.

## Command line

In these article we will use the command line and not any IDEs so let's look at the
command line tools we get when we install the JDK:

Once you have downloaded and installed the JDK you have two command-line tools:

`javac` is the Java compiler. If you run `javac -version` it will display

```
$ javac -version
javac 1.8.0_60
```

`java` s the runtime environment or `Java Virtual Machine`.

```
$ java -version
java version "1.8.0_60"
Java(TM) SE Runtime Environment (build 1.8.0_60-b27)
Java HotSpot(TM) 64-Bit Server VM (build 25.60-b23, mixed mode)
```

## Hello World

Now that we have the tools ready we can creat the following file in any text editor
(e.g.even Notepad if you are really hard-core)

{% include file="examples/java/HelloWorld.java" %}

The we switch to the terminal (or command prompt in Windows) `cd` to the directory
where we saved the `.java` file and run:

```
$ javac HelloWorld.java
```

this fill create a file called `HelloWorld.class` but won't print anything to the screen.

Then we can run our application using:

```
$ java HelloWorld
Hello World
```

## Troubleshooting

A couple of issues I've encountered while making these first steps:

I've tried to run `javac` only giving the name of the file without the extension:

```
$ javac HelloWorld
error: Class names, 'HelloWorld', are only accepted if annotation processing is explicitly requested
1 error
```

Passed the filename including the extension to the `java` program which only needs the name of the file without the extension:

```
$ java HelloWorld.class
Error: Could not find or load main class HelloWorld.class

$ java HelloWorld.java
Error: Could not find or load main class HelloWorld.java
```

