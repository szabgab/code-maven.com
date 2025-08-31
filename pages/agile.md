---
title: "Agile practices"
timestamp: 2017-01-01T07:30:02
tags:
  - Agile
published: false
author: szabgab
archive: true
---


What we get is shorter development time, better accuracy in estimations, less bugs.
Peace of mind for both developers and managers.


* unit testing
* continuous integration
* coding standards  (including the use of linter)
* refactoring
* Test-Driven development
* Automated Acceptance testing
* Automation (usually means CI or something similar)
* Continuous Deployment
* [Pair programming](/pair-programming)
* Frequent commits
* Frequent code-review
* collective code ownership
* Behavior-driven development
* Sustainable pace

## Books
* [Refactoring](https://martinfowler.com/books/refactoring.html) by Martin Fowler
* [Working Effectively with Legacy Code](https://www.amazon.com/dp/0131177052/) by  Michael Feathers
* [Rapid Development: Taming Wild Software Schedules](https://www.amazon.com/Rapid-Development-Taming-Software-Schedules/dp/1556159005) by [Steve McConnell](http://stevemcconnell.com/books/)

## Articles

* [Working Effectively with Legacy Code](http://www.netobjectives.com/system/files/WorkingEffectivelyWithLegacyCode.pdf) (short pdf)
* [Introducing An Agile Process to an Organization](https://www.mountaingoatsoftware.com/articles/introducing-an-agile-process-to-an-organization)
* [State of Agile](http://stateofagile.versionone.com/)
* [State of Agile 2017](https://explore.versionone.com/state-of-agile/versionone-11th-annual-state-of-agile-report-2)
* [What's the Value of CI/CD?](https://builttoadapt.io/whats-the-value-of-ci-cd-c2e6c39450bd)

## Counter points

* Clean-up is invisible to users, we need to add new features.
        <ul>
* Bugs are visible. Especially bugs that return.
* Security issue are even worse.
* Clean-up will help us go faster.
        </ul>
    
* We don't have time for clean-up.
        <ul>
* Prevention a lot cheaper than cure. Both in terms of money, time, and bugs.
        </ul>
    

## Steps

* Introduce (unit)testing.
        <ul>
            <li>Introduce the practice with low-hanging fruits even if they don't provide a lot of value. Get the CI going!
            <li>Increase the modularity of the code.
            <li>Increase the testability of the code.
            <li>Use mocking in the meantime.
        </ul>
    

## Tools

* [Mikogo](https://www.mikogo.com/) for remote screen sharing

