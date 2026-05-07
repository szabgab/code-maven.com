# INSERT or UPDATE (replace)

`ON CONFLICT`

This statement will try to `INSERT` a row, but if the `name` is already in the database
then it will update the `recent` field. The `exclude.recent` is the value we tried to insert.
It can be used instead of duplicating the value of the `recent` field.

The first statement will INSERT a row. (because 'Joe' was not in the database yet)

The second statement will UPDATE the `recent` field of Joe.

{% embed include file="examples/insert-or-replace.sql" %}

{% embed include file="examples/insert-or-replace.sql" %}

{% embed include file="examples/insert-or-replace.out" %}
