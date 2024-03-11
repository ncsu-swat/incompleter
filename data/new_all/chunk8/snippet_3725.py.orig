#Source: https://stackoverflow.com/questions/69085989/error-attributeerror-kivy-properties-objectproperty-object-has-no-attribute
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivy.core.window import Window
Window.size = (1280, 720)


class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)

    def show_data(self, obj):
        client.send(pickle.dumps(['login', self.username.text, self.password.text]))
        MenuScreen.data = pickle.loads(client.recv(1024))
        MenuScreen.get_data()

class MenuScreen(Screen):
    data = '_'
    menuName = ObjectProperty(None)
    menuBalance = ObjectProperty(None)

    @classmethod
    def get_data(self):
        self.menuName.text = self.data[0][0]
        self.menuBalance.text = self.data[0][1]


sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(MenuScreen(name='menu'))

class DemoApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Pink'
        self.theme_cls.theme_style = 'Light'
        screen = Builder.load_string(screen_helper)
        # Clock.schedule_interval(MenuScreen.name_ret, 15)
        return screen


DemoApp().run()