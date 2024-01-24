#Source: https://stackoverflow.com/questions/62983706/i-get-an-attribute-error-when-i-run-this-program-im-working-with-kivy-module-i
import kivy
from kivy.app import App 
from kivy.uix.widget import Widget 
from kivy.uix.gridlayout import GridLayout 
from kivy.lang import Builder 
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager 
from kivy.uix.textinput import TextInput
from kivy.graphics import *


class Login(Widget):
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    print(name, email)

kv = Builder.load_file("test_page.kv")

class MyApp(App):
    def build(self):
        return kv 

if __name__ == '__main__':
    MyApp().run()