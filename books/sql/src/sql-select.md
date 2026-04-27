# SELECT FROM

We use the `SELECT FROM` expression to fetch data from the database. The `*` means that we would like to see all the columns. After the `FROM` we put the table.

Instead of the `*` we could select specific columns, reducing the data transfer. We could also add a `WHERE` clause to filter the rows according to some condition.

We could also use multiple tables and their relationship.

{% embed include file="src/examples/select_all.sql" %}

```
select * from person;
+----------------------+--------+--------+------------+---------------+--------+
| name                 | height | weight | birthday   | occupation    | gender |
+----------------------+--------+--------+------------+---------------+--------+
| Musashimaru Koyo     |   1.92 |    235 | 1971-05-02 | sumo wrestler | male   |
| Tara Nott Cunningham |   1.54 |     48 | 1972-05-10 | weight lifter | female |
| Elisa Di Francisca   |   1.77 |     65 | 1982-12-13 | foil fencer   | female |
| Alfrd Hajos          |   NULL |   NULL | 1878-02-01 | swimmer       | male   |
| Krisztina Egerszegi  |   1.74 |     57 | 1974-08-16 | swimmer       | female |
| Sharran Alexander    |   1.82 |    203 | NULL       | sumo wrestler | female |
+----------------------+--------+--------+------------+---------------+--------+
6 rows in set (0.00 sec)
```



