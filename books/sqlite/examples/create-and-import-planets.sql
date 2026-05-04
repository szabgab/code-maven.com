.mode batch

.read examples/planets.sql
.import --csv --skip 1 -v examples/planets.csv planets
SELECT '----------';

.schema
SELECT '----------';

SELECT * FROM planets;
SELECT "Distance (AU)" FROM planets;

