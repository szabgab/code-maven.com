---
title: "Dependency Injection in AngularJS - with and without introspection"
timestamp: 2016-10-05T20:30:01
tags:
  - $scope
  - $log
published: true
books:
  - angularjs
author: szabgab
archive: true
---


[Dependency Injection](https://en.wikipedia.org/wiki/Dependency_injection) has a nice and
complex explanation on Wikipedia and elsewhere. In AngularJS however it is somewhat different and I think
I need a simple explanation.


Normally you define a function that expects certain parameters and the responsibility of the
user of that function to pass in the correct parameters in the correct order.

The user will know what parameters and in what order to pass by reading the documentation of your code,
or if there is not enough documentation by reading the source code.

E.g. if you define a function

```javascript
function store_user (name, password, email) {
}
```

Then the user will have to call the function passing values that will be assigned to the respective
variables:

```javascript
store_user('Foo Bar', 'secret', 'foo@bar.com');
```


## Tell Angular what are your parameters

When you create a `controller`, a `service`, or some other part of the AngularJS
ecosystem, you need to declare an anonymous function that actually implements
that AngularJS element.

You can write something like this:

```javascript
   angular.module('DemoApp', [])
   .controller('DemoController', ['$scope', '$log', function($scope, $log) {
       $scope.message = "Hello World";
       $log.debug('logging hello');
   }]);
```


Here the `controller` method receives two parameters. The first is the name
of the controller ('DemoController'), the second is an array. In the array
the last element is the anonymous function while all the elements before are
the names of the objects Angular needs to pass to the function in the order it
needs to pass them. Inside the function declaration we have the same names in the
same order. Note however that outside the function declaration those are strings
holding the names while inside they are the real variable name.

{% include file="examples/angular/dependency_injection_full.html" %}

[view](examples/angular/dependency_injection_full.html)

[$scope](https://docs.angularjs.org/guide/scope) and
[$log](https://docs.angularjs.org/api/ng/service/$log)
are two objects provided by AngularJS. 

This is called <b>Dependency Injection</b>. That based on the values in the array
Angular will know what object to "inject" into the function.

## Why the duplication?

You might wonder why do we need that duplication of the names. Why do we need
both the string `'$scope'` and then the parameter `$scope`.

Actually we don't need that, but without that our code will break when we minify it.

## Introspection

There are many AngularJS examples where the above code looks like this:

```javascript
   angular.module('DemoApp', [])
   .controller('DemoController', function($scope, $log) {
       $scope.message = "Hello World";
       $log.debug('logging hello');
   });
```

The difference is that in this case the second parameter the `controller` function receives
is the function implementing it. There is no array wrapping it. The function has the parameters
it is expecting, but they are not listed earlier.

So the duplication of names is gone, but you might be wondering how does Angular know which objects
to pass to this function and in which order?

The explanation is in "introspection". While the JavaScript code runs, it can look at its own source code,
inspect it and know what variable names a given function is expecting. Then it can call that function
passing in the correct objects in the expected order.


The problem with this approach is that if we minify our JavaScript code the parameter names of our script
will be also shortened and Angular won't know what objects to pass to the function call. The previous version,
the one with the duplication, solves this problem as the strings in the array declaring the values that
are expected won't change even during minification. That way Angular will know what objects to pass to
the function call.



## Comments

Simple, short, and great explanation. When i saw in tutorials both ways you mention i couldn't understand when to use one or the other, and now i do thanks to you.


