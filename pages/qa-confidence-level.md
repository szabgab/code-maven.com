---
title: "Measuring confidence level in your application - Quality Assurance?"
timestamp: 2020-09-30T07:30:01
tags:
  - QA
  - testing
  - quality
description: "How can you measure the confidence level in your application?"
published: true
author: szabgab
archive: true
show_related: true
---


One of my clients that is moving their services from an on-premise installation to the cloud, started to talk about the level of confidence in their code.

I am wondering why it came up now? What is different from the previous 20+ years when they released software? And how can we really measure confidence?


I think the big difference is that earlier they relied on a <b>QA department</b> that was checking their application after the main part of the development
was done. This took months of back-and-forth bug reporting, fixing and re-testing. We all know and hate this model.

This system was not good back then, but it is impossible now when moving to the cloud.

In this new cloud-based environment the expectation is that we will be able to release and deploy code within hours of it being "finished" by the developers.
I think they still have not fully accepted that the word "finished" or "done" has a totally different meaning than what they used to have.

In any case I was trying to come up with a few ways we can measure this level of confidence. These might help your organization as well?

## Business level measurement

These could be things like
* How much money do we make?
* How many visitors convert to users?
* etc.

but at least in our business the sales are done by sales people, so our measurements need to focus on how well we serve existing clients.

## Business level serving existing clients

The primary measurement should be <b>goals set by the business</b>: The number, severity, and length of production failures. Who measures it and how?
In general the lower the numbers the better. One needs to measure these and make sure they keep going down with time. Once thing that is really difficult
here is to measure the "severity".

A similar measurement could be something like the following:

* Number of open issues/tickets (weighted based on severity)?
* How long are the issues open?
* How soon are they found after they got added to the code?
* How soon are they fixed in the code?
* How soon do they reach production?


## Code level


* Unit test
* Test coverage
* Data coverage.
* Load and Performance test thresholds met
* Code standardization measurements. Static Code Analyzers  (linter, tidy etc.)
* Cyclomatic code complexity measurement.


## Other

A few other resources I looked at:

[Test coverage metrics](https://reqtest.com/testing-blog/test-coverage-metrics/)

[Traceability matrix](https://reqtest.com/testing-blog/5-key-benefits-of-using-a-traceability-matrix-to-stay-on-top-and-in-control-of-your-project/)

