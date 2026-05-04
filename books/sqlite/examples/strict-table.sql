CREATE TABLE strict_data (
    id INTEGER,
    name TEXT,
    height REAL
) STRICT;

INSERT INTO strict_data (id, name, height) VALUES (1, 'foo', 1.8);
INSERT INTO strict_data (id, name, height) VALUES ('2', 'bar', '2.1');

INSERT INTO strict_data (id, name, height) VALUES ('three', 'Jane', 1.3);
-- Runtime error near line 10: cannot store TEXT value in INTEGER column strict_data.id (19)

SELECT * from strict_data;


