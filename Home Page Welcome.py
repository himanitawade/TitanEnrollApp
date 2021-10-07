from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager,Screen

class Home(Screen):
    pass

class Enrollment(Screen):
    pass

class Department(Screen):
    pass

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file('Md.kv')

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.accent_palette = "Orange"
        return kv
    
MainApp().run()