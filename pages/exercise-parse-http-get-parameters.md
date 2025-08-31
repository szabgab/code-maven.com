---
title: "Exercise: Parse HTTP GET parameters"
timestamp: 2015-11-03T21:00:01
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


When you visit a web-site, fill in a form and submit it, in some cases you will see the URL containing a question mark `?`
followed by a long list of key-value pairs. These are the HTTP parameters of this GET request.

Every programming language has plenty of libraries handling these values properly, but we can also use them as an exercise.



So given a string like this:  `fname=Foo&lname=Bar&email=foo@bar.com`
or a string like this `ip=127.0.0.1&machine=foobar` create a hash/dictionary/associative array that will hold the key-value
pairs found in the string.

Given `fname=Foo&lname=Bar&email=foo@bar.com` the data structure should look like this:

```
{
  'fname' : 'Foo',
  'lname' : 'Bar',
  'email' : 'foo@bar.com'
}
```

Given this string `ip=127.0.0.1&machine=foobar` the data structure should look like this:

```
{
  'ip'      : '127.0.0.1',
  'machine' : 'foobar'
}
```


For extra bonus try to handle this case as well:

Given `fname=Foo&lname=Bar&email=foo@bar.com&email=here@there.or` the data structure should look like this:

```
{
  'fname' : 'Foo',
  'lname' : 'Bar',
  'email' : [ 'foo@bar.com', 'here@there.or' ]
}
```

