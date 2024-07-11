DO
$do$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_database WHERE datname = 'library_db') THEN
      PERFORM dblink_exec('dbname=' || current_database(), 'CREATE DATABASE library_db');
   END IF;
END
$do$;


\c library_db;

CREATE TABLE IF NOT EXISTS authors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors(id)
);

CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);


CREATE TABLE IF NOT EXISTS book_category (
    book_id INTEGER,
    category_id INTEGER,
    PRIMARY KEY (book_id, category_id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);


INSERT INTO authors (first_name, last_name) VALUES
('Ліна', 'Костенко'),
('Тарас', 'Шевченко'),
('Іван', 'Франко');

INSERT INTO books (title, author_id) VALUES
('Маруся Чурай', 1),
('Кобзар', 2),
('Захар Беркут', 3);

INSERT INTO categories (name) VALUES
('Поезія'),
('Історична проза'),
('Класика української літератури');

INSERT INTO book_category (book_id, category_id) VALUES
(1, 3),
(2, 1),
(3, 2),
(2, 3),
(3, 3);