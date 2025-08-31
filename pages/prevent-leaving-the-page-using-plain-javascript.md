---
title: "Prevent leaving the page using plain JavaScript"
timestamp: 2016-01-26T19:50:01
tags:
  - onbeforeunload
published: true
books:
  - javascript
author: szabgab
archive: true
---


In many case, but espeically in single-page applications when there is some unsaved data in the browser you might want to make
sure the user does not accidently leave the page without first saving the data. This can be achived using the `onbeforeunload`
(read "on before unload") event.


This even will trigger whenever the user is trying to leave the page by

* clicking the "Back" button
* reloading the page
* typing in a new URL
* clicking on a link on your page
* or even when trying to close the current tab or the whole browser

In the following example, that you can try by clicking on the "Try" link, you can see how it is implemented.

{% include file="examples/js/prevent_leaving_the_page.html" %}

[view](examples/js/prevent_leaving_the_page.html)

We just need to assign a function to the `window.onbeforeunload` attribute and that function needs
to return something. That will tell the browser that it should display a pop-up window asking the user if she
wants to leave the page. 

Firefox will just ask `This page is asking you to confirm that you want to leave - data you have entered may not be saved.`.<br>
<img src="/img/firefox_confirm_navigate.png" title="Firefox: This page is asking you to confirm that you want to leave - data you have entered may not be saved."><br>

Chrome will be more specific "Confirm Reload" + "Are you sure you want to reload this page?",<br>
<img src="/img/chrome_confirm_reload.png" title="Chrome: Confirm Reload - Are you sure you want to reload this page?"><br>

or "Confirm Navigation" + "Are you sure you want to leave this page?"<br>
<img src="/img/chrome_confirm_navigation.png" title="Chrome: Confirm Navigation - Are you sure you want to leave this page?"><br>

It will even include the text we returned from the function.

Safari will ask "Are you sure you want to leave this page?" and include our text.<br>
<img src="img/safari_leave_page.png" title="Safari: Are you sure you want to leave this page?"><br>

Opera totally disregarded the code. I wonder if it would work if the JavaScript code was in a separate file.

If the function does not call `return` and just falls out at the end of the function,
or if it calls `return;` without returning any value then the the browser will not ask anything
and it will just do whatever we told it to do. (Reload the page, navigate away, etc.)

This allows us write some conditional code that will only show the popup of there is any data
that needs saving.

```javascript
window.onbeforeunload = function() {
   if (data_needs_saving()) {
       return "Do you really want to leave our brilliant application?";
   } else {
      return;
   }
};
```



## Comments

window.onbeforeunload = function() { return; };
I tried to return nothing to disable the pop up. But, it does not work

---

you have to return undefined

---

Hi, I have a situation, where I am opening a new window from my main application as a new tab. I need to prompt the message while the user tries to close the new tab. I have given the code as below.

```
<script>
window.onbeforeunload = function () {
return "Do you really want to leave our brilliant application?";

};
</script>
```

But when I click on the X button, the new tab closes without prompting the message. Please suggest.

---

copied the same code but not working in chrome (not even any browser!!). Getting the default message only as below:
"Changes you made may not be saved."
---
Many browsers have reverted that feature.

See https://caniuse.com/?search=onbeforeunload

---

Hi, this doesn't work on IOS (either Safari & Chrome).
Do you have workaround for that?

---

https://stackoverflow.com/questions/7317273/warn-user-before-leaving-web-page-with-unsaved-changes/7317311#7317311


window.addEventListener("beforeunload", function (e) {
    var confirmationMessage = 'It looks like you have been editing something. '
                            + 'If you leave before saving, your changes will be lost.';

    (e || window.event).returnValue = confirmationMessage; //Gecko + IE

    return confirmationMessage; //Gecko + Webkit, Safari, Chrome etc.
});

---

This doesn't work anymore in Safari

---
You can tell the guy who published that solution on stack-overflow. He might help you on this :)

---

Thanks for the code man :D




