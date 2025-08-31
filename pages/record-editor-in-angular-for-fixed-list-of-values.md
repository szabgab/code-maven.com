---
title: "Record editor in Angular for fixed list of values"
timestamp: 2016-05-08T22:30:01
tags:
  - files
published: true
books:
  - angularjs
author: szabgab
archive: true
---


Earlier we have started to build an editor in Angular to edit a record. In the first article we have prepared
and editor for a simple [input box for free text](/record-editor-in-angular).

This time we'll add an editor for a record where the user must choose from a fixed list of values.


In the HTML we have two pages in two `div` elements. One of them is for the list of records, the
one is the editor. In addition we also have an `h2` element called 'Records' which is always visible.
It shows in a rather readable way the content of the `records` attribute which contains all the records.

You can try the code by clicking on "Try".

{% include file="examples/angular/editor_with_selector/edit_record.html" %}

[view](/examples/angular/editor_with_selector/edit_record.html)


In the JavaScript file we have two function that represent out interaction with the remote servers.
`get_data` sets the current list of records as we have received from the server, `get_values`
returns the list of values available for the `planet` field.

`$scope.page` holds the name of the current page. We start by showing the `list` of the records.

When the user clicks on the `Edit` button the `$scope.edit` is called, passing the `$index`
of the current record in the list of records in `$scope.records`.

We copy the content of the current record to `$scope.editor` and switch to the `editor` view.

We use an `ng-options` directive to show a `select` element and we use
`"v as v.name for v in values track by v.id"` to actually list the potential values.
In this case the use of `track by` is not critical, as the values themselves are unique,
but if there can be duplication of values, then we must explicitly tell AngularJS which field to use
as unique identifier for the record. Without that `ng-options` will break.

If the user clicks `Cancel` we switch back to the list view removing the content of the `$scope.editor` attribute.

If the user clicks `Save` we first copy the content of the `$scope.editor` back to `current_record`
and then clear the content of `$scope.editor`.

{% include file="examples/angular/editor_with_selector/edit_record.js" %}

As you can see there are 4 cases in the original data. 'Foo' does not have any planet in the original data.
In this case the list selector will come up empty, but once we selected a value there is no going back.
(Well, except if we press cancel and don't save the change.)

In the case of 'Bar' the 'planet' attribute holds an object (hash for Ruby and Perl programmers, dictionary for Python programmers) 
with the id of the planet from the `$scope.values` list. When we open the editor it will automatically select and display
the proper value.  Once we click on save (leaving the same value or selecting another planet) the full value record (both name and id)
will be stored in `$scope.records`.

'Qux' has a planet in the original data, but it is represented only by its name. Our solution does not know what to do with it
as the values are identified by their id. So when we try to `Edit` this record we'll have no value selected in the planet selector.

The same goes with 'ET', whose planet is not an object but a simple string.


