CREATE TABLE person (
    id INTEGER,
    name TEXT,
    email TEXT
);

INSERT INTO person (id, name, email) VALUES (1, 'Joe', 'joe@example.com');
INSERT INTO person (id, name, email) VALUES (2, 'Jane', 'jane@example.com');
INSERT INTO person (id, name, email) VALUES (3, 'Mary', 'mary@example.com');
INSERT INTO person (id, name, email) VALUES (4, 'Peter', 'peter@example.com');

SELECT id, name FROM person;

