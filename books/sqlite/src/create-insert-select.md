# CREATE - INSERT - SELECT


* CREATE
* INSERT
* SELECT

{% embed include file="examples/create-insert-select.sql" %}

* In memory:

```shell
$ sqlite3 < create-insert-select.sql
Foo|foo@example.com
Bar|bar@example.com
```

* In file:

```shell
$ sqlite3 demo.db < create-insert-select.sql
Foo|foo@example.com
Bar|bar@example.com

$ rm -f demo.db
```


