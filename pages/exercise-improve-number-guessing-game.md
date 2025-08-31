---
title: "Exercise: Improve Number guessing game"
timestamp: 2015-10-25T20:20:01
tags:
  - exercises
  - projects
published: true
books:
  - ruby
  - python
  - javascript
  - php
author: szabgab
archive: true
---


This is an extension of the <a href="">Number guessing game exercise</a>.


This exercise has several steps.

First of all, let the user guess several times (with responses each time), until she finds the hidden number.

Allow various special keys too:
* n - skip the rest of this game (give up) and start a new game with new hidden number.
* s - show the hidden value (cheat).
* m - toggle: turn on/off move mode: When the move mode is on, after every guess the number can change by 2 in either direction.
* d - toggle: turn on / off debug mode. In debug mode show the hidden number every time before you are asked to supply the guess.
* x - exit

Now I can tell you that this is actually a 1 dimensional space fight. The number is your distance from the enemy space ship.

For training purposes limit the outer space to be between 0-200 so even when the move mode is on the space-ship won't fly off this area.

Finaly, keep track of the minimum and maximum score (number of guesses till hit) in a file.

## Tools

* 

## Solutions

* [Perl 5: Improve the number guessing game - multiple guesses](https://perlmaven.com/beginner-perl-maven-solution-number-guessing-game-multiple-guesses)
* [Perl 5: Improve the number guessing game - exit](https://perlmaven.com/beginner-perl-maven-solution-number-guessing-game-exit)
* [Perl 5: Improve the number guessing game - s for show](https://perlmaven.com/beginner-perl-maven-solution-number-guessing-game-s-show)
* [Perl 5: Improve the number guessing game - n for next game](https://perlmaven.com/beginner-perl-maven-solution-number-guessing-game-n-next-game)
* [Perl 5: Improve the number guessing game - d for debug mode](https://perlmaven.com/beginner-perl-maven-solution-number-guessing-game-d-debug-toggle)
* [Perl 5: Improve the number guessing game - m for move mode](https://perlmaven.com/beginner-perl-maven-solution-number-guessing-game-m-move-toggle)
