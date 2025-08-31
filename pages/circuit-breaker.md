---
title: "Software Circuit Breaker"
timestamp: 2018-07-02T12:30:01
tags:
  - CodeMaven
published: true
author: szabgab
archive: true
---


A circuit breaker in software is proxy-like object that monitors the performance the remote resource.
If the remote resource stops answering or if the response time is beyond some threshold, the circuit breaker
will stop forwarding the request and it will return an error-code or raise an exception itself.

The idea is that it is better to fail fast then to fail slow.

It is also better to avoid further overloading the already overloaded remote system.


In electrical system it is acceptable to expect an external action to reset the circuit breaker.
In software however we might want to allow the circuit breaker to check if the protected resource
is already available and start letting requests through again.

For more details see [circuit breakers](https://martinfowler.com/bliki/CircuitBreaker.html) as described by Martin Fowler
and see the [Circuit breaker design pattern](https://en.wikipedia.org/wiki/Circuit_breaker_design_pattern) on Wikipedia.

