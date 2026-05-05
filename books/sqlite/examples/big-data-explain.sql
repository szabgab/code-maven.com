.import --csv -v examples/big-data.csv pairs

EXPLAIN SELECT * from pairs WHERE name = 'aaaaaaaz';

CREATE INDEX names ON pairs (name);

SELECT '--------------------------------';
EXPLAIN SELECT * from pairs WHERE name = 'aaaaaaaz';

