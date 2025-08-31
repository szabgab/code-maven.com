---
title: "CSV - Comma Separated Files"
timestamp: 2016-05-31T15:00:01
tags:
  - CSV
published: true
author: szabgab
archive: true
---


CSV stands for Comma Separated Values, though in reality, the character that separates the values can be anything.
`,` is probably the most popular one, but there are plenty of files where the separator is semi-colon `;`.
In other places it is `|`, and yet in other places it is a `\t` TAB.
The latter is usually also called TSV - Tab Separated Values.

We'll just use the name <b>CSV</b> and mean any of these cases.


A CSV file is great for representing table-like data. Something you could also store in Excel,
[Calc of Libre Office](https://www.libreoffice.org/discover/calc/), or any other Spreadsheet application.
Without the formatting and without the calculating of expressions. Just the raw data.

A CSV file can be seen as a table from a relational database, one that you'd normally interrogate using SQL.
If you need to represent multiple SQL tables, that will require one CSV file for each table.

A rather simple example looks like this:

{% include file="examples/data/process_csv_file.csv" %}

Here each field is separated by a semi-colon `;` and each physical row represents one row in the table.

(Data: [Snowwhite and the 7 Dwarfs](https://hu.wikipedia.org/wiki/H%C3%B3feh%C3%A9rke) in Hungarian.)

A more complex example is this one:

{% include file="examples/data/distance.csv" %}

(Data: totally made up.)

Here the fields are separated using `,` and we can see two special cases:

## Handle embedded speparator characters

The line starting with "New York" contains a field that has a comma `,` in the middle.
In order to make it clear that the comma between Moscow and East is part of the element the creator of
the CSV file can do two things. Either wrap the element in quotes as happend in this example:

```
New York,"Moscow, East",6000,km
```

The character can also be "escaped" using a back-slash `\`. (Escaping here means that the character looses
its special meaning separating fields.

`New York,Moscow\, East,6000,km`

The software creating the CSV file needs to be able to add these extra marks and the software reading the CSV file must
be able to understand them and interprete them correctly.

## Embedded newline (Multi-line fields)

The second special case can be seen in the lines which comprise a single logical row.
We already know that the quotation character `"` marks the beginning of a field which ends with the next quotation character 
`"`, but in this case that second charcter is in a subsequent physical row. Effectively here we have a field that has a newline
embedded in it.


```
Local,"Remote
Location",10,km
```

If you are familiar with any of the Spreadsheet software you probably have already seen files with a few multi-line fields.
This is how such fields are represented.

Here too, it is very important for the software to be able to parse the file correctly. A simple call to `split`
won't work properly.


## Header or not?

In the earlier examples each row contained data, though rows were not necessary aligned along newlines.

In the next example the first row of the file is the header. In that row the values are the names of the columns similar to
what you would have in a relational database, except that in this case there is no restriction as to what the column
name can contain. So we have one column with a space in the name and another column where the name (the content of the first row)
has both space and parenthese.

{% include file="examples/data/planets.csv" %}

When reading such a file one must treat the first row as special. At a minimum it should not be used it as data,
but maybe it can even be used as way to refernce the values in the various fields.

(Data source [Solar System](https://en.wikipedia.org/wiki/Solar_System). No really.)

## Implementations of CSV parsers


* [CSV in Perl](https://perlmaven.com/csv)
* [CSV in Python 2.x](https://docs.python.org/2/library/csv.html)
* [CSV in Python 3.x](https://docs.python.org/3/library/csv.html)
* [Create CSV in JavaScript](/create-and-download-csv-with-javascript)
* [Read CSV in Ruby](/reading-csv-file-in-ruby)

See also an [exercise to add numbers taken from a CSV file](/exercise-add-numbers-from-csv-file).

