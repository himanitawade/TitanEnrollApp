from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from databaseconnection import getlistofcourses
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import MDScreen
from kivymd.uix.expansionpanel import MDExpansionPanel,MDExpansionPanelTwoLine
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.boxlayout import MDBoxLayout

class HomePage(MDScreen):
    pass

class SelectionPage(MDScreen):
    #make sure the d1 and p1 have values as in the database entry
    d1 = ObjectProperty(None)
    p1= ObjectProperty(None)
    def viewcoursecatalog(self):
        print('Button has pressed')
      
        
class Content(MDBoxLayout):
    pass
class CourseCatalogPage(MDScreen):
    displaycatalog=ObjectProperty(None)
    deaprtment=''
    program=''
    def on_enter(self, *args):
        # get the value of ids from screen 1 to screen2
        self.deaprtment= self.manager.get_screen('selectionpage').d1.text
        self.program = self.manager.get_screen('selectionpage').p1.text
        print(self.deaprtment)        

class PageManager(ScreenManager):
    pass

class TitanEnrolHelper(MDApp):
   
    def __init__(self,**kwargs):
        super(TitanEnrolHelper,self).__init__(**kwargs)
        self.root= Builder.load_file('pagescreen.kv')

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette= "Blue"
        self.theme_cls.accent_palette= "Orange"
        
       
        return self.root


#run the application
##using command line call
if __name__ == '__main__':
    TitanEnrolHelper().run()

#without command line in IDE
TitanEnrolHelper().run()