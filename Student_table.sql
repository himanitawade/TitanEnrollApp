/****** Script for Inserting Student Information  ******/

INSERT INTO Student(firstname,lastname,Email,username,upassword,admittedYear,admittedSemester,phonenumner,DepartmentID,ProgramID)
VALUES
('Jeevika','Yarlagadda','jeevika@gmail.com','jy','jeevi123',2021,'Fall',98675646,(SELECT DepartmentID FROM DEPARTMENT WHERE DepartmentName='Computer Science'),(SELECT ProgramID FROM Program WHERE Programname='Bachelor in Computer Science')),
('Nidhi','Shah','nidhi@gmail.com','ns','nidhi123',2021,'Fall',98675647,(SELECT DepartmentID FROM DEPARTMENT WHERE DepartmentName='Computer Science'),(SELECT ProgramID FROM Program WHERE Programname='Bachelor in Computer Science')),
('Himani','Tawade','Himani@gmail.com','ht','Hima123',2021,'Fall',98675648,(SELECT DepartmentID FROM DEPARTMENT WHERE DepartmentName='Computer Science'),(SELECT ProgramID FROM Program WHERE Programname='Bachelor in Computer Science')),
('Abhiruch', 'Shinde','Abhi@gmail.com','as','Abhi123',2021,'Fall',98675649,(SELECT DepartmentID FROM DEPARTMENT WHERE DepartmentName='Computer Science'),(SELECT ProgramID FROM Program WHERE Programname='Bachelor in Computer Science'))



