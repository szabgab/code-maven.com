---
title: "Create and download data in CSV format using plain JavaScript"
timestamp: 2016-03-23T23:30:01
tags:
  - CSV
published: true
books:
  - javascript
author: szabgab
archive: true
---


There can be cases, especially in Single Page Applications, when you have some data in the browser already
that you have probably received via an Ajax call that you'd like to let your users download.

[CSV](https://en.wikipedia.org/wiki/Comma-separated_values) is a nice and simple format to
keep tabular information.

In this simple example you'll see how to let your users save data from the browser.

This solution only works in the simple case, but it could be improved to handle some of the stranger cases as well.


{% include file="examples/js/download_csv.html" %}

[view](examples/js/download_csv.html)

The `data` is just some array of arrays holding, well, the data. It does not really matter how it got into the browser.

The `download_csv` function that is triggered by the click of the button, will create a string that will become
the content of the file on the disk of the user. In the first line we add the header row and finish it with a newline (`\n`).
Then using a `forEach` loop we add additional lines separating the values with comma (`,`). After all we
are creating a file with comma separated values. Each line is finished with a newline.

Once we have the content in some variable we create a an `a` element and in the link (the `href` part)
we add the URI-encoded version of the future CSV file. We can even add the future name of the file which is 'people.csv'
in our case. Without that Chrome just saved the file calling it 'download.csv'.

The last step is to trigger the newly created element which tell the browser to download the "file".


## Caveat

This solution only handles the case when the data is "simple".
If the data might have comma `,` in it then, in order for the file to work properly we'll have to
put the value with the comma in it inside quotes. This can be added quite easily.

However, what happens if the data can also contain quotes? We will then have to escape those.

This is not "unsolvable" of course, but it needs some more work and currently I did not have the need for that.

## Comments

In Firefox is not working. I click the button and nothing happens.Thanks

---

Firefox requires the download A-element to be present in the DOM before clicking and not created dynamically. So, just add a hidden <a id=dummy_download> or similar and fetch that instead of using createElement and you're set. :)

(This might not be the official explanation, but it works)

<hr>

hye how can i click the save button and it will automatically save into my server not my laptop ?

<hr>
Excellent little example - just what I needed.
Thanks very much Gabor.

<hr>

Hi, is there any check to prevent delimiter inside data? What if any data will contain delimiter (",")? rows and columns wont match. Is there workaround for that? 

<hr>

thanks, very handy!

<hr>

thank you .....its perfect

<hr>

I'm glad you explain each. line of code. Thanks!

<hr>

Thank you

<hr>
Chrome has an issue using encodeURI if the filesize is greater than 1mb. This discussion on StackOverflow shows how to use createObjectURL instead.
https://stackoverflow.com/questions/24610694/export-html-table-to-csv-in-google-chrome-browser/24611096#24611096

<hr>

Hi, It is not working in IE 11. I have added tag in DOM. Whenever call function to download csv, getting alert, "Do you want to open application from this website". After click on Allow csv is not dwonloading. Working fine on chrome. Please help to eun on IE 11.

<hr>

Thank you very much!

<hr>

hello....I need your help...i want to export form data into csv file using plain JS

<hr>

Is there any option to set password for the files.

<hr>

How can we download multiple sheets?

<hr>
what if my delimiter in the string is ; instead of comma
---

Then join with a semi-colon instead;

csv += row.join(';');


<hr>

Thank's for this solution, I'm saved :)

<hr>

i followed the steps hoewever i get my array values written in one row in CSV file, no \n is applied.
my data is an array returned by a function as :
var data = [days];
return data;
and i call this function from the downloadCSV ()

<hr>

Getting the following error: (TypeError: row.join is not a function) Any idea?

<hr>

Hi, How to achieve the same functionality in IE 11 ?

<hr>

Thank you!

