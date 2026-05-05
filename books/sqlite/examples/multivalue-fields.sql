CREATE TABLE grades (
  student TEXT,
  subjects TEXT,
  grades  TEXT
);

INSERT INTO grades (student, subjects, grades) VALUES ('Joe', 'Math,Chemistry,Programming', '27,89,32');
INSERT INTO grades (student, subjects, grades) VALUES ('Jane', 'Math,Literature,Physics', '99,100,97');

SELECT * FROM grades;
