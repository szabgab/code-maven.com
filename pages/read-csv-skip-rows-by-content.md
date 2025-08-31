---
title: "read_csv file using Pandas skipping rows based on content"
timestamp: 2023-03-13T16:30:01
tags:
  - Pandas
  - read_csv
  - filter
  - enumerate
published: true
books:
  - python
author: szabgab
archive: true
show_related: true
---


Ideally each CSV file you work with will contain homogeneous data: only one row of header and in ever row similar type of data.
Unfortunately real world sometimes gives us files where several tables are mixed. The question arises how can we read the content
of such file using the [read_csv](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html?highlight=read_csv)
method of Pandas?

One could use the <b>skiprows</b> and the <b>skipfooter</b> parameters, but what if I don't the number of the rows we need to skip?


## The file

This a very short version of a file I just created for the demo. The real file is much, much bigger.

{% include file="examples/data/mixed.csv" %}

This file has 3 different tables in it.


## Read everything


{% include file="examples/python/load_mixed_csv.py" %}

Reading everything will not result in anything useful. The header of the 2nd and the 3rd table are seen as data in the first table.
Along with the content of those tables.

```
          code           from        to         departure length  price  tickets
0      CM 2201            BUD       LTN  2016-05-29 06:00   2:35   80.0     20.0
1      CM 2203            BUD       LTN  2016-05-29 09:00   2:35   80.0     17.0
2      CM 2202            LTN       BUD  2016-06-10 08:10   2:25  120.0      5.0
3  Planet name  Distance (AU)      Mass               NaN    NaN    NaN      NaN
4      Mercury            0.4     0.055               NaN    NaN    NaN      NaN
5        Venus            0.7     0.815               NaN    NaN    NaN      NaN
6       City 1         City 2  distance               NaN    NaN    NaN      NaN
7     Budapest       Bukarest      1200               NaN    NaN    NaN      NaN
8     Tel Aviv         Beirut       500               NaN    NaN    NaN      NaN
```

We could try to fiddle with the dataframe to locate the rows that are relevant to our data, but I thought a much filtering the original data would be
simpler.


## Set the skips manually

Before trying to go to the dynamic solution I wanted to see if the <b>skiprows</b> and <b>skipfooter</b> parameters work as I expect.
So we have a version where we supply these two parameters specific to the sample csv file:

{% include file="examples/python/load_mixed_csv_skip_manually.py" %}

The result is this:

```
  Planet name  Distance (AU)   Mass
0     Mercury            0.4  0.055
1       Venus            0.7  0.815
```

I also had to supply the <b>engine="python"</b> to avoid a warning:
<b>ParserWarning: Falling back to the 'python' engine because the 'c' engine does not support skipfooter; you can avoid this warning by specifying engine='python'.</b>

This also made me worried that maybe this will cause the whole loading to work a lot slower. We'll have to see it on real data.


## Calculate the skips

Finally we have the code to calculate the number of rows automatically. I did not want to do it with Pandas as this solution, where we only care about strings, seems to be much faster.
(But I have not measured it.)

{% include file="examples/python/load_mixed_csv_skip_automatically.py" %}

First we read the content of the csv file into memory as a list of rows. Then we use the <b>get_row</b> function to find the row-number.

<b>enumerate()</b> returns a list of tuples of the form <b>(row_number, row)</b>.

We use the <b>filter</b> on the enumerated list. The filter function takes element 1 of the tuple (which is the current row in the file) and checks if it is equal to the string we supplied.

<b>filter</b> returns a filter object, we use <b>list</b> to flatten it into a list.

Then we make sure we found exactly one such row. I know theoretically the file should be correct and have exactly this format. But I know in reality....
So I prefer to report an error or an ambiguity on the input data then to give false results.

That's it.

I hope this will be useful to someone.

