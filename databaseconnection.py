""" This file have all queries to run on database TITANENROLLDB"""
""" All functions will be called and run the query"""

# pyodbc is the module to connect to sql server
import pyodbc as connector
#connection string with needed information
""" The server name will be differ for all partners"""
connection_string=(r"Driver={SQL Server};"
               r"Server=LTCSUF-24KH0B3\SQLEXPRESS;" # please change this to your server--> run 'select @@SERVERNAME' in sql studio to find your server
               r"Database=TITANENROLLDB;"
               r"Trusted_Connection=yes;")

#connect to the server and database under that server
conn= connector.connect(connection_string)

#create a cursor to work on the database
cur=conn.cursor()

def getlistofavailablecourses(department,program):
  # query will get all available courses
   cur.execute(f"""SELECT Classes.ClassID,Courses.CourseID,Courses.CoursesName,Professor.firstname+Professor.lastname,Classes.Timeslot,Classes.RemainingSeats,Courses.Unit FROM Courses 
                  INNER JOIN Classes 
                     ON Courses.CourseID = Classes.CourseID 
					 INNER JOIN Professor
					 ON Classes.ProfessorID = Professor.ProfessorID""")
   
   availabledata=[]             
   for i in cur:
      availabledata.append(i)
   return availabledata

def getlistofregisteredcourses(studentId):
  # query will get all available courses
   cur.execute(f"""SELECT Courses.CoursesName,Professor.firstname+Professor.lastname,Classes.Timeslot,Classes.ClassID,Courses.Unit FROM Courses 
                  INNER JOIN Classes 
                  ON Courses.CourseID = Classes.CourseID
                  INNER JOIN classStudentList 
                  ON classStudentList.classID = Classes.ClassID
                  INNER JOIN Professor
                  ON Classes.ProfessorID = Professor.ProfessorID""")
   
   registeredclasses=[]             
   for i in cur:
      registeredclasses.append(i)
   return registeredclasses

def getlistofcourses(department,program):
   print('server function call')
   # connection_string=(r"Driver={SQL Server};"
   #             r"Server=DELL-K2QI68SB10\NIDHI544APP;"
   #             r"Database=TITANENROLLDB;"
   #             r"Trusted_Connection=yes;")

   # conn= connector.connect(connection_string)

   # cur=conn.cursor()
   
  # query will get all courses on selected department and program
   cur.execute(f"""SELECT Courses.CourseID,Courses.CoursesName,Courses.CourseDescription,Courses.Unit FROM Courses 
                  JOIN Program 
                     ON Courses.ProgramID = Program.ProgramID 
                  JOIN Department
                  ON Program.DepartmentID = Department.DepartmentID
                  Where Department.DepartmentName='{department}' AND Program.Programname='{program}'""")


 # print the list of query result
   courselist=[]
   for i in cur:
      course=[]
      for j in i:
         course.append(j)
         #print(j,'\n')
      courselist.append(course)
   #print(courselist)
   
   return courselist

### To authenticate user credentials
def authenticateUser(username,password):
      if username=="" or password=="":
         return False
      else:
         cur.execute(f"""SELECT Student.StudentID FROM Student WHERE username='{username}' AND upassword='{password}'""")
         student=[]
         for i in cur:
            student.append(i)
            print(student[0][0])
            if not student:
               return False
            else:
               return student[0]