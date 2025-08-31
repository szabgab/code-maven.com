---
title: "One dimensional spacefight (aka. The spaceship operator)"
timestamp: 2018-04-20T16:30:01
tags:
  - CodeMaven
published: true
books:
  - exercise
author: szabgab
archive: true
---


You are the pilot of a spaceship and your task is to fire upon and hit the enemy spaceship.

You are in one-dimensional space.



## Level 0

* The computer creates a random integer number between 0-100 "the space" which is the distance of the spaceship from you
* You guess the distance by typing in a number.
* The computer write if it is a hit or not

## Level 1

* The computer can tell you if your shot was too short or too long.
* The computer will allow you to shoot multiple times.

## Level 2

* If the user hits x, s/he leaves the game without finishing it.

## Level 3

* If the user presses 's', show the hidden value (cheat)
* If the user presses 'd' the game gets into debug mode: the system starts to show the current number to guess every time, just before asking the user for new input. Pressing 'd' again turns off debug mode. (It is a toggle.)

## Level 4

* The 'm' button is another toggle. It is called 'move mode'. When it is 'on', the object move a little bit after every step (+/-2). Pressing 'm' again will turn this feature off.

## Level 5

* Let the user guess several times.
* Pressing 'n' will skip this game and start a new one (generate new number to guess).


```
Allow the user to type
n   - skip this game and start a new one (generate new number to guess)
s   - show the hidden value (cheat)
d   - debug mode 
      (It is a toggle. 
       Pressing once the system starts to show the current
       number to guess every time before asking the user for new input
       pressing again, turns off the behavior.
       )
m   - move mode
      (It is a toggle.
       Pressing once the object will start to move a little bit after
       every step. Pressing again will turn this feature off.)
x   - exit
```

* Make the size of the space configurable.
* Make sure the enemy does not wander off the training field.
* Give warning if the user shoots out of space.
* Keep track of the minimum and maximum number of hits (in a file or database).

## Level

Refactor the code to be nice small functions e.g. for

* moving of the spaceship
* checking the hit

