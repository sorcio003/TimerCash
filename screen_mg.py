from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from timercash import TimerCash

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:

<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        on_press: root.manager.current = 'timer'
    Image:
        source: 'login.png'
        pos_hint: {'center_x':0.5, 'center_y':0.2}

<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Welcome Drake'
        halign: 'center'

"""

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))


class APP(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)

        return screen
    
app = APP()

app.run()