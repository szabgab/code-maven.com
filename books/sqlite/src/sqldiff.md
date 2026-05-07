# sqldiff

The [sqldiff](https://sqlite.org/sqldiff.html) program comes with the installation of SQLite.
It can help creating migration scripts by showing the differences between two databases.

We have a before and after schema:

{% embed include file="examples/before.sql" %}
{% embed include file="examples/after.sql" %}

We create two `db` files and run the `sqldiff` command on these files.

{% embed include file="examples/sqldiff.sh" %}

This is the output we get:

{% embed include file="examples/sqldiff.out" %}

