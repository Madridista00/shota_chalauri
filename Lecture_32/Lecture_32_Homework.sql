-- Active: 1712949019593@@127.0.0.1@3306@it_step_db

-- თუ არ გაქვთ შექმნილი, შექმენით მონაცემთა ბაზა სახელად IT_STEP  და შეასრულეთ შემდეგი დავალებები:

-- create database if not exists it_step_db;

-- DROP DATABASE if EXISTS it_step_db;

-- 1. დაწერეთ SQL რომელიც შექმნის Author ცხრილს, რომელსაც ექნება პირველადი გასაღები

CREATE TABLE Author(
    AuthorID int PRIMARY KEY AUTO_INCREMENT,
    AuthorName VARCHAR(50)
)

-- 2. დაწერეთ SQL რომელიც შექმნის Books ცხრილს, სადაც გექნებათ მეორადი გასაღები AuthorID
CREATE TABLE Books(
    BookName VARCHAR(100),
    AuthorID int,
    FOREIGN KEY (AuthorID) REFERENCES Author(AuthorID)
)
;

-- 3. დაწერეთ SQL Author და Books ცხრილებისთვის სადაც შექმნით მინიმუმ 5 ჩანაწერს

INSERT INTO author(`AuthorName`)
VALUES
('J. K. Rowling'),
('Mario Puzo'),
('Charles Dickens'),
('Antoine de Saint-Exupéry'),
('Jack Higgins')
;

INSERT INTO books(`BookName`, `AuthorID`)
VALUES
('Harry Potter and the Chamber of Secrets', 1),
('The Godfather', 2),
('A Tale of Two Cities', 3),
('Harry Potter and the Order of the Phoenix', 1),
('The Little Prince', 4),
('Harry Potter and the Half-Blood Prince', 1),
('The Eagle Has Landed', 5)
;


SELECT * FROM author;
SELECT * FROM books;

-- 4. დაწერეთ SQL Books ცხრილისთვის სადაც გამოიყენებთ update ბრძანებას და გაანახლებთ კონკრეტულ ჩანაწერის ერთ-ერთ ველის მნიშვნელობას

UPDATE books
set `BookName` = 'Harry Potter and the Philosopher\'s Stone'
where `BookName` = 'Harry Potter and the Chamber of Secrets'


SELECT * FROM author;
SELECT * FROM books;

-- 5. ცხრილების დაჯოინება
SELECT `BookName`, `AuthorName` FROM books
JOIN author ON Books.`AuthorID` = Author.`AuthorID`
;

-- 6. წაშალეთ ყველა ჩანაწერი Author და Books ცხრილიდან

DELETE FROM books;
DELETE FROM author;

SELECT * FROM author;
SELECT * FROM books;

-- 7. წაშალეთ Author და Books ცხრილები

DROP Table books;
DROP TABLE author;