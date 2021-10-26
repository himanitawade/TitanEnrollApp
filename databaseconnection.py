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
   print(studentId)
  # query will get all available courses
   cur.execute(f"""SELECT Courses.CoursesName,Professor.firstname+Professor.lastname,Classes.Timeslot,Classes.ClassID,Courses.Unit FROM classStudentList 
                  JOIN Classes 
                  ON classStudentList.classID = Classes.ClassID 
                  JOIN Courses
                  ON Courses.CourseID = Classes.CourseID 
                  JOIN Professor
                  ON Classes.ProfessorID = Professor.ProfessorID
                  Where classStudentList.studentID='{studentId}'
                  """)
   
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
            if not student:
               return False
            else:
               return student[0]

##########################################################################
### function for class registration (enrollment) #################
   # This function will take input of classid and and studentid
   # First: It will check the class have available seats or not. 
   # If there is available seat, then it will update with one addition of enrollment.
   # After fixing that, It will update the classstudentlist with studentid and classid

def classenrollment(studentid,classid):
   
   capacity=0
   remaining=0
   enrolled=0
   state=""
   # query to get current remaining seats with class capacity
   cur.execute(f"""SELECT Classes.classCapacity,Classes.RemainingSeats,Classes.Enrolled,Classes.Status FROM Classes Where Classes.ClassID={classid}""")

   # getting the remaining and class capacity data into variable
   for data in cur:
      capacity=data[0]
      print('capacity',capacity)
      remaining=data[1]
      print('remaining',remaining)
      enrolled=data[2]
      print('enrolled',enrolled)
      state=data[3]
      print('state',state)


      #print('remaining',remaining)
   
   # If the remaining seats are less than classcapasity, then enroll student and update the database
   #else send a message that class is fully enrolled, cannot enroll in this class.
   if (remaining < capacity) and (state=="Open"):
      print("HAPPENING")
      remaining = remaining - 1
      print('new remaining',remaining)
      enrolled= enrolled + 1
      print('new enrolled',enrolled)
      #Before doing update - check the enrolled and capacity is equal or not to change class status
      if enrolled == capacity:
         state="Close"
     
      try:
         # Query to insert student record with enrolled class.
         cur.execute(f""" INSERT INTO classStudentList VALUES ({classid},{studentid})""")
         # Query to update that class information that neeeded for enrollment functionality
         cur.execute(f"""UPDATE Classes SET Classes.RemainingSeats={remaining}, Classes.Enrolled={enrolled},Classes.Status='{state}' Where Classes.ClassID={classid} """)
         #cur.commit()
      except Exception as e:
         # print(e.args[0])
         # print(type(e.args[0]))
         #if the exception is the duplciate entry in classStudentList - means student is trying to enroll in class which is already enrolled by that student
         if(e.args[0]== '23000'):
            print(" You are trying to enroll the class in which you are already enrolled.")
            return f' You are trying to enroll the class in which you are already enrolled.'
      else:
         cur.commit()
         #cur.close()
      return f"Successfully Enrolled"
   elif (enrolled==capacity) and (state=="Close"):
      return f"You cannot enroll this class because it is already Fully Enrolled."