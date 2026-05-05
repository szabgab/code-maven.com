# ALTER TABLE after adding data

Here we have a table with two fields (id and name) and with some data in it. Then we inserted some data.

Then we execute `ALTER TABLE` to add another column.

After that we can add new rows, this time already supplying the new field as well.

The old rows will have `NULL` in the new field.

We can also update the old rows to have some value in the field using the `UPDATE` command.


{% embed include file="examples/alter-table-after-adding-data.sql" %}

```shell
sqlite3 < exmples/alter-table-after-adding-data.sql
```

{% embed include file="examples/alter-table-after-adding-data.out" %}

```
╭────┬──────╮
│ id │ name │
╞════╪══════╡
│  1 │ Joe  │
│  2 │ Jane │
╰────┴──────╯
╭────┬──────┬───────╮
│ id │ name │ phone │
╞════╪══════╪═══════╡
│  1 │ Joe  │ NULL  │
│  2 │ Jane │ NULL  │
╰────┴──────┴───────╯
╭────┬────────┬───────────╮
│ id │  name  │   phone   │
╞════╪════════╪═══════════╡
│  1 │ Joe    │ NULL      │
│  2 │ Jane   │ NULL      │
│  3 │ Marcus │ '1234565' │
╰────┴────────┴───────────╯
```
