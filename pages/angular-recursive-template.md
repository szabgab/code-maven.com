---
title: "Almost infinite recursive template in AngularJS for representing tree structures"
timestamp: 2016-05-18T23:30:01
tags:
  - $rootScopeProvider
  - digestTtl
  - ng-repeat
  - ng-include
  - config
published: true
books:
  - angularjs
author: szabgab
archive: true
---


Representing a tree-like structure can be a tricky thing, but as plenty of other examples
found on the Internet show, people need to do it. Recently I also needed to do that and it
worked quite well till the people who built the data have added another level to the tree.
Then it blew up with a horrible error message. It was so big that the link leading to
the Angular Error report site was also broken.

After some additional research I found the solution. Let's see it.


## Recursive template with static data

First let's see the "standard" solution showing tree stuctures:

Our JavaScript code looks like this:

<include file="examples/angular/recursive_template/recursive.js"

It doesn't have much in it, just the data structure.

The HTML, including the template look like this:

{% include file="examples/angular/recursive_template/recursive.html" %}

[view](examples/angular/recursive_template/recursive.html)

the <b>tree_view</b> is the name of the template and it includes itself.

You can click on the <b>try</b> link to see the result.

## Recursive template with generated data

In order to demonstrate the problem, and to avoid creating a large data structure manually,
I've created another example in which we generate the same tree structure using a
recursive JavaScript function. There are some logging messages included to make
it easier to see what's going on. (Read: I spent quite a few minutes getting the function right
and needed those printouts.)

{% include file="examples/angular/recursive_template/recursive_generated.js" %}

Besides the name of the included JavaScript file, the HTML did not change:

{% include file="examples/angular/recursive_template/recursive_generated.html" %}

[view](examples/angular/recursive_template/recursive_generated.html)

As long as we give a number less than 10 to the function, which means the number of
levels in the tree, everything works find. Once we pass 10 or any larger number we
get a nasty error in [the JavaScript console](/open-javascript-console).
If you are lucky and the data structure isn't
too big, like in this example, the error will include a link that, after further
cleaning leads to <href="https://docs.angularjs.org/error/$rootScope/infdig?p0=10">this error page</a>

It reads:
<pre>
Error: $rootScope:infdig Infinite $digest Loop
10 $digest() iterations reached. Aborting!
</pre>

In a nutshell: we had a recursive call in Angular, (this one we knew, this is what we wanted),
but in order to protect us from infinitely loops AngularJS (as many programming languages too)
imposes an arbitrary limit to the number of recursive calls. In the case of AngularJS this number is 10.
So one we reach this depth, AngularJS stops the recursion and reports the error.

At the end of the page it also suggests that we can adjust the limit through the
[$rootScopeProvider](https://docs.angularjs.org/api/ng/provider/$rootScopeProvider).

## Increase the recursion limit by setting $rootScopeProvider.digestTtl

The solution is then to increase the limit to something that matches our need.
Increasing this number means that in case you get in a unwanted recursive call
Angular will work harder before putting an end to the ordeal which might mean
that the application will be less responsive, so change it with care.

In this example I've increased the value to 14 which will be enough for our example:

```javascript
.config(function($rootScopeProvider){
    $rootScopeProvider.digestTtl(14);
})
```

Here is the full JavaScript code:

{% include file="examples/angular/recursive_template/recursive_generated_fixed.js" %}

Here you can try it:

{% include file="examples/angular/recursive_template/recursive_generated_fixed.html" %}

[view](examples/angular/recursive_template/recursive_generated_fixed.html)


<h3>Screenshots</h3>

![](/img/shots/angular-recursive-template.png)

