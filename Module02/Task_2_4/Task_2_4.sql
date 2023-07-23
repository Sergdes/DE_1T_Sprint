--// a. Попробуйте вывести не просто самую высокую зарплату во всей команде, а вывести именно фамилию сотрудника с самой высокой зарплатой.//--

SELECT surname||' '||CASE WHEN name_employee IS NOT NULL THEN (name_employee||' ') END || patronymic,salary FROM employees WHERE salary=(SELECT MAX(salary) FROM employees);

--// b. Попробуйте вывести фамилии сотрудников в алфавитном порядке.//--

SELECT surname FROM employees ORDER BY surname ASC;

--//c. Рассчитайте средний стаж для каждого уровня сотрудников.//--

SELECT grade,AVG(NOW()-start_date) FROM employees GROUP BY grade;

--//d. Выведите фамилию сотрудника и название отдела, в котором он работает.//--

SELECT e.surname,d.name FROM employees e LEFT JOIN departaments AS d ON d.id=e.departament_id;

--//e. Выведите название отдела и фамилию сотрудника с самой высокой зарплатой в данном отделе и саму зарплату также.//--

with salary AS (SELECT e.departament_id,MAX(e.salary) sal FROM employees e GROUP BY e.departament_id) 
SELECT d.name,salary.sal,e.surname FROM departaments d LEFT JOIN salary ON salary.departament_id=d.id LEFT JOIN employees e ON e.departament_id=d.id AND salary.sal=e.salary;