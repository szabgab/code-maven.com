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

INSERT INTO new_grades (student, subject, grade)
SELECT students.id, subjects.id, flat_grades.grade
FROM (
    SELECT student, 'math' AS subject, math AS grade FROM grades
    UNION ALL
    SELECT student, 'chemistry' AS subject, chemistry AS grade FROM grades
    UNION ALL
    SELECT student, 'biology' AS subject, biology AS grade FROM grades
    UNION ALL
    SELECT student, 'physics' AS subject, physics AS grade FROM grades
    UNION ALL
    SELECT student, 'literature' AS subject, literature AS grade FROM grades
    UNION ALL
    SELECT student, 'sport' AS subject, sport AS grade FROM grades
    UNION ALL
    SELECT student, 'drawing' AS subject, drawing AS grade FROM grades
) AS flat_grades
JOIN students ON students.name = flat_grades.student
JOIN subjects ON subjects.name = flat_grades.subject
WHERE flat_grades.grade IS NOT NULL AND flat_grades.grade != '';

SELECT students.name AS student, subjects.name AS subject, new_grades.grade
FROM new_grades
JOIN students ON students.id = new_grades.student
JOIN subjects ON subjects.id = new_grades.subject
ORDER BY students.id, subjects.id;
