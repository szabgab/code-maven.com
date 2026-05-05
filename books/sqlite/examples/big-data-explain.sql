.timer on
.import --csv -v examples/big-data.csv pairs
SELECT COUNT(*) FROM pairs;
SELECT * from pairs WHERE name = 'aaaaaaaz';
EXPLAIN SELECT * from pairs WHERE name = 'aaaaaaaz';

CREATE INDEX names ON pairs (name);

SELECT * from pairs WHERE name = 'aaaaaaaz';
EXPLAIN SELECT * from pairs WHERE name = 'aaaaaaaz';

