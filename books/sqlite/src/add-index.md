# INDEX

Adding `INDEX` to a table might speed up certain request.

{% embed include file="examples/big-data-time.sql" %}

```shell
$ sqlite3 < examples/big-data-time.sql
```

{% embed include file="examples/big-data-time.out" %}


* The 1st SELECT takes 0.005019 seconds. That's going over all the rows.
* The 3rd SELECT takes 0.000018 seconds. That's because having and index allows SQLite to go directly to the right row.

* The `CREATE INDEX` statement takes 0.027671 seconds. So it is very time consuming and also uses extra memory. It starts to be worth doing it if you run the select at least 7 times. (In this specific case.)
