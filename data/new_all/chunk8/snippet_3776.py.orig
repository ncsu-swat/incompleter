#Source: https://stackoverflow.com/questions/68240266/kivy-event-eventdispatcher-init-is-raising-the-error-typeerror-object-i
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginScreen(Widget):
    pass

class PasswordScreen(Widget):
    pass

class PasswordApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(PasswordScreen(name='passwords'))

        return sm

if __name__ == '__main__':
    PasswordApp().run()