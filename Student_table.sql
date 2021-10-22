/****** Script for Inserting Student Information  ******/

INSERT INTO Student(firstname,lastname,Email,username,upassword,admittedYear,admittedSemester,phonenumner,DepartmentID,ProgramID)
VALUES
('Jeevika','Yarlagadda','jeevika@gmail.com','jy','jeevi123',2021,'Fall',98675646,(SELECT DepartmentID FROM DEPARTMENT WHERE DepartmentName='Computer Science'),(SELECT ProgramID FROM Program WHERE Programname='Bachelor in Computer Science')),
('Nidhi','Shah','nidhi@gmail.com','ns','nidhi123',2021,'Fall',98675647,(SELECT DepartmentID FROM DEPARTMENT WHERE DepartmentName='Computer Science'),(SELECT ProgramID FROM Program WHERE Programname='Bachelor in Computer Science')),
('Himani','Tawade','Himani@gmail.com','ht','Hima123',2021,'Fall',98675648,(SELECT DepartmentID FROM DEPARTMENT WHERE DepartmentName='Computer Science'),(SELECT ProgramID FROM Program WHERE Programname='Bachelor in Computer Science')),
('Abhiruch', 'Shinde','Abhi@gmail.com','as','Abhi123',2021,'Fall',98675649,(SELECT DepartmentID FROM DEPARTMENT WHERE DepartmentName='Computer Science'),(SELECT ProgramID FROM Program WHERE Programname='Bachelor in Computer Science'))

use TITANENROLLDB
select * from Courses
select * from Classes
select * from Program

use TITANENROLLDB
select * from Student

select * from classStudentList

select * from Professor

select * from Department


INSERT INTO Professor
VALUES ('Doina','Bein','doinabein@gmail.com',100)
INSERT INTO Classes
				VALUES('Virtual','Spring',2022,'2022-01-01','2022-04-01',120,'MW 6:30PM-10:45PM',30,10,20,'Open','CPSC544',2000);

SELECT Classes.ClassID,Courses.CourseID,Courses.CoursesName,Professor.firstname+Professor.lastname,Classes.Timeslot,Classes.RemainingSeats FROM Courses 
INNER JOIN Classes 
ON Courses.CourseID = Classes.CourseID 
INNER JOIN Professor
ON Classes.ProfessorID = Professor.ProfessorID

INSERT INTO Student values('Nidhi','S','abcd@gmail.com','nidhi','abc',2021,'fall',99999999,100,2)
INSERT INTO Student values('Jeevika','Yarlagadda','abc@gmail.com','Jeevika','abc',2021,'fall',999999999,100,2)

INSERT INTO classStudentList values(57000,80000000)
INSERT INTO classStudentList values(57001,80000004)

SELECT Courses.CoursesName,Professor.firstname+Professor.lastname,Classes.Timeslot,Classes.ClassID,Courses.Unit FROM classStudentList 
JOIN Classes 
ON classStudentList.classID = Classes.ClassID 
JOIN Courses
ON Courses.CourseID = Classes.CourseID 
JOIN Professor
ON Classes.ProfessorID = Professor.ProfessorID
Where classStudentList.studentID=80000000

SELECT Courses.CoursesName,Professor.firstname+Professor.lastname,Classes.Timeslot,Classes.ClassID,Courses.Unit FROM Courses 
INNER JOIN Classes 
ON Courses.CourseID = Classes.CourseID
INNER JOIN classStudentList 
ON classStudentList.classID = Classes.ClassID 
INNER JOIN Professor
ON Classes.ProfessorID = Professor.ProfessorID

