---
title: "Automatic counter using AngularJS"
timestamp: 2015-08-06T21:00:01
tags:
  - $timeout
  - ng-click
published: true
books:
  - angularjs
  - javascript
author: szabgab
archive: true
---


We have seen [how to create a counter in AngularJS](/simple-in-memory-counter-with-angularjs) in which we incremented (or deceremented) the counter by clicking
on a button. In this example we'll automatically increased the counter as time passes.

Don't forget to check out the other [counter examples](/counter)!


## Schedule future execution using $timeout

{% include file="examples/angular/automatic_counter.html" %}

[view](examples/angular/automatic_counter.html)

In this example the controller function expects two parameters, the `$scope`
that contains the attributes we interact with in our HTML page and`$timeout`
which is a function similar to the plain JavaScript `setTimeout` function.
(Atually this is called <b>dependency injection</b> and not parameters, but let's not worry about that now.
Especially as I don't understand it yet.)

`$timeout` is a function that receives two parameters: a callback function object and a time expressed in millisecond.
It schedules the execution of the function object delayed by the time given. Passing 1000 as the second parameter
means we want the callback function to run 1 second after this call was made.

Inside the controller function the first thing is that we create an attribute called `counter` and
set the default value of it to 0. We want to start counting from 0.

Then we create a function called `updateCounter` that, when called, will increment the `counter` and use `$timeout`
to schedule itself 1 second later as well. Effectively this means that every time `updateCounter` runs,
it increments the counter and asks the system to run it again 1 second later. This means the function will run every 1 second.

Then the last step is to call `updateCounter` for the first time to initiate the endless loop.

## Counter with stop button

this timer will be executed every second, but if we would like to stop it?
We'll see an example with an additional button, that will stop the counter.

`$timeout` returns a `promise` object we can later use to cancel the timer.
In order to have that `promise` available to us when needed, I've created a variable
called `timer` and assigned the return value of `$timeout` to it.
(Of course I could have used any name here.)

Then I've added a button to the HTML and using `ng-click` configured it to run then
`stopCounter` method when clicked.

The only thing left was to create the `stopCounter` method.

At first I created it using `var stopCounter = function() { ... }`
just as the `updateCounter`, but that did not work. Because we want to
call it from the HTML, we need to add this method to the `$scope`. Hence
I had to change the definition to be:
`$scope.stopCounter = function() { ... }`.

Inside we have the statement `$timeout.cancel(timer);` that will cancel the
timer. Go ahead. Try it!

{% include file="examples/angular/automatic_counter_with_stop.html" %}

[view](examples/angular/automatic_counter_with_stop.html)


## Counter with stop and start buttons

As an extra feature I wanted to see how can I add another button, to start the counter again.

The first version was simple. I just added a button and a new function:

```javascript
$scope.startCounter = function() {
    updateCounter();
};
```

and the corresponding HTML button to call it.

The problem with this solution was that it allowed me to click the start button
several times in a row and the counter started to go much faster and sometimes jumped by 2 or by 3.
What actually happened that every time I clicked on the `start` button, a new timer
was created and I had several timers waiting in parallel.

I had to somehow make sure that only one timer exists at any given time. Either by disabling
the `start` button after it was clicked or by checking if there is already a live
timer and launching a new one only if there was no live counter.

I picked this solution as I was more interested in the JavaScript/AngularJS solution.
I had to make two changes. One in the `stopCounter` function. I've added

```javascript
timer = null;
```

After all once we have cancelled the timer, there is no point in having an unusable
object around.

Then in the `startCounter` I could check if `timer` is not `null`
and create the new $timeout object only if the timer was `null`.


{% include file="examples/angular/automatic_counter_with_stop_start.html" %}

[view](examples/angular/automatic_counter_with_stop_start.html)

## Comments

Is it possible to add a save button and save the elapsed (time) count in the above script? Maybe make the elapsed time counter value a variable in an ionic application?

