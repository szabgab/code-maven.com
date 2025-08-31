---
title: "Python: Repeat the same random numbers using seed"
timestamp: 2019-01-14T14:30:01
tags:
  - random
  - seed
published: true
author: szabgab
archive: true
---


Python has a module called [random](https://docs.python.org/library/random.html) that can provide
[pseudo random numbers](https://en.wikipedia.org/wiki/Pseudorandom_number_generator).

In a nutshell that means that the numbers seem to be random and can be used for various applications as if they were
indeed random, but in fact they are just a really strange series of fixed numbers.


That means you should not use them for certain types of applications, e.g. encryption and that they are
<b>repeatable</b>.

If you start from the same place in the series twice, then you get the exact same "random" numbers.

The way to set this beginning in the `random` module of python is to call the `random.seed()`
function and give it an arbitrary number. e.g. 42 would be perfect.

Let's see this!

In this simple script we just load the `random` module and called the `random.random()` method.

{% include file="examples/python/fixed_seed/single_random.py" %}

Every time we run this script we get a different number.

```
0.511318181959
0.771417342337
0.565304847619
```

This happens because when python loads the `random` module it calls the `seed` function with the current
time. As that time always changes the casual viewer would see random numbers.

{% include file="examples/python/fixed_seed/single_random_fixed_seed.py" %}

If we run this script several time we'll always get back the same "random" number.

```
0.639426798458
0.639426798458
0.639426798458
```

## Why are repeatable "random" numbers a good thing?

You might ask. Well, they are good if you would like to make sure you can run the same
sequence of events while they are (almost) randomly created. For example when you write
some test code. With tests you usually want the process to be repeatable.

So if you have a function that uses random numbers to calculate something and for every call it will
return a different result then it is hard to check if it works properly. If you fix the random numbers
then you will be able to observe the same result twice.

Anyway, what happens if your code loads other modules that also use random numbers?


Here we have a main file:

{% include file="examples/python/fixed_seed/main.py" %}

That loads the other.py:

{% include file="examples/python/fixed_seed/other.py" %}

If we run `python main.py` several time we'll get different number-pairs on every run:

```
0.864327113674
0.675706432586

0.221254773857
0.0473047970533

0.415061037659
0.718553482388
```


If we enable the call to `random.seed(42)` we get the same two numbers on every run:


```
0.639426798458
0.0250107552227

0.639426798458
0.0250107552227

0.639426798458
0.0250107552227
```


