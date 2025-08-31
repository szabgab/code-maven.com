---
title: "Calculator in Java"
timestamp: 2018-04-28T08:30:01
tags:
  - java
  - javac
published: true
books:
  - java
author: szabgab
archive: true
---


The [Calculator exercise](/exercise-calculator) is a basic exercise to show how Input/Output
works in a language, how one can use basic numerical operation. In some languages it is eaier than in others.


## Arguments on the command line

In this solution we receive the 2 numbers and the operator on the command line.

{% include file="examples/java/ArgsCalculator.java" %}

The command

```
javac ArgsCalculator.java
```

will compile the Java clode and create a file called ArgsCalculator.class

Then we can run it as

```
java ArgsCalculator 2 + 3
```

The result will be 5.

```
java ArgsCalculator 7 - 3
```

works as well and prints 4.

If we would like to multiply numbers we have to be careful.

```
java ArgsCalculator 7 * 3
```

would print an exception like this:

```
Exception in thread "main" java.lang.NumberFormatException: For input string: "ArgsCalculator.java"
	at java.lang.NumberFormatException.forInputString(NumberFormatException.java:65)
	at java.lang.Integer.parseInt(Integer.java:580)
	at java.lang.Integer.parseInt(Integer.java:615)
	at ArgsCalculator.main(ArgsCalculator.java:6)
```

That's because the `*` on the command line is interpreted by the shell as a wide-card character and it is replaced by the names of all the files in the current directory. So the shell will actually call something like this:

```
java ArgsCalculator 7 ArgsCalculator.java ArgsCalculator.class HelloWorld.java 3
```

Assuming we have those 3 files in the current directory. That in turn will trigger an exception on our code as it tries
to parse the string "ArgsCalculator.java" into an integer.

This problem is caused by the shell interfering with our businees.

In order to avoid this we need to tell the shell to pass the `*` as it is. For this we need to but it in quotes:

```
java ArgsCalculator 7 '*' 3
```

will print 21.

Finally we also have to accept that the division as it is in this code will work as an integer division. So

```
java ArgsCalculator 21 / 3
```

is 7, but

```
java ArgsCalculator 22 / 3
```

is also 7 as Java will only keep the integer part of the division.

## Explanation

The `args` array will hold the values passed on the commad line. `args[0]` is the first element of the array.

`Integer.parseInt` can convert a string into an integer number.

`int` is used to decalare a variable as integer.

`String` is used to declare a variable as string.

`if` has its condition in parentheses and the code in curly braces.

`else if` allows us to attach more, alternative conditions.

`throw new java.lang.Error("...")` will raise an exception in case the user supplied an operator we don't handle.

## Read from Standard Input STDIN

In this alternative soluton, instead expecting the operands and the operator on the command line,
we ask the user to type the values in during the execution of the program.

{% include file="examples/java/InputCalculator.java" %}

An interaction would look like this:

First compile the code:

```
$ javac InputCalculator.java
```

Then run the application:

```
$ java InputCalculator
First number: 23
Second number: 19
Operator: +
Result: 42
```


The interesting difference here is the use of
`System.in` which represents STDIN, the `InputStreamReader`
and the `BufferedReader` classes to read from the input channel.


