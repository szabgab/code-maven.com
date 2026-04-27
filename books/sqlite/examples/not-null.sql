CREATE TABLE plain (
    id INTEGER,
    name TEXT
);

INSERT INTO plain (id, name) VALUES (1, "Joe");
INSERT INTO plain (name) VALUES ("Jane");

SELECT * from plain;

CREATE TABLE restricted (
    id INTEGER NOT NULL,
    name TEXT
);

INSERT INTO restricted (id, name) VALUES (1, "Joe");
INSERT INTO restricted (name) VALUES ("Jane");

SELECT * from restricted;


