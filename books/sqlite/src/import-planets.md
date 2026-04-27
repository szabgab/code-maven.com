# Import planets.csv


{% embed include file="examples/planets.csv" %}

```
sqlite> .import --csv planets.csv planets
sqlite> .schema
CREATE TABLE IF NOT EXISTS "planets"(
"Planet name" TEXT, "Distance (AU)" TEXT, "Mass" TEXT);
sqlite> select "Distance (AU)" from planets;
```
