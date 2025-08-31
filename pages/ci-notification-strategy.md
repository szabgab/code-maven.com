---
title: "CI notification strategy"
timestamp: 2019-11-28T21:30:01
tags:
  - CI
published: true
author: szabgab
archive: true
---


A recommended notification strategy for CI systems


## Email notification:

* On failure send message TO the most recent comitter and CC the team.
* On the first success after a failure send message TO the most recent comitter and CC the team.
* On regular success send message TO the most recent comitter (and not to the team).

In every case the subject should start with the same text, eg. [TEAM-NAME CI] to make it easy to filter, followed by the status: FAILURE, FIXED, SUCCESS respectively.

Normally failure in the CI system should be a rare event, but when it happens we want everyone to know about it and we want everyone to look at the problem. Both in order to be able to help fixing it and to
learn from the mistakes. Even if they were made by some other people.

We would want to send notification on the first success after failure to everyone so if they were looking at the problem they know they can now relax. Also if someone looks at their e-mail later, we would
like them to be able to easily see that the problem was already fixed. Besides, if the failure event is rare then this is also rare.


Finally we would want to send a notification to the most recent comitter on the plain success of the CI system so s/he get a nice confirmation that their work was integrated properly.

## Chat system (Slack, IRC, etc.) notifications.

Like in e-mail but TO is replaced by DM (Direct Message) and CC-the team is replaced by a message to the central channel of the team.


