from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivy.lang import Builder

screen_helper = """
<Login>:
name: 'login'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press: root.manager.current = 'profile'
"""

class Login(Screen):
    pass

