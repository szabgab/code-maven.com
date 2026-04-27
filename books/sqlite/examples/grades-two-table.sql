PRAGMA foreign_keys = ON;

CREATE TABLE ubjects (
    id INTEGER NOT NULL,
)

CREATE TABLE person (
    name TEXT,
    subject TEXT,
    grade INTEGER
);

INSERT INTO person (name, subject, grade) VALUES ('Jane',  'Chemistry', 62);
INSERT INTO person (name, subject, grade) VALUES ('Jane',  'Physics', 70);
INSERT INTO person (name, subject, grade) VALUES ('Jane',  'Math', 23);
INSERT INTO person (name, subject, grade) VALUES ('Joe',   'Chemistry', 45);
INSERT INTO person (name, subject, grade) VALUES ('Joe',   'Physics', 85);
INSERT INTO person (name, subject, grade) VALUES ('Joe',   'Math', 77);
INSERT INTO person (name, subject, grade) VALUES ('Peter', 'Chemistry', 35);
INSERT INTO person (name, subject, grade) VALUES ('Peter', 'Physics', 63);
INSERT INTO person (name, subject, grade) VALUES ('Mary',  'Chemistry', 95);
INSERT INTO person (name, subject, grade) VALUES ('Dean', 'Physics', 100);
INSERT INTO person (name, subject, grade) VALUES ('Dana', 'Math', 97);
INSERT INTO person (name, subject, grade) VALUES ('George', 'Math', 97);
INSERT INTO person (name, subject, grade) VALUES ('George', 'Chemistry', 45);

