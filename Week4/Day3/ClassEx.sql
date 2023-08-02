-- Part 1
-- CREATE SEQUENCE mysequence
-- INCREMENT 10
-- START 10;

-- CREATE TABLE DEPARTMENT
-- (
--    DEPTCODE   INTEGER DEFAULT nextval('mysequence') PRIMARY KEY,
--    DeptName   CHAR(30),
--    LOCATION   VARCHAR(33) UNIQUE
-- );

-- CREATE TABLE EMPLOYEE
-- (
--    EmpCode      INTEGER PRIMARY KEY,
--    EmpFName     VARCHAR(15) NOT NULL,
--    EmpLName     VARCHAR(15) NOT NULL,
--    Job          VARCHAR(45),
--    Manager      CHAR(4),
--    HireDate     DATE,
--    Salary       DECIMAL DEFAULT 0,
--    Commission   INTEGER,
--    Department_code	INTEGER REFERENCES DEPARTMENT(DEPTCODE)
-- );


-- Part 2
-- INSERT INTO DEPARTMENT (DeptName,LOCATION) VALUES 
-- ('FINANCE', 'EDINBURGH'),
-- ('SOFTWARE','PADDINGTON'),
-- ('SALES', 'MAIDSTONE'),
-- ('MARKETING', 'DARLINGTON'),
-- ('ADMIN', 'BIRMINGHAM');

-- INSERT INTO EMPLOYEE (EmpCode,EmpFName,EmpLName,Job,Manager,HireDate,Salary,Commission,Department_code)
-- VALUES (9369, 'TONY', 'STARK', 'SOFTWARE ENGINEER', 7902, '1980-12-17', 2800,0,20),
--        (9499, 'TIM', 'ADOLF', 'SALESMAN', 7698, '1981-02-20', 1600, 300,30),    
--        (9566, 'KIM', 'JARVIS', 'MANAGER', 7839, '1981-04-02', 3570,0,20),
--        (9654, 'SAM', 'MILES', 'SALESMAN', 7698, '1981-09-28', 1250, 1400,30),
--        (9782, 'KEVIN', 'HILL', 'MANAGER', 7839, '1981-06-09', 2940,0,10),
--        (9788, 'CONNIE', 'SMITH', 'ANALYST', 7566, '1982-12-09', 3000,0,20),
--        (9839, 'ALFRED', 'KINSLEY', 'PRESIDENT', 7566, '1981-11-17', 5000,0, 10),
--        (9844, 'PAUL', 'TIMOTHY', 'SALESMAN', 7698, '1981-09-08', 1500,0,30),
--        (9876, 'JOHN', 'ASGHAR', 'SOFTWARE ENGINEER', 7788, '1983-01-12',3100,0,20),
--        (9900, 'ROSE', 'SUMMERS', 'TECHNICAL LEAD', 7698, '1981-12-03', 2950,0, 20),
--        (9902, 'ANDREW', 'FAULKNER', 'ANALYST', 7566, '1981-12-03', 3000,0, 10),
--        (9934, 'KAREN', 'MATTHEWS', 'SOFTWARE ENGINEER', 7782, '1982-01-23', 3300,0,20),
--        (9591, 'WENDY', 'SHAWN', 'SALESMAN', 7698, '1981-02-22', 500,0,30),
--        (9698, 'BELLA', 'SWAN', 'MANAGER', 7839, '1981-05-01', 3420, 0,30),
--        (9777, 'MADII', 'HIMBURY', 'ANALYST', 7839, '1981-05-01', 2000, 200, NULL),
--        (9860, 'ATHENA', 'WILSON', 'ANALYST', 7839, '1992-06-21', 7000, 100, 50),
--        (9861, 'JENNIFER', 'HUETTE', 'ANALYST', 7839, '1996-07-01', 5000, 100, 50);

-- Part 3
-- SELECT * FROM DEPARTMENT;
-- SELECT * FROM EMPLOYEE;

-- 1. How many employees are in dept 10. = 3
-- select count(*) from employee where department_code = 10;

-- 2. How many employees are analyst in dept 10. = 1
-- select . How many employees are analyst in dept 10. = 1(*) from employee where department_code = 10 and job = 'ANALYST';

-- 3. Display the names of each employees, their job and dept location
-- select EmpFName,EmpLName,Job, location
-- from employee
-- left join department
-- on employee.department_code = department.deptcode

-- 4. Find the avg salary of the software engineers = 3066.6..../3067
-- select avg(salary) from employee where job = 'SOFTWARE ENGINEER'

-- 5. Create a query that displays EMPFNAME, EMPLNAME, Department_code, DEPTNAME, LOCATION from EMPLOYEE, and DEPARTMENT tables.
--  -- Make sure the results are in the ascending order based on the EMPFNAME and LOCATION of the department.
-- SELECT  employee.EMPFNAME, employee.EMPLNAME, employee.Department_code, department.DEPTNAME, department.LOCATION
-- from employee
-- join department
-- on employee.department_code = department.deptcode
-- order by empfname asc, location asc

-- 6. Display EMPFNAME and "TOTAL SALARY" for each employee (commission and salary)
-- SELECT EmpFname, SUM(salary + commission) from employee group by EmpFname
-- -- #2 option
-- SELECT EMPFNAME, CONCAT(commission + salary) AS TOTAL_SALARY from employee

-- 7. Display MAX SALARY from the EMPLOYEE table. = 7000
-- SELECT MAX(Salary) from employee
-- -- #2 option
-- SELECT EMPFNAME, EMPLNAME, SALARY from Employee
-- where salary = (select max(salary) from Employee)

-- 8. Bonus : Which join should we use to display the employee 9777 even if he has no deptcode?
-- SELECT EMPFNAME, EMPLNAME, salary, empcode, deptcode
-- FROM EMPLOYEE
-- LEFT JOIN DEPARTMENT
-- ON employee.department_code = department.deptcode



-- -- part 4
-- 1
-- create table BOSS (
-- 	boss_id serial primary key,
-- 	boss_name varchar(50),
-- 	boss_type varchar(50),
-- 	dept_number int unique references department(deptcode)
-- )
-- 2
-- insert into boss (boss_name, boss_type, dept_number)
-- values ('Kate', 'angry', (select deptcode from department where deptname = 'FINANCE')),
-- ('Michael', 'funny', (select deptcode from department where deptname = 'MARKETING'))
-- 3
-- SELECT boss_name, boss_type, (select deptname from department where deptcode = dept_number) as dept_name from boss where dept_number = (select deptcode from department where deptname = 'FINANCE').