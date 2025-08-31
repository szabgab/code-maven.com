---
title: "Create a Personal Microblog"
timestamp: 2020-01-18T17:30:01
tags:
  - Exercises
  - Microblog
published: true
author: szabgab
archive: true
---


This is a project idea included in the list of [exercises](/exercises).


A microblog - at least for us - is a site where you can post short notes. Similar to Twitter, but for now it for one user only. This project has several steps.

1. Create a command line tool that will accept some text and save it in some local database with the current timestamp. After submitting several messages we'll have a list of messages with the appropriate dates in the file. The length
of the messages should be limited to some number. The number should be probably configurable, but you can start with 280 character limite which is what Twitter has now.
1. Create another command line script that creates a JSON file listing all the messages. Actually it should probably accept a parameter of how many messages to show and should default to the 10 most recent messages.
1. Create another command line script that generated a static web site. On the main page (called index.html) it shows the 10 most recent messages. Each message also has its own file. The filename is made out of the milisecond the
message was posted. e.g. 1579360497123.html
1. Create a command line scipt to generate an Atom feed of the messages. Again, have it include the 10 most recent messages. Make the number configurable.
1. Create a simple dynamic web application that can serve the content but in a dynamic way.



