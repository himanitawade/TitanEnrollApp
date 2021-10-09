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
from kivymd.uix.menu import MDDropdownMenu



class HomePage(MDScreen):
    pass

class LoginPage(MDScreen):

    pass


class SelectionPage(MDScreen):
    #make sure the d1 and p1 have values as in the database entry
    dept=ObjectProperty(None)
    prog=ObjectProperty(None)
    
    def on_enter(self,**kargs):
        self.dept=self.manager.get_screen('page').dept
        self.prog=self.manager.get_screen('page').prog
      
        menu_items = [{
                "text": f"Computer Science",
                "viewclass":"OneLineListItem" ,
                "on_press": self.menu_callback("Computer Science"),
            }]
        
        menu_items1 = [{
                "text": f"Master",
                "viewclass":"OneLineListItem" ,
                "on_release": self.menu_callback1("text"),
            },{
                "text": f"Bachelor",
                "viewclass":"OneLineListItem" ,
                "on_release": self.menu_callback1("text"),
            }]
        self.menu = MDDropdownMenu(
            caller=self.manager.get_screen('page').dept,
            items=menu_items,
            width_mult=4,
        )
        
        self.menu1 = MDDropdownMenu(
            caller=self.manager.get_screen('page').prog,
            items=menu_items1,
            width_mult=4,
        )
        
        
    def drop(self):
        self.menu.open()
        print(self.dept.text)
        
    def drop1(self):
        self.menu1.open()
        print(self.prog.text)
    
    def menu_callback(self, text_item):
        self.dept.text = text_item 
        print(self.dept.text)
        #self.menu.dismiss()
        
    
    def menu_callback1(self, text_item):
        self.prog.text = text_item 
        print(self.prog.text)
      
        

    #d1 = ObjectProperty(None)
    #p1= ObjectProperty(None)
    def viewcoursecatalog(self):
        print('Button has pressed')
      
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
    
        self.deaprtment= self.manager.get_screen('page').d1.text
        self.program = self.manager.get_screen('page').p1.text
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

