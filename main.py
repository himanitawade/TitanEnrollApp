from typing import Text
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard
from databaseconnection import getlistofcourses
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.expansionpanel import MDExpansionPanel,MDExpansionPanelTwoLine
from kivymd.uix.list import TwoLineListItem,OneLineListItem
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from databaseconnection import getlistofavailablecourses
from databaseconnection import getlistofregisteredcourses
from kivymd.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton,MDIconButton
from databaseconnection import authenticateUser
from databaseconnection import classenrollment

studentID = ''

class HomePage(MDScreen):
    pass

class LoginPage(MDScreen):
    dialog = None
    
    def ShowLoginErrorMessage(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text = "Invalid Username/Password",
                #size_hint=(.8, None),
                #height=dp(200),
            )
        self.dialog.open()  
        
    def Login(self,username,password):
        self.studentId = authenticateUser(username,password)
        if self.studentId:
            studentID = self.studentId
            self.manager.current = "enrollmentpage"
        else:
            self.ShowLoginErrorMessage()                    

class EnrollmentPage(MDScreen):
    Home = HomePage();
    dialog = None
    availablecourseslist=ObjectProperty(None)

    def getRowData(self, dbList): 
        data = []
		#append each row of data fetched from db into an array
        for i in dbList:
            data.append(i)
        return data
        
    def getStudentCourses(self,courses):
        list=[]
        for i in courses:
            list.append(i)
            print(i)
        return list 

    def dialog_close(self, obj):
        self.dialog.dismiss()
    
    def navigateToHomePage(self,obj):
        self.manager.current = 'homepage'

    def checked(self, instance_table, instance_row):
		#get the dblist
        print(studentID)
        dbList = self.getRowData(getlistofavailablecourses('Computer Science', 'Master in Computer Science'))
        if(instance_row.index/6>=0):
            #Successfully Enrolled
            #You cannot enroll this class because it is already Fully Enrolled.
            # You are trying to enroll the class in which you are already enrolled.
            enrollResult = classenrollment(studentID,dbList[int(instance_row.index/6)][0])
            
            if not self.dialog:
                self.dialog = MDDialog(
                    text = enrollResult,
                    buttons = [MDFlatButton(
                                    text="CLOSE",on_release=self.dialog_close
                                )]
                )
                self.dialog.open()     

    def on_enter(self, *args):
        layout = GridLayout(rows=5,row_default_height=24)
        self.manager.get_screen('enrollmentpage').availablecourseslist.clear_widgets()
        dbList = getlistofavailablecourses('Computer Science', 'Master in Computer Science')
        registeredcourses = getlistofregisteredcourses(studentID) # student ID
        layout.add_widget(MDIconButton(icon = 'home',md_bg_color='orange',
                                        #size_hint =(40,.2),
                                        on_release=self.navigateToHomePage,
                                        pos_hint= {"center_x": .2, "center_y": .2}
                                    ))
        layout.add_widget(Label(text="Registered Courses"
            ,size_hint=(.8, 8)
                ))
        if not registeredcourses:
            print('not yet registered')
            layout.add_widget(Label(text="You are not yet registered into any course for this semester"))
        else:
            registeredtable = MDDataTable(
                pos_hint={'center_x': 100, 'center_y': 0.5},#position
                size_hint=(5, 40),						    #size
                use_pagination=True,						#pagination
                rows_num=3,									#initial no for pagination
                pagination_menu_height='240dp',				#menu height for pagination
                pagination_menu_pos="auto",					#menu position
                background_color=[1, 0, 0, .5],				#backgnd color
                #define column data
                column_data=[
                    ("Course Name", dp(30)),
                    ("Professor Name", dp(30)),
                    ("Timeslot", dp(30)),
                    ("ClassID",dp(30)),
                    ("Unit",dp(30))
                ],
                #define row data
                row_data=self.getStudentCourses(registeredcourses)
            )  
            layout.add_widget(registeredtable)

        if not dbList:
            layout.add_widget(Label(text="Currently there are no available courses for this semester"))
        else:    
            table= MDDataTable(
                pos_hint={'center_x': 0.5, 'center_y': 0.5},#position
                size_hint=(50, 40),						#size
                use_pagination=True,						#pagination
                rows_num=3,									#initial no for pagination
                pagination_menu_height='240dp',				#menu height for pagination
                pagination_menu_pos="auto",					#menu position
                background_color=[1, 0, 0, .5],				#backgnd color
                #define column data
                column_data=[
                    ("ClassId", dp(30)),
                    ("CourseID", dp(30)),
                    ("Course Name", dp(30)),
                    ("Prefessor Name", dp(30)),
                    ("Timeslot", dp(30)),
                    ("Remaining Slots", dp(30)),
                    ("Units",dp(30))
                ],
                height=400,
                width=200,
                #define row data
                row_data=self.getRowData(dbList)
            )
            table.bind(on_row_press=self.checked)  

            layout.add_widget(Label(text="Available Courses"))
            layout.add_widget(table) 

        self.manager.get_screen('enrollmentpage').availablecourseslist.add_widget(layout) 
                                                      

