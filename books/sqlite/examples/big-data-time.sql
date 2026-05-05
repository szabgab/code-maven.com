.timer on
.import --csv -v examples/big-data.csv pairs

SELECT * from pairs WHERE name = 'aaaafryc'; -- 'aaaaaaaz';

CREATE INDEX names ON pairs (name);

SELECT * from pairs WHERE name = 'aaaafryc'; -- 'aaaaaaaz';

