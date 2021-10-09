# Importing Kivymd

from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager

screen_helper = """
ScreenManager:
    MainPage:
    LoginPage:
    EnrolPage:

<LoginPage>:
    name: 'Login'
    MDRectangleFlatButton:
        text: 'BACK'
        pos_hint: {"down": 1}
        on_press: root.manager.current = 'MainPage'
<MainPage>:
    name: 'Main'
    MDRectangleFlatButton:
        text: 'LOGIN'
        pos_hint: {"center_x":0.5}
        on_press: root.manager.current = 'LoginPage'
"""


# creating class

class MainPage(Screen):
    pass


class LoginPage(Screen):
    pass


sm = ScreenManager()
sm.add_widget(MainPage(name='Main'))
sm.add_widget(LoginPage(name='Login'))


class loginpage(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Teal"

        return Builder.load_file('Loginpage.kv')

    def logger(self):
        # def verify(self, username, password):
        # if username == "Kavitha" and password == "kavi12":
        self.root.ids.CSU_Login.text = f'Hi {self.root.ids.user.text}!'

    # else:
    # self.root.ids.CSU_Login.text = f'Login Failed'

    def clear(self):
        pass


# run the app
loginpage().run()


