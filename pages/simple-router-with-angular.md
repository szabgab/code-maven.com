---
title: "Angular example: simple router"
timestamp: 2016-03-12T00:30:01
tags:
  - ngRouter
  - $routeProvider
  - ng-view
  - template
  - templateUrl
  - redirectTo
published: true
books:
  - angularjs
author: szabgab
archive: true
---


When creating Single Page Applications with AngularJS it is quite important to handle the back button properly.
The [ngRoute](https://docs.angularjs.org/api/ngRoute) service provides a simple way to handle this.


{% include file="examples/angular/simple_router/simple_router.html" %}

[view](examples/angular/simple_router/simple_router.html)

We need to load both AngularJS and the Angular Route service.

In the HTML page we add an `ng-view` directive:

```html
<div ng-view></div>
```

When we create the Angular Application using the `angular.module` call we need to pass `'ngRoute'` in the
second parameter to indicate which dependencies to use.

The controller itself can be empty. We only used it here to show where does it fit.
We just fill a simple attribute that will be the h1 element in the page.

The interesting part is the `config` call.
The [$routeProvider](https://docs.angularjs.org/api/ngRoute/provider/$routeProvider)
will have a mapping of URL pathes and what to show when each one is hit.

Assuming the page lives at the URL `http://example.com/example.html` all the pages will be seen
as anchors of that page. So for example the '/abc' route will be
`http://example.com/example.html#/abc`

In our example if the user arrives to the `/abc` Angular will take the content of the
`template` and show it in the div-element having the `ng-view` directive.

If the user arrives to `/def`, Angular will fetch the content of the 'def.html' page from the same server
and will display the content of that file in the `ng-view`.


The `otherwise` entry tells the router where to redirect user arriving to any other anchoredurl.
So for example example.html#/xyz  will be automatically redirected to example.html#/ .

## Route page with button

{% include file="examples/angular/simple_router/simple_router_with_button.html" %}

[view](examples/angular/simple_router/simple_router_with_button.html)

In the second example there is an additional element. A button that helps us show how to change
the page from within the  controller. In order for this to work we had to inject the
[$location](https://docs.angularjs.org/api/ng/service/$location) service into the controller.

We can then set the route but calling `$location.path()` and passing the new route to it.
For example '/abc', or '/def' from the previous example. In our demo we have encapsulated this
call in another function which we called 'goto' and which was made available in the HTML code
by adding it to the `$scope`.

In the HTML we have a button that calls this `goto` function that was connected to it
using the `ng-click` directive.

In addition, in this example we have also changed the value of the default page defined
by the `otherwise` call. So any user arriving to a page like "#/xyz" will be redirected
to "#/def"


