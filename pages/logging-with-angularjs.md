---
title: "Logging in AngularJS applications"
timestamp: 2016-10-30T07:30:01
tags:
  - $log
  - console.log
  - $logProvider
published: true
books:
  - angularjs
author: szabgab
archive: true
---


We have already seen [how to log in plain JavaScript](/logging-in-javascript),
and even dealt with <a href=/logging-javascript-objects">logging JavaScript objects</a>,
but what if we are using [AngularJS](/angularjs)?


## $log in AngularJS

AngularJS comes with a service called [$log](https://docs.angularjs.org/api/ng/service/$log) that
is a simple wrapper around the `console.log` facilities.

In this example we can see that in order to use the `$log` service we need to use the
`dependency injection` of AngularJS `['$log', function($log)` passing the `$log`
object to the function implementing the controller where we would like to use it.

We see both calls to 5 `$log.*` methods and to the corresponding `console.*` methods.

{% include file="examples/angular/logging.js" %}

The results looks like this in Chrome:

<img src="/img/angular_logging_chrome.png" alt="Logging in AngularJS" />

As you can see the results of the corresponding logging functions look the same in AngularJS and pure JavaScript, except that the
calls to the `$log.*` methods don't show accurate line numbers.

That's clearly a drawback and we are going to try to fix this soon, but before that we are going to
look at the advantage of the `$log` facilities over the corresponding `console.*` functions.

In any case if you'd like to try it yourself, here is the HTML file that will load the above JavaScript file:

{% include file="examples/angular/logging.html" %}

[view](examples/angular/logging.html)


## Turn off logging in AngularJS

The only advantage of `$log.debug` over `console.debug` I could find is
the ability to turn off the debugging printouts.

We can do that through the
[$logProvider](https://docs.angularjs.org/api/ng/provider/$logProvider) provider
in the `config` directive of AngularJS by adding the following:

```javascript
.config(['$logProvider', function($logProvider) {
    $logProvider.debugEnabled(false); // turns off the calls to $log.debug, but not the others
}])
```

This turns off the `$log.debug` calls, but as you can see in the comment, it
does not turn off the other 4 calls of `$log`. Our code will still print out
any of the `info`, `log`, `warn`, and `error` messages.

See the results:

<img src="/img/angular_logging_off_chrome.png" alt="Logging in AngularJS" />

As far as I know, Angular does not provide a way to turn those off.

The full JavaScript is here:

{% include file="examples/angular/logging_off.js" %}

The corresponding HTML file is here:

{% include file="examples/angular/logging_off.html" %}

[view](examples/angular/logging_off.html)

## Showing the correct line numbers

There is a way to tell AngularJS to show the correct line numbers. You just need to bind the `$log.*`
functions to the `console.*` functions. Like this:

```javascript
    $log.debug = console.debug.bind(console);
```

You will have to do that for each one of the 5 methods separately. In our example we have done it for 2:

<img src="/img/angular_logging_lines_chrome.png" alt="Logging in AngularJS" />

{% include file="examples/angular/logging_lines.js" %}

The next HTML file can help you try this in your browser.

{% include file="examples/angular/logging_lines.html" %}

[view](examples/angular/logging_lines.html)


## Other Solution

While searching for solutions I've bumped into the 
[Blackbox JavaScript Source Files](https://developer.chrome.com/devtools/docs/blackboxing), that can be used to fix
the incorrect reporting of line numbers. Unfortunately that's Chrome only.

## Conclusion

As it stands I don't see any real advantage for using the logging mechanism provided by AngularJS.
I'll stick with calls to `console.*`.


