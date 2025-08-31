---
title: "The Spaceship Operator"
timestamp: 2015-06-01T12:06:01
tags:
  - Casio
published: true
author: szabgab
archive: true
---


A long time ago, in a country far, far away, when I was still a teenager, at the dawn of the personal computing age,
my parents bought me a [Casio FX-702P](http://en.wikipedia.org/wiki/Casio_FX-702P).

I've made my first steps programming on this device. I did not understand it back then, but the feeling that I can
make that thing do what I want was enormous. I taught myself programming by writing a game. A very simple game.

This game turned into a career and a hobby. I am one of the lucky people who makes a living with something I really enjoy.

Programming and teaching programming.

In this series of articles I plan to show you how to build that game in a modern computing environment in the hope
that you will also fall in love with it.


## Prerequisites

The prerequisites of this series is deliberately minimal: You need to have access to a computer.

That's it.


## The Game

I call the game <b>The Spaceship operator</b> partially as a wink to the similarly named operators in some of the programming languages.
But never mind.

The game is very simple, you might imaging something I could build on that device, but in this series we are going to extend it in all
kinds of directions.

The core of the game is that there is a spaceship out there and you need to shoot it down. You know that the spaceship is between 1-200
units away. You aim, shoot, and the computer tells you if you have hit the target, if your shot was too short or too long.
If you have not hit the target you can adjust and shoot again till you hit the target.
The objective is to shoot down the spaceship with the smallest number of shots.
Luckily the spaceship is not moving. At least not in the initial version of the game.

In a less space-oriented description: the computer "thinks" about a whole number between 1-200 and hides it. You have to guess the number.
After every guess the computer tells you if the guess was correct, if it was smaller or larger than the hidden number.
Then you can guess again.

What is the best strategy? Is there a strategy that can always win?

<div class="spoiler" text="Click for Explanation">
<p>
The naive way to find the other space-ship is to shoot one-by-one from 1 to 200. In worst case, if the computer thought 200,
it will require 200 shots.  If you play a lot, on average you'll hit the target in 100 shots.
</p>

<p>
There is a much better strategy though.
You can shoot in the middle of the range. If the shot was short we know that the spaceship in the second half of the space. If
the shot was too long, we know the spaceship is in the first half of the space. In either case, in one shot we halved the space we need
to check. We can then repeat this on the half where the spaceship can be found until the (search-)space is reduced to only one spot and
then we hit the space-ship. In worst case, if we don't get lucky in one of our shots, we can reduce the space to 1 place in just 8 steps:
The size of the space after each shot: 200 -> 100 -> 50 -> 25 -> 12 -> 6 -> 3 -> 1 
</p>
<p>
This strategy is called <b>binary-search</b> and it can be very important in computer programming, but outside of it as well.
For example, if you need to shoot down space-ships.
</p>
</div>


## Outline

I don't have the full outline of the series. I'll make it up as we go.
But I know some of the steps:

<ol>
  <li>[Basics of HTML to show a page](/html-basics)</li>
  <li>Basics of JavaScript to play the game</li>
  <li>HTML5/CSS3 to make the game more persistent</li>
  <li>Some backend-language to store the data on a server</li>
</ol>


