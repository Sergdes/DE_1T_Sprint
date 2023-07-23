
CREATE TYPE grade_type AS ENUM ('junior', 'midle', 'senior');
CREATE TYPE score_type AS ENUM ('A','B','C', 'D', 'E');
--1. Создание даблицы сотрудников
CREATE TABLE IF NOT EXISTS employees(
id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	surname VARCHAR (255) NOT NULL,
	birthdate DATE NOT NULL,
	startdate DATE NOT NULL,
	grade grade_type NOT NULL,
	salary INT,
	departament_id INT,
	driver_license BOOLEAN,
	CONSTRAINT departament_fk
		FOREIGN KEY (departament_id)
		REFERENCES departaments(id)
		ON DELETE CASCADE)

--2. Создание таблицы отделов
CREATE TABLE IF NOT EXISTS departaments(
id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name VARCHAR (255) NOT NULL,
	derictory_name VARCHAR (255),
	employees_count SMALLINT )

----3. 
CREATE TABLE IF NOT EXISTS scores (
employees_id INT PRIMARY KEY,
	q1 score_type,
	q2 score_type,
	q3 score_type,
	q4 score_type,
	CONSTRAINT employees_fk
		FOREIGN KEY (employees_id)
		REFERENCES employees(id)
		ON DELETE CASCADE)
--Наполнение
insert INTO scores(
employees_id,
	q1,
	q2,
	q3,
	q4
)
VALUES 
	(1,'C','B', 'B', 'A'),
	(2,'C','E', 'B', 'A'),
	(3,'A','A', 'B', 'C'),
	(4,'C','C', 'B', 'C'),
	(5,'A','D', 'B', 'C'),
	(6,'A','B', 'B', 'A'),
	(7,'C','B', 'C', 'A')
;
--4.--Вставка значений в таблицы
INSERT INTO departaments (
	name,
	derictory_name,
	employees_count
)
VALUES 
('data engineer', 'Ivanov', 3),
('engineer ASU', 'Petrov', 2),
('data anlyst', 'Sidorov', 1);


INSERT INTO employees (
	surname,
	birthdate,
	startdate,
	grade,
	salary,
	departament_id,
	driver_license
)	

VALUES
('Ivanov','1995-02-27','2022-02-27', 'midle', 15000, 1, True),
('Petrov','1994-03-11','2022-02-27', 'junior', 80000, 2, True),
('Orlov','1992-09-02','2022-02-27', 'senior', 256000, 1, True),
('Pushkin','1990-06-16','2022-02-27', 'midle', 135000, 1, True),
('Kuznetcov','1990-02-11','2022-02-27', 'junior', 70000, 2, True);

5. Добавление отдела и сотрудника
INSERT INTO departaments (
	name,
	derictory_name,
	employees_count
)
VALUES 
('engineer designer', 'Sidorov', 4);


INSERT INTO employees (
	surname,
	birthdate,
	startdate,
	grade,
	salary,
	departament_id,
	driver_license
)	

VALUES
('Bbrov','1990-02-11','2022-10-12', 'midle', 10000, 4, True),
('Munov','1991-11-11','2022-10-12','midle', 10000, 4, True)
;
--6. 
select * from employees e;
--6.1
select id, surname, startdate from  employees e ;
--6.2
select id, surname, startdate from  employees e limit 3;
--6.3
select id from  employees e  where driver_license= true;
--6.5
SELECT 	id FROM employees e WHERE q1 IN ('D','E') OR q2 IN ('D','E') OR q3 IN ('D','E') OR q4 IN ('D','E');
--6.5--максимальная зарплата
select max(salary) from employees