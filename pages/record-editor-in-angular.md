---
title: "Record editor using Angular JS"
timestamp: 2015-12-17T20:30:01
tags:
  - $index
published: true
books:
  - angularjs
author: szabgab
archive: true
---


I am working on several web application where we have lists of data records and we would like to give our users
some capability to edit those records. In this article I'll look at one of the solutions I've tried.


In this simplified application each record has a single text field that can be edited.

Each record looks like this:

```
  {
     'name' : 'Foo'
  }
```

The whole HTML page is a single Angular Module with a single Angular Controller.
There are two "pages" similar to what we were doing in the
[simple pages and tabs with Angular JS](/simple-pages-or-tabs-with-angularjs)
example.

The first page is the listing of the records. Nothing fancy. Next to each value there is a button that will call
the `edit` function with the current record when clicked.

The second page is the editor. It has an `input` box for the only value we have in each record.
This input box is bound to the `editor.name` attribute.

There are also two buttons. One to save the changes and one to cancel the editing. Each one has a function
call.

{% include file="examples/angular/editor1/edit_record.html" %}

[view](examples/angular/editor1/edit_record.html)

Now let's see the JavaScript file.

In the real application we get the records via an Ajax call, but in this example I just have
a function called `get_data` that returns the records. I put it outside of the Angular module
in order to emphasize that the data comes from outside of our application.

Inside the controller we set the default page and fill the records from that external data source.

The `edit` function receives the current record as a parameter and assigns to a separate attribute
that represents the editor and then switches to that page.

Clicking on either the `cancel` or the `save` buttons will switch back to the list-view,
but in the save function we also need to implement the actual saving of the data. Before doing that
please try the code.

{% include file="examples/angular/editor1/edit_record.js" %}

You will notice that if you make changes in the editor they are automatically reflected in the list
whenever you click on the `save` button. Unfortunately the same will happen when you click on
the cancel button. By assigning the current record as a whole to the `$scope.editor` attribute
we connected that listing of that selected record (on the list page) to the editor through an attribute
on the `$scope`. Two-way bindings are one of the "selling features" of AngularJS,
but we created two pairs of two-way bindings that currently bites us.

We either need to implement something that will put back the old value when the user clicked on the "cancel" button,
or we need to totally separate the two bindings and copy the content of the record when we open the editor
and copy the data back when we click on save.

When clicking on "edit" copy the current record to the editor attribute. Have separate bindings. Copy the data from the editor to the list if the user clicks on "save".

When clicking on "edit" copy the current record to a backup variable, bind the list entry to the editor. Copy the data back if the user clicks on "cancel".

## Separate Editor

I have a feeling that separating the editor is the cleaner solution conceptually. So let's start with that.

If we are going to separate the current item of the list and the editor, then somehow we have to remember
which item were we editing. Probably the best way is to remember the order number of the record in the whole
list of records.  In order to facilitate this we will pass the `$index` attribute supplied by the
`ng-repeat` instead of the actual record.

So the HTML changed a bit and we are now calling `edit($index)`.

{% include file="examples/angular/editor2/edit_record.html" %}

[view](examples/angular/editor2/edit_record.html)

The JavaScript code went through a much bigger change. We accept the index in the "idx" variable and
then we copy the value of the "name" attribute of the current record to the editor.
We also save the index in an attribute on the `$scope`. 

The `cancel()` does not have to do anything just switching back to the "list" page.

The `save()` function copies the new value from the editor to the appropriate record using
the saved index.
It should also call some Ajax function to send the new data to the back-end, but in this example
we don't want to deal with that.

{% include file="examples/angular/editor2/edit_record.js" %}

Try this solution. It works.

## Separate Stash

For the 3rd example we did not have to make any changes to the HTML page, only to the
JavaScript. Here, instead of copying the content of the record to the editor we copy it
to some other attribute we called "stash". We store the index as previously and then we
connect the editor to the current record.

This time we don't have to do anything if the user clicks on the 'save' button as the
editor was connected to the current record. We only need to have the Ajax call.

Instead of that we now need to copy the old data back from the stash to the current record
if the user clicked on "cancel".

{% include file="examples/angular/editor3/edit_record.js" %}

{% include file="examples/angular/editor3/edit_record.html" %}

[view](examples/angular/editor3/edit_record.html)

## Caveat

In all these cases we manually copied the single attribute the record has. If we have larger and more complex records
we'll better use the `angular.copy` method to do a full deep-copy of the record.

We could also stash away the whole "records" array and copy it back if the user clicks on "cancel", but if this feels
like a waste of memory.


