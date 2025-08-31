---
title: "Filters in AngularJS"
timestamp: 2017-01-27T12:30:01
tags:
  - $filter
  - ng-repeat
  - filter
published: true
books:
  - angularjs
author: szabgab
archive: true
---


Filters in AngularJS have two major uses.

Some filters work as the `map` function in Perl, Python, Ruby, JavaScript and in many other languages.
They allow us to apply some transformation to one or more values at once.
Among many other things this can be used to change how a single value is displayed.

Other filters are similar to the `grep` function in Perl, which is called `select` in Ruby,
and `filter` in Python and JavaScript.
These filters usually apply to a list of values and return a subset of the original values.
They filter out certain values using some condition.


## Filter as a transformer

Filters in AngularJS can be used either in the HTML code or in the JavaScript code. Let's start with an example in the HTML code
where we apply a filter by using a single pipe `|` inside the double-curly braces:

```javascript
{{ some_attribute | some_filter }}
```

## Changing the format of a value in the HTML

One example would be changing the display format of a value.
For example the [number](https://docs.angularjs.org/api/ng/filter/number) filter will put commas after ever 3 digits
from the right to left as you would do if you wanted to make a large number more readable.

```javascript
{{ some_attribute | number }}
```

So if some_attribute contains `1234.56` , the above expression will display `1,234.56`

On the other hand, if the number has less than 4 digits on the left hand side of the decimal point (if there is one),
then it won't add any commas. `12` will stay `12`.

In addition to the commas, the `number` filter also rounds the number. By default it will round to 3 digits
after the decimal point, but you can add a parameter that sets the number of digits for rounding. Interestingly you
can even set this to a negative number which means round to that many digits to the left of the decimal point.

0-4 will be rounded down, 5-9 will be rounded up.

So given `price = 1234.56789` this will be the output:

<table>
<tr><td>price             </td><td>1234.56789</td></tr>
<tr><td>price | number    </td><td>1,234.568</td></tr>
<tr><td>price | number:0  </td><td>1,235</td></tr>
<tr><td>price | number:4  </td><td>1,234.5679</td></tr>
<tr><td>price | number:-1 </td><td>1,230</td></tr>
<tr><td>price | number:-2 </td><td>1,200</td></tr>
</table>

Let's see a full example that you can also try.

{% include file="examples/angular/filters/change_number_in_html.html" %}

[view](examples/angular/filters/change_number_in_html.html)

## Changing the format of a value in the JavaScript code

While I think this is less interesting, the filters can be also used in the JavaScript code.
For this to work we need to [inject](http://code-maven.com/dependency-injection-in-angularjs) the [$filter](https://docs.angularjs.org/api/ng/service/$filter)
service in the controller:

```javascript
.controller('DemoController', ['$scope', '$filter', function($scope, $filter) {
```

Then we can use the `$filter` object as a function, passing the name of the filter to it,
which itself returns the conversion function. We can pass the raw value to it:


```javascript
$scope.price_number = $filter('number')($scope.price);
```

We can also pass a second parameter to it which, in the case of the `number` filter,
indicates the number of digits for rounding.

```javascript
$scope.price_number4 = $filter('number')($scope.price, 4);
```

The results are the same as in the HTML code, but you can try that here too with the
big difference that the code converting the raw number to formatted numbers will only run
once when we load the page and thus the input box in this example is rather pointless.

{% include file="examples/angular/filters/change_number_in_js.html" %}

[view](examples/angular/filters/change_number_in_js.html)


## Filter as a, well, filter

In the second set of examples we'll see how to us the AngularJS `filter` to
filter out some of the elements from a list. This too can be used either in the
HTML code or in the JavaScript code. We'll start with the HTML code.

## Filter out some of the values in HTML

For this example we need 3 things:

First we need to have an attribute with a list of values. For example a list of numbers.

```javascript
$scope.numbers = [1, 2, 3, 4, 5, 6, 7, 8];
```

Then we need a function, that will accept a single value and return `true` if
we would like to keep that value and `false` if we would like to throw it away.
We need to assign this function to an attribute of the `$scope` to make
it available inside the HTML code.

For our example we will create a function called `odd` that will return `true`
if the `input` was an odd number. That is if dividing it by 2 will have 1 remaining,
or in other words if [modulo](https://en.wikipedia.org/wiki/Modulo_operation) 2 we get 1.

```javascript
$scope.odd = function(input) { return input % 2 === 1 };
```

(Actually we don't even need the `=== 1` part in this code, but for extra clarity I added it.)

Then comes the interesting part.

Normally if we would like to display the content of an array we use the `ng-repeat` directive to
iterate over it. So thats what we would do with the `numbers` array as well:


```html
<li ng-repeat="n in numbers">{{n}}</li>
```


We can apply the `odd filter` using the pipe `|` followed by the word `filter` followed
by `odd`, the name of our function:


```javascript
<li ng-repeat="n in numbers | filter:odd">{{n}}</li> 
```

Looking back to the previous example you might notice that actually in our case the filter was called `filter`
and `odd` was its parameter.

In the [documentation of $filter](https://docs.angularjs.org/api/ng/filter/filter) this parameter is called the
`expression`.

The full example for you to see and try can be found here:

{% include file="examples/angular/filters/filter_odd_values_in_html.html" %}

[view](examples/angular/filters/filter_odd_values_in_html.html)


## Filter out some of the values in JavaScript

The same filter can also be used in the JavaScript code. For this,
just as in the previous JavaScript example, we need to [inject](http://code-maven.com/dependency-injection-in-angularjs)
the `$filter` service:

```javascript
.controller('DemoController', ['$scope', '$filter', function($scope, $filter) {
```

Naturally we need the data to work on. Just as previously.

```javascript
$scope.numbers = [1, 2, 3, 4, 5, 6, 7, 8];
```


We need the `odd` function, but this time it does not need to be part of the `$scope`
as it is only used within our JavaScript code.

```javascript
var odd = function(input) { return input % 2 === 1 };
```

Then we can use `$filter` as a function passing the name of the filter
to it, which is, `filter`. (I know, you might already have filter-overdose.)
This will return a function that accepts the data as the first parameter
which is `$scope.numbers` in our case,
and the name of the `expression`
to be used for the filtering which is the name `odd` in our case.

```javascript
$scope.odd_numbers_angular = $filter('filter')($scope.numbers, odd);
```


Actually, I am not sure at all if this form is useful at all. After all, we can
use the `filter` method which is available on every JavaScript Array
and for that we don't need any help from AngularJS. We don't even need the
`$filter` to be injected in our controller:

```javascript
$scope.odd_numbers_plain = $scope.numbers.filter(odd);
```

The full example with both solution inside the JavaScript code can be found here:

{% include file="examples/angular/filters/filter_odd_values_in_js.html" %}

[view](examples/angular/filters/filter_odd_values_in_js.html)

## Conclusion

There is a lot more to experiment with filters, but this might give you the fist
step in understanding and using them. This might have clarified a bit the odd
(again this word?) overloading of the word `filter`.


