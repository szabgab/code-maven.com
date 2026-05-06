# Multi-column UNIQUE-ness constraint

Sometimes the each column can have the same value more than once, but 2 (or more column) put together must be unique.
For example in this table we are storing coordinates of points. Both x and y can be any value and the same value can
appear multiple times in either x or y.

However the (x, y) pair must be unique.

Here is how we can accomplish that.

{% embed include file="examples/points.sql" %}

```shell
$ sqlite3 < examples/points.sql
```

{% embed include file="examples/points.out" %}
