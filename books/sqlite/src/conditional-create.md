# Conditional CREATE

`IF NOT EXISTS` can help us especially with migration scripts.
Both when they are external to the application and when they
are part of the startup code.

In this example the first statement succeeds creating the table.

The second statement fails with an error.

The third statement fails but there is no error.

{% embed include file="examples/conditional-create.sql" %}

```shell
$ sqlite3 < examples/conditional-create.sql
```

{% embed include file="examples/conditional-create.out" %}

