---
title: "Sites with public API with CORS - Cross-Origin Resource Sharing enabled"
timestamp: 2015-08-18T10:30:01
tags:
  - CORS
  - Access-Control-Allow-Origin
published: true
books:
  - angularjs
  - javascript
author: szabgab
archive: true
---


When learning [AngularJS](/angularjs), or any other [JavaScript](/javascript)
framework for building Single Page Web Applications you can go only so far without a back-end to
access.

There are tons of web sites with public API that we could access, but most of them use the default
CORS security setting (by not setting <b>Access-Control-Allow-Origin</b>) which means we can only
access their API from the command line or from the server and not from the browser.

On this page you'll find a collection of web sites that provide public APIs with Access-Control-Allow-Origin
enabled. You can access them to fetch data via Ajax requests.


<script src="/javascripts/angular.min.js"></script>

<script>
angular.module('CORSApp', [])
    .controller('CORSController', function($scope, $http) {
        //var url = '';
        // XMLHttpRequest cannot load http://www.imdb.com/xml/find?json=1&nr=1&nm=on&q=jeniffer+garner.
        // No 'Access-Control-Allow-Origin' header is present on the requested resource.
        //var url = 'https://en.wikipedia.org/w/api.php?action=query&titles=Main%20Page&prop=revisions&rvprop=content&format=json';
        //var url = 'https://api.smartsheet.com/2.0/sheets';
        //var url = 'http://public-api.wordpress.com/rest/v1/sites';
        $scope.clear = function() {
            console.log('clear');
            $scope.data = '';
            $scope.error = 0;
        }
        $scope.try = function() {
            $http.get($scope.url).then(
                function(response) {
                    console.log(response);
                    $scope.data = response.data;
                },
                function(response) {
                    console.log("error");
                    console.log(response);
                    $scope.error = 1;
                }
            );
        }
    });
</script>

<div ng-app="CORSApp" ng-controller="CORSController">
    <select ng-model="url" ng-change="clear()">
        <option value="http://www.imdb.com/xml/find?json=1&nr=1&nm=on&q=jeniffer+garner">IMDB (does not work)</option>
        <option value="https://api.github.com">GitHub</option>
        <option value="http://api.metacpan.org/v0/release/_search?size=10">MetaCPAN</option>
        <option value="http://api.openweathermap.org/data/2.5/weather?q=Budapest">OpenWeatherMap</option>
        <option value="https://api.flickr.com/services/rest/?&method=flickr.people.getPublicPhotos&format=json&api_key=6f93d9bd5fef5831ec592f0b527fdeff&user_id=9395899@N08">Flickr</option>
    <select>
    <button ng-click="try()">Try</button>
    URL: {{url}}
    <hr>
    Result: {{ data }}
    <div ng-show="error" id="error">Failed</div>
</div>

The Flickr an example is
https://api.flickr.com/services/rest/?&method=flickr.people.getPublicPhotos&format=json&api_key=API_KEY&user_id=USER_ID
You can get an API Key from the [App Garden](https://www.flickr.com/services/), and you can find the user_id
based on a username via the [Flickr username finder](https://www.flickr.com/services/api/explore/flickr.people.findByUsername).

There lots of [stes with public APIs](http://www.programmableweb.com/apis/directory), but many of those will refuse to work
if we try to access them from the browser. (The don't set Access-Control-Allow-Origin)
