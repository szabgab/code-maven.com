---
title: "TODO in HTML5 and plain JavaScript"
timestamp: 2015-06-04T19:30:01
tags:
  - localStorage
  - getItem
  - setItem
  - getElementById
  - getElementsByClassName
  - JSON.parse
  - JSON.stringify
  - getAttribute
  - Array.splice
published: true
books:
  - javascript
  - cm
author: szabgab
archive: true
---


Creating a TODO list can be considered just a little bit further from "Hello World", the "standard" example people use when
learning a new language. In this example we'll build a very basic TODO application using some HTML5 features and JavaScript.


The very first thing we need is to create an HTML page. We could get by with just the following 3 lines, as those are the important lines,
but I thought adding a few extra lines of HTML would make it more "correct".

The 3 important lines are the following:

```html
<input id="task"><button id="add">Add</button>
<div id="todos"></div>
<script src="todo.js"></script>
```

At first we have an `input` element where we'll be able to enter text and it has a button that we'll be able to click.

In the second row we have an empty `div` element. We are going to display the current list in that element.

Finally we load an external JavaScript file called `todo.js`

The reason we load the JavaScript file at the end is that we wanted to make sure the other elements are already in the browser by
the time the JavaScript file is loaded and by the time it starts to run.

The full version can be seen here, and you can even try it by clicking on the link below.

{% include file="examples/js/todo.html" %}

[view](examples/js/todo.html)

In the JavaScript code we have 4 function, and after the declaration of those 3 function we have the following code:

```javascript
document.getElementById('add').addEventListener('click', add);
show();
```

The first line locates the HTML element that has the id "add" using the [getElementById](/javascript-hello-world-change-the-dom)
method. On the returned object we call the [addEventListener](/handling-events-in-javascript) method and assign the 
`add` function to the `click` event. This code will make sure then whenever the user clicks on the "Add" button, the `add` function
will be called.

Finally we run the `show` function.

The 4 function we have in our code are the following:

`show` will display the current list of TODO items.

`add` will take the text from the `input` box and save it in our "database".

`remove` will remove the selected item from the list of TODO items in our "database".

`get_todos` is the function that will retrieve the list of TODO items from our "database".


## The "database"

I put the word in quotes as it is not really a database in the same way most people consider databases,
but then any place we can persistently store data could be called a "database".

Specifically we are going to use the [localStorage](/on-load-counter-with-javascript-and-local-storage)
facility. It is a key-value pair database in the browser. We can store any string in it and that data will be available to us
when we return to the same page later. We just have to remember, the information stored in `localStorage` is not going to
be sent to the server and it won't be available on the same page if we visit it from another computer, or even from the same computer,
but a different browser.

For our TODO list we are going to use a single key in the `localStorage` and the value will be the stringified version of the list of TODO items we have.


## Fetching from the database: get_todos

As this function used by all the other functions, let's see the `get_todos` function first. It does not get any parameter.
It just fetches the content of the `todo` key of the `localStorage` using the `getItem` method.
If this is the first time ever the function is called, the specific localStorage entry will be empty and the `localStorage.getItem` 
call will return `null`. In that case we return the newly created empty `Array`.

If the returned value is not `null` then it must be the stringified data we stored earlier. We use `JSON.parse` to
convert the JSON string back to JavaScript data and return that.

```javascript
function get_todos() {
    var todos = new Array;
    var todos_str = localStorage.getItem('todo');
    if (todos_str != null) {
        todos = JSON.parse(todos_str); 
    }
    return todos;
}
```

## Adding a new TODO entry

The second function we might want to take a look at is the one called `add` which is called when the user has
clicked on the `All` button. At first, using `getElementById` it locates the HTML element with the id `task` which is the
`input` box and then it retrieves the `value` the user has typed in.

Then, calling `get_todos` we retrieve the already existing list of TODO items from the "database". As explained above,
at the first time this function will return an empty `Array`.

