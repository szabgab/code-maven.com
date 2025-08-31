---
title: "TODO list"
timestamp: 2016-09-10T17:00:01
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


Creating a TODO list is a fairly standard exercise soon after one have created a [web based Hello World](/exercise-web-hello-world)
and an [web based echo](/exercise-web-echo). Let's describe the task here and see how what interesting features we might include.

See other [projects and exercises](/exercises).


## Simple TODO

Probably the simplest version of the TODO list has a single string which is the descripton of the task.
In this version we can add a task, remove a task and list all the tasks. We can even add a feature to search among the tasks
to display only the onese that match a certain substring.

We can assume that each task is a single line of text (without newlines in it). This way we can save the tasks in a simple text file
where each row is a task. There is no need for a database.

The problem might arise if we type in the exact same task twice. We might want to make sure this does not happen.

## Use and ID, make the title changeable

A slight improvement is to use a unique number as the ID of each task. This usually can be a counter starting from 1.
The advantage is that it is easr to refer to a task by ID which will be fixed during the life of the task while we might
change the title of the task. Having and ID and a title can still easily be stored in a single [CSV file](/csv).
Each row will have two fields, the first one is the id, the second one is the title.

The problem which might, or might not bother you is that we need a way to know what is the next id to allocate.

We could just take the biggest ID available and add one, but if we delete the task that had the highest number and then
we add another task then we'll be using the same id we already used. For some cases this might not be a problem, but
if we have URLs build using the ID, or otherwise there is some place where those ids are remembered, then someone could
try to access an already deleted item. In such case it would probably make more sense to give a "not found" error, than to return
an unrelated task that happened to receive the same id.

So we either need to make the CSV file irregular and reuse one of the rows to store the "largest id ever used", or
we need to have some other file to store that number.

This already starts to make the "database" a bit too complex.

For such case I'd probably either use some other file format (e.g. [JSON](/json)
or [YAML](/yaml)), or a real database, such as [SQLite](https://www.sqlite.org/).

For SQLite case here is a sample code for creating the table:

```
CREATE TABLE tasks (
    id      INTEGER  PRIMARY KEY,
    title   VARCHAR(255)
);
```

Using SQLite, the id will be automaticlly incremented every time we add a new entry and we can use the id
to identify the task that need to be updated when editing the title.

## Details, date, and status

If we would like to improve the application evan further we might want to add a few more fields.

`details` could be an extensive description of the task.

`created` could hold the date when the task was created. If we use the auto-incrementing id
then we could alread use that to sort the items by creationg time, but we can't tell if an item
is 1 day or 1 year old. So having a creation date can be useful.

`done` Instead of deleting tasks that were finished, you might want to mark
them as "done". For this we could use a `BOOLEAN` type (even though types don't really exist in SQLite).

`status` A probably even better solution might be to have a column called `status` that can have different
value such as "waiting", "on hold", "in progress", or "done" to further fine-tune the status of the tasks.

`due` Even more imprtant than the start date you might want to have a dead-line, or a due-date.

`priority` When deciding which tasks to do you will need to take in account the due date, but even then you might have
a few competing tasks. Setting a prioroty level will make it easier to decide.


```
CREATE TABLE tasks (
    id       INTEGER  PRIMARY KEY,
    title    VARCHAR(255),
    details  BLOB,
    created  DATE     default date('now'),
    due      DATE,
    status   BOOLEAN  default 'waiting',
    priority INTEGER
);
```


## Remember the Milk

If you need more ideas what to include in your TODO list, you can always check out 
[Remember the Milk](https://www.rememberthemilk.com/) which is one of the best TODO applications.


