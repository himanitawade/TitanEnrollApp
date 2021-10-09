from typing import Text
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from kivymd.uix.card import MDCard
from databaseconnection2 import getlistofcourses
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.expansionpanel import MDExpansionPanel,MDExpansionPanelTwoLine
from kivymd.uix.list import TwoLineListItem,OneLineListItem
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

#Window.size=(400,500)
############################################## MAIN PAGE
class HomePage(MDScreen):
    pass
# ################################################ SELECTION DEPARTMENT AND PROGRAM PAGE
class SelectionPage(MDScreen):
    #make sure the d1 and p1 have values as in the database entry
    d1 = ObjectProperty(None)
    p1= ObjectProperty(None)
    #department=''
    #program=ObjectProperty(None)
    def viewcoursecatalog(self):
        ########################################
        # Code need to be done to make sure the variable course catalog page need its value should be similar as database value
        # for master - Master in Computer Science
        #################################
        #self.department='Computer Science'
       # self.p1.text='Master in Computer Science'
        print('Button has pressed')
      
#########################################################3  
# ########## ############################### COURSE CATALOG VIEW PAGE      

class content2(BoxLayout):
    coursedesc=ObjectProperty(None)
    courseunit=ObjectProperty(None)
class Content(BoxLayout):
    pass
class CourseCatalogPage(MDScreen):
    displaycatalog=ObjectProperty(None)
    selectedeptandprogram=ObjectProperty(None)
    deaprtment=''
    program=''
    def on_enter(self, *args):
        # get the value of ids from screen 1 to screen2
       # print('((((',self.manager.get_screen('selectionpage').p1.text)
    
        self.deaprtment= self.manager.get_screen('selectionpage').d1.text
        self.program = self.manager.get_screen('selectionpage').p1.text
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
        self.root= Builder.load_file('pagescreen2.kv')

    def build(self):
       
        return self.root
#####################################################################


######################################################
#run the application
##using command line call
if __name__ == '__main__':
    TitanEnrolHelper().run()

#without command line in IDE
TitanEnrolHelper().run()
###################################################