We append the new task to the `Array` using the `push` method and then save the new list of TODO items
in the "database". For this we first stringify the `Array` using the `JSON.stringify` method and then
we store the returned string using the `localStorage.setItem` method.

In the next step we call the `show()` function that will update the list of TODOs displayed on the web page.

Finally we `return false;` to avoid any further actions generated by the 'click' event.

```javascript
function add() {
    var task = document.getElementById('task').value;

    var todos = get_todos();
    todos.push(task);
    localStorage.setItem('todo', JSON.stringify(todos));

    show();

    return false;
}
```

## show the TODO list

The `show` function will display the current TODO list stored in the "database".
First thing it calls `get_todos` to get the (possibly empty) `Array` of
TODO items.

Then we manually create an HTML snippet in the, otherwise arbitrarily named `html` variable. 
This is a `ul` element (and unordered list), with a `li` (list item) for each TODO entry.
In addition to the content of the `todos` array we also add a button to each list item.
Each button belongs to a class called 'remove' and each button has an id containing the index of the
todo item in the list retrieved from the "database". We'll use these buttons to allow the user to remove
an item from the list.

The call `document.getElementById('todos').innerHTML = html;` insert the newly generated HTML
snippet in the original document loaded from the server. It actually replaces the content of the
element with the id "todos". This means in subsequent calls it will just show the new list
regardless of what was there earlier.

In the next 4 lines we use the `getElementsByClassName` method to fetch all the buttons
that are in the 'remove' class. These are the buttons we have just added to each todo item.
To each button we assign a `event listener` that will be called if the user clicks on
either of those buttons. The call to `addEventListener` connects the 'click' event to the
`remove` function.

```javascript
function show() {
    var todos = get_todos();

    var html = '<ul>';
    for(var i=0; i<todos.length; i++) {
        html += '<li>' + todos[i] + '<button class="remove" id="' + i  + '">x</button></li>';
    };
    html += '</ul>';

    document.getElementById('todos').innerHTML = html;

    var buttons = document.getElementsByClassName('remove');
    for (var i=0; i < buttons.length; i++) {
        buttons[i].addEventListener('click', remove);
    };
}
```

## remove a TODO item

Finally we arrive to the `remove` function that will be called when the user clicks on any of
the remove buttons. (The remove buttons have an X on them.)

`this` represents the current DOM-object which is the remove-button the user just clicked.
We retrieve the value of its `id` attribute using the `getAttribute` method. This is
the index of the specific TODO item among the TODO items in the "database".

After retrieving the current list of TODO items, we use the `splice` method to remove
a specific element from the JavaScript array, and then we store the new list back the database.

Then, just as in the `add` function we call the `show` function to update the list in the
browser as well and we `return false;` to stop the propagation of the 'click' event.

```javascript
function remove() {
    var id = this.getAttribute('id');
    var todos = get_todos();
    todos.splice(id, 1);
    localStorage.setItem('todo', JSON.stringify(todos));

    show();

    return false;
}
```

## Full JavaScript code for TODO list

That's it all the code for the JavaScript based TODO list.

{% include file="examples/js/todo.js" %}

## Comments

thanks for sharing its so helpful..

<hr>

It is useful to develop in my project. Thanks..

<hr>

```
<body>
    <div class="container">
        <input id="task"><button class="btn" id="add">Add</button>
        <ul id="todos" class="collection"></ul>
    </div>
    <script type="text/javascript">
        var add = document.getElementById('add');
        add.addEventListener('click',function() {
            var task = document.getElementById('task').value;
            var list = [];
            list.push(task);
            localStorage.setItem('todo', JSON.stringify(list))
            var todo_str = localStorage.getItem('todo');
            var todos = JSON.parse(todo_str);
            var html = '';
            for(var i=0; i<todos.length; i++)="" {="" html="" +="&lt;li class="collection-item"&gt;" +="" todos[i]="" +="" '<="" li="">';
            }
            document.getElementById('todos').innerHTML = html;
        })
    </script>
</body>
```

Why isn't this code storing the values in localStorage?

<hr>

how to store and retrieve tasks as javascript objects?


