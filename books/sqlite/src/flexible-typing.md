# Flexible typing

[The Advantages Of Flexible Typing](https://sqlite.org/flextypegood.html)

Here, although we declared the types of the fields, we can insert any type of value.

{% embed include file="examples/flexible-data.sql" %}

```
$ sqlite3 < examples/flexible-data.sql
```

{% embed include file="examples/flexible-data.out" %}
