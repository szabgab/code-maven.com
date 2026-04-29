CREATE TABLE flexible_data (
    id INTEGER,
    name TEXT,
    height REAL
);

INSERT INTO flexible_data (id, name, height) VALUES (1, "foo", 1.8);
INSERT INTO flexible_data (id, name, height) VALUES ("id", 23, "tall");

SELECT * from flexible_data;

