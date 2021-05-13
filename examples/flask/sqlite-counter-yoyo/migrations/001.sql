CREATE TABLE counter (
	name VARCHAR(80) NOT NULL,
	count INTEGER NOT NULL,
	PRIMARY KEY (name),
	UNIQUE (name)
);
