DROP TABLE IF EXISTS urls;

ALTER USER debmon WITH PASSWORD 'secretpassword';

CREATE TABLE urls (
    id serial PRIMARY KEY,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    origin VARCHAR(100) NOT NULL,
    final VARCHAR(20) NOT NULL
);