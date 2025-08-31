---
title: "Personal Bookmarks"
timestamp: 2015-11-11T22:00:01
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


The objective of this project is to create a web application to store bookmarks.


The owner of the site should be able to store URLs with tags and some comments.
Search the previously stored URL. Edit them and even remove them.

The most basic version can work without any authentication. Assuming it is working on
the desktop computer without external access or assuming it is behind a
"Basic Authentication" system.

An improved version can have an authentication part. It does not need a registration part as
it is a personal system. Only one person, the owner should be able to add/search/edit/delete items.

A 3rd version should allow the owner of the site to add/search/edit/delete items, but it should
also allow anyone to search and view the items.

A 4th level can allow the owner to designate each entry to be "private" or "public".
Non-authenticated users will only be able to see the entries marked as "public".


## Database design


Each entry has a
* URL
* A title that could be fetched from the web site or typed in manually.
* 0 or more tags. Each tag can be a few words long.
* A short description.
* Private note. This is only relevant in the 3rd and 4th level. These comments should be never made public even if the entry is public.
* A flag marking the entry to be private or public. Only relevant in the 4th version.
* Date when the item was added.
* Date when the item was last edited.


The actions the owner or the logged in user should be able to perform:

* Add a new item.
* Search based on any of the fields.
* Edit an exsting item.
* Delete an existing item.

In the 3rd version only the logged in user can search and see items.

In the 4th version then anyone can search, but private entries can be only found by the logged in user.
One must take care that even the autocomplete suggestion system (if there is one) won't suggest words or tags
from private entries as that can reveal information.


