---
title: "MasterMind"
timestamp: 2018-04-20T18:30:01
tags:
  - exercises
published: true
books:
  - exercise
author: szabgab
archive: true
---


Implement the [MasterMind](https://en.wikipedia.org/wiki/Mastermind_(board_game)) game.



The computer "thinks" a string with 4 different digits. You guess which digits.
For every digit that matched both in value, and in location the computer gives you a *.
For every digit that matches in value, but not in space the computer gives you a +.


Try to guess the given number in as few guesses as possible.

```
Computer: 2153
You:      2467  *
You:      2715  *++
```

