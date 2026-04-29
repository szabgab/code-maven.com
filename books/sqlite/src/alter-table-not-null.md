# ALTER TABLE not NULL

What if we would like to add a column that should be `NOT NULL`?

We cannot add a column that is `NOT NULL` as it would immediately violate the integriry of the table.

We can first add the column. Then update the existing rows, then change the column definition.


{% embed include file="examples/add-not-null.sql" %}
