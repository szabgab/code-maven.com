CREATE TABLE IF NOT EXISTS grades (
    student TEXT NOT NULL UNIQUE,
    math INTEGER,
    chemistry INTEGER,
    biology INTEGER,
    physics INTEGER,
    literature INTEGER,
    sport INTEGER,
    drawing INTEGER,
    id INTEGER PRIMARY KEY
);
.import --csv --skip 1 examples/flat-grades.csv grades

SELECT * FROM grades;


---------------------------

CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

SELECT id, student from grades ORDER BY id;

INSERT INTO students SELECT id, student FROM grades;

SELECT * FROM students ORDER BY id;

CREATE TABLE subjects (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL UNIQUE
);

SELECT name FROM pragma_table_info('grades') WHERE name != 'id' AND name != 'student';

INSERT INTO subjects (name) SELECT name FROM pragma_table_info('grades') WHERE name != 'id' AND name != 'student';

SELECT * FROM subjects;

CREATE TABLE new_grades (
    student INTEGER REFERENCES students(id),
    subject INTEGER REFERENCES subjects(id),
    grade INTEGER
);
CREATE UNIQUE INDEX new_grades_index ON new_grades (student, subject);




