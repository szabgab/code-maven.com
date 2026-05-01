CREATE TABLE person (
    id INTEGER,
    name TEXT,
    email TEXT
);

INSERT INTO person (id, name, email) VALUES (1, 'Foo', 'foo@example.com');
INSERT INTO person (id, name, email) VALUES (2, 'Bar', 'bar@example.com');
SELECT * FROM person;

