---
title: "JavaScript input with prompt and confirm"
timestamp: 2015-02-10T16:10:01
tags:
  - prompt
  - confirm
published: true
books:
  - javascript
author: szabgab
archive: true
---


Once we know how to [show output from JavaScript](/introduction-to-javascript), let's have a quick look
at two ways to receive input. Probably neither of these is use a lot, but they can be used easily to play
around with the basics.


## prompt

The fist one is called `prompt`.
It will show a pop-up window with the text provided as the first parameter and with a textbox the user can fill in.
When the user presses `OK`, the value in the text box will be returned by the `prompt()` function.
Then, in this example we use the [document.write](/introduction-to-javascript) method to update the html
with the text.

{% include file="examples/js/prompt.html" %}

[view](examples/js/prompt.html)

The textbox will be pre-filled with the content of the second parameter. This can be very useful if we would like to
ask the user to edit some value. We can pre-fill the box with the old value.

{% include file="examples/js/edit.html" %}

[view](examples/js/edit.html)

In either case, if the user presses `cancel` or hits the `ESC` the `prompt()` function will return `null`.

## confirm

The other pop-up is not really an input method. It allows the developer to ask a Yes/No question. Calling the `confirm()`
function will show a pop-up window with the provided texts and with two buttons. If the user presses `OK` the `confirm()`
function will return `true`, if the user presses `cancel` or hits the `ESC` key, the function will return `false`.

Of course in order for this to make more sense you'll have to understand what `true` and `false` really mean and what this
`if - else` construct does. If you have programming background then you probably already understand the code,
and even if you don't have programming background you might figure out.

That code can basically be translated to the following English sentence:

`If confirm returned true, print "Hello World", otherwise print "OK, I won't print it."`

Or even better:

`If the user presses OK when we asked "Shall I print Hello World?", then print "Hello World", otherwise print "OK, I won't print it."`

{% include file="examples/js/confirm.html" %}

[view](examples/js/confirm.html)

## Comments

How do you change the colors of the prompt box?

---

Write a function that takes a grade and returns grade letter using switch case.
Greater or equal to 9 = Grade Letter is A
Greater or equal to 8 = Grade Letter is B
Greater or equal to 7 = Grade Letter is C
Greater or equal to 6 = Grade Letter is D
Less than 6 = Grade Letter is F
You must take this course again

here is my code but its not displaying resul

```
<html>
<head><title>Exercise 1</title>
<script type="text/javascript">
var a = prompt("Please enter youre grade \n",);

function myGrading() {

switch(true) {
case (value >=9):

document.getElementById("cs").innerHTML = "Grade letter is A";
break;
case (value >=8):

document.getElementById("cs").innerHTML = "Grade letter is B";
break;
case (value >=7):

document.getElementById("cs").innerHTML = "Grade letter is C";
break;
case (value >=6):

document.getElementById("cs").innerHTML = "Grade letter is D";
break;
case (value <6):

document.getElementById("cs").innerHTML = "Grade letter is F";
break;

default:
return 'INVALID SCORE';
}

return gscore;
}

</script>
</head>

<body>

Result:

</body>
</html>.
```


---

very helpful, thank u

---

1 2 3 4 5
1 2 3 4
1 2 3
1 2
1

can u plz give me the answer. using js loop method


---

You shoud really figure this out by yourself, it's not that big of a deal. You can achieve this by doing:
var a = [ 1, 2, 3, 4, 5 ];
for (var i = a.length; i > 0; i--) {
var line = "";
for (var j = 0; j < i; j++) line += a[j] + " ";
console.log(line);
}

Also, it really depends on what you try to achieve with this. So this solution might not be your right solution.

---

