CREATE TABLE person (
    name TEXT,
    subject TEXT,
    grade INTEGER
);

INSERT INTO person (name, subject, grade) VALUES
    ('Jane',  'Chemistry', 62),
    ('Jane',  'Physics', 70),
    ('Jane',  'Math', 23),
    ('Joe',   'Chemistry', 45),
    ('Joe',   'Physics', 85),
    ('Joe',   'Math', 77),
    ('Peter', 'Chemistry', 35),
    ('Peter', 'Physics', 63),
    ('Mary',  'Chemistry', 95),
    ('Dean', 'Physics', 100),
    ('Dana', 'Math', 97),
    ('George', 'Math', 97),
    ('George', 'Chemistry', 45);


SELECT * FROM person;

