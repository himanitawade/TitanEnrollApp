""" This file have all queries to run on database TITANENROLLDB"""
""" All functions will be called and run the query"""

# pyodbc is the module to connect to sql server
import pyodbc as connector
#connection string with needed information
""" The server name will be differ for all partners"""
connection_string=(r"Driver={SQL Server};"
               r"Server=DELL-JMD7R7JF08\CPSC544NIDHI;" # please change this to your server--> run 'select @@SERVERNAME' in sql studio to find your server
               r"Database=TITANENROLLDB;"
               r"Trusted_Connection=yes;")

#connect to the server and database under that server
conn= connector.connect(connection_string)

#create a cursor to work on the database
cur=conn.cursor()


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