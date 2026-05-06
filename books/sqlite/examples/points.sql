CREATE TABLE points (
    x INTEGER,
    y INTEGER
);
CREATE UNIQUE INDEX xy_index ON points (x, y);


INSERT INTO points (x, y) VALUES (2, 3);
INSERT INTO points (x, y) VALUES (4, 5);
INSERT INTO points (x, y) VALUES (2, 3);

SELECT * FROM points;
