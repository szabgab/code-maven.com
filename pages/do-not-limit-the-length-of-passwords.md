---
title: "Do not limit the length of the passwords!"
timestamp: 2024-09-23T11:30:01
tags:
  - password
  - hashing
published: true
author: szabgab
archive: true
show_related: true
---

Every once in a while I encounter a web site where the length of the password is limited. Usually to 8 characters.


This is really scary.


I am trying to figure out why would any developer want to limit the length of the password you use.


I can think of two explanations.


One is that someone thought that "it would be hard for you to remember a longer password so we limit it to 8 characters". Is this patronizing? Where would this come from?


The other, much worse is that they have allocated a given size of space (e.g. 8 characters) in the database where they store the passwords and they want to make sure yours will also fit in. This is really scary as this would indicated that they store the password as you typed in. In clear text. That's a huge security hole as that means anyone who can see the content of the database will have all the passwords. So for example if the admins store a backup of the database on some place that less secure than the original database server then someone might be able to access that.


The correct way to store passwords is to use some kind of a strong hashing algorithm. The nice feature of all the hashing algorithms is that they  take any arbitrary long string and convert it to a fixed length string. For example sha256 will give you a 256 bit (32 bytes) long string. Regardless of the length of the input. So your password can be 10 characters or 20, after the conversion it will be 32 bytes long and that's what the developer needs to store in the database. Maybe with a few extra characters.


So the developers can fix the allocated place in the database and they can be sure that regardless of the length of the real password they will only need to store the expected number of bytes.

