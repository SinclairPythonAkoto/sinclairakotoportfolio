DROP TABLE if exists review_page;
CREATE TABLE review_page (
  id SERIAL PRIMARY KEY,
  firstname VARCHAR,
  lastname VARCHAR,
  email VARCHAR,
  review_message VARCHAR
  );

DROP TABLE if exists feedback_page;
CREATE TABLE feedback_page (
	id SERIAL PRIMARY KEY,
	name VARCHAR,
	experience VARCHAR,
	functionality VARCHAR,
	aesthetics VARCHAR,
	my_cv VARCHAR,
	my_webapp VARCHAR,
	outstanding VARCHAR,
	improve VARCHAR,
	email VARCHAR
);

DROP TABLE if exists contactme_page;
CREATE TABLE contactme_page (
	id SERIAL PRIMARY KEY,
	firstname VARCHAR,
	lastname VARCHAR,
	email VARCHAR,
	exposure VARCHAR,
	message VARCHAR
);