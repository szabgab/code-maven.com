CREATE TABLE flexible (
    id INTEGER,
    name TEXT,
    height REAL
);

INSERT INTO flexible (id, name, height) VALUES (1, 'foo', 1.8);
INSERT INTO flexible (id, name, height) VALUES ('id', 23, 'tall');

SELECT * from flexible;