class SelectionPage(MDScreen):
   
    spinner_dept = ObjectProperty()
    spinner_prog = ObjectProperty()
   
    
    def spinner_clicked(self,value):
        print(value)
        print(self.manager.get_screen('selectionpage').spinner_dept.text )
    def spinner_clicked_prog(self,value):
        print(value)
        print(self.manager.get_screen('selectionpage').spinner_prog.text )
    
    
class content2(BoxLayout):
    coursedesc=ObjectProperty(None)
    courseunit=ObjectProperty(None)
    
class Content(BoxLayout):
    pass

class DialogPage():
    pass

class CourseCatalogPage(MDScreen):
    displaycatalog=ObjectProperty(None)
    selectedeptandprogram=ObjectProperty(None)
    deaprtment=''
    program=''
    def on_enter(self, *args):
        # get the value of ids from screen 1 to screen2
       # print('((((',self.manager.get_screen('selectionpage').p1.text)
    
        self.deaprtment= self.manager.get_screen('selectionpage').spinner_dept.text
        self.program = self.manager.get_screen('selectionpage').spinner_prog.text
        print("inside course catalog",self.deaprtment)
        print("inside course catalog",self.program)
        ##adjusting department and program selection values for database query
        
        if(self.deaprtment == "computer science"):
            self.deaprtment = "Computer Science"
        if(self.program == "Master" ):
            self.program = "Master in Computer Science"
        elif (self.program == "Bachelor" ):
            self.program = "Bachelor in Computer Science"
            
        self.manager.get_screen('catalogpage').selectedeptandprogram.text=f'Course Catalog For \n Department: {self.deaprtment} \nProgram: {self.program}'
        
        #call the database query function
        if (len(self.deaprtment) != 0  and len(self.program) !=0):
            data=getlistofcourses(self.deaprtment,self.program)
        #  if there is data rsult from the query, the data need to collect in a way that will show in next page
            if not data:
                print('no data found')
            else:
                #self.manager.get_screen('catalogpage').displaycatalog.add_widget(MDLabel(text='result'))
                
                for course in data:
                    insight=content2()
                    #innerdata=Content()
                    #innerdata.add_widget(OneLineListItem(text=course[2],size_hint_y=None,height=50))
                   # insight.add_widget(MDCard(orientation='vertical', title='nidhi',body='data'))
                    print('coursedesc:',insight.coursedesc.text)
                    print('courseunit:',insight.courseunit.text)
                    insight.coursedesc.text=f' Description:\n {course[2]}'
                    print(type(insight.coursedesc.text))
                    print(type(course[2]))
                    insight.courseunit.text= f'Unit: {course[3]}'
                    
                    self.manager.get_screen('catalogpage').displaycatalog.add_widget(
                                                            MDExpansionPanel(
                                                                icon=f"{'Images2/'}folder.png",
                                                                content = insight,
                                                                panel_cls=MDExpansionPanelTwoLine(
                                                                                text=str(course[0]),
                                                                                secondary_text=str(course[1])
                                                                                )
                                                            )
                                                        ) 

    #GOing Back to selection page
    def Gobacktoselectionwork(self):
            self.manager.get_screen('catalogpage').displaycatalog.clear_widgets()
#####################################################################################################               
                   
        

############################## SCREEN MANAGER ##########################
class PageManager(ScreenManager):
    pass

#########################################################################

################# MAIN APP CLASS #################################
class TitanEnrolHelper(MDApp):
   
    def __init__(self,**kwargs):
        super(TitanEnrolHelper,self).__init__(**kwargs)
        self.root= Builder.load_file('pagescreen.kv')

    def logger(self):
        self.root.ids.CSU_Login.text = f'Hi {self.root.ids.user.text}!'

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette= "Blue"
        self.theme_cls.accent_palette= "Orange"
        
       
        return self.root
    

######################################################
#run the application
##using command line call
if __name__ == '__main__':
    TitanEnrolHelper().run()

#without command line in IDE
TitanEnrolHelper().run()
###################################################
