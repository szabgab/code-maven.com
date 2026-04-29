
-- enforce foreignk key integrity
PRAGMA foreign_keys = ON;

CREATE TABLE subject (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE person (
    name TEXT,
    subject_id INTEGER REFERENCES subject(id),
    grade INTEGER
);

INSERT INTO subject (id, name) VALUES
    (1, 'Chemistry'),
    (2, 'Physics'),
    (3, 'Math');

INSERT INTO person (name, subject_id, grade) VALUES
    ('Jane', 1, 62),
    ('Jane', 2, 70),
    ('Jane', 3, 23),
    ('Joe', 1, 45),
    ('Joe', 2, 85),
    ('Joe', 3, 77),
    ('Peter', 1, 35),
    ('Peter', 2, 63),
    ('Mary', 1, 95),
    ('Dean', 2, 100),
    ('Dana', 3, 97),
    ('Gerorge', 3, 97),
    ('Gerorge', 1, 45);

SELECT * FROM subject;
SELECT * FROM person;

SELECT person.name, subject.name AS subject, person.grade FROM person, subject WHERE person.subject_id = subject.id;
