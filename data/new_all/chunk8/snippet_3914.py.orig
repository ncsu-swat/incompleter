#Source: https://stackoverflow.com/questions/65372742/python-kivy-attributeerror-nonetype-object-has-no-attribute-text
# main.py
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.list import MDList,OneLineListItem
from kivy.uix.scrollview import ScrollView
from exel import DataBase

class TOPRIGHTINVOICE(Screen):
    invoice = ObjectProperty(None)
    For = ObjectProperty(None)

    def next(self):
        db.add_loadinfo(self.invoice.text, self.For.text)

        self.reset()
        sm.current = "CARRIERPAGE"
    
    def reset(self):
        self.invoice.text = "" 
        self.For.text = ""

    def login(self):
        self.reset()
        sm.current = "CARRIERPAGE"


class CARRIERPAGE(Screen):

    def build(self):
        screen = Screen()

        scroll = ScrollView()
        list_view= MDList()
        scroll.add_widget(list_view)

        item1 = OneLineListItem(text='Coyote')
        item2 = OneLineListItem(text='TQL')

        list_view.add_widget(item1)
        list_view.add_widget(item2)

        screen.add_widget(list_view)
     


def MissingInfo():
    pop = Popup(title= 'Missing Information',
                content=Label(text='You are missing information, are you sure you want to continue?'),
                suze_hint=(None,None), size=(400,400))
    pop.open()

class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("user.txt")

screens = [TOPRIGHTINVOICE(name="main"), CARRIERPAGE(name="CARRIERPAGE")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "main"

class MyScreen(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MyScreen().run()