---
title: "JSON"
timestamp: 2015-11-20T12:30:01
tags:
  - JSON
published: true
author: szabgab
archive: true
---


[JSON (JavaScript Object Notation)](http://json.org/) is a lightweight data interchange (serialization) format inspired by JavaScript object literal syntax.
The power of JSON comes from the fact that it maps rather well to the complex data structures of many programming languages and that there are converters
between JSON and the data structures of over 60 programming languages. See the [JSON site](http://json.org/) for specification and for the list of implementations.


For our purposes JSON is a string that can be easily stored in a file, or can be easily transmitted over some networking protocol.
This makes it an extremely useful format for data exchange between processes even if the process are running on different machine, at different times,
and are written in different languages. It can be also used as a format for configuration files as it is rather readable and writable to humans as well.

## Use cases of JSON

Ajax, that stands for <b>"asynchronous JavaScript and XML"</b>, describes how an application written in JavaScript running in a browser can communicate
with the application running on the server that is most likely written in some other language, for example in [Perl](https://perlmaven.com/),
[Python](/python), [Ruby](/ruby), or PHP.
Originally, as the name indicates, the data sent back-and-forth between the two applications was supposed to be in XML, but today, a large chunk of those applications communicate
using JSON format. It is more light-weight than XML and fits the purpose much better.

Using it as a human edited configuration file is another use case. The fact that it allows the creation of deep hierarchies makes it much more useful that
the INI-file format which was used extensively especially in Microsoft Windows.

JSON can be used as a Data Serialization method for caching.

A step-child of it, called [BSON (Binary JSON)](http://en.wikipedia.org/wiki/BSON),
is being used as the data format in [MongoDB](https://www.mongodb.org/).

## Implementations and articles

* [JSON in Perl](https://perlmaven.com/json)
* [Ajax request for JSON data](/ajax-request-for-json-data)
* [JSON module in Ruby](http://ruby-doc.org/stdlib-2.0.0/libdoc/json/rdoc/JSON.html)
* [json in Python 2](https://docs.python.org/2/library/json.html)
* [JSON in PHP](http://php.net/manual/en/book.json.php)


