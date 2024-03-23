#Source: https://stackoverflow.com/questions/64563883/attributeerror-kivy-properties-objectproperty-object-has-no-attribute-add-wi
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import MDList,ThreeLineListItem
from kivymd.uix.button import MDFlatButton,MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.properties import ObjectProperty

class MenuScreen(Screen):
    list11=ObjectProperty(None)
    
class ProfileScreen(Screen):
    field1=ObjectProperty(None)
    field2=ObjectProperty(None)
    field3=ObjectProperty(None)
    def but1(self):
        self.but2=MDRectangleFlatButton(text='remove')
        if self.field1.text=="":
            self.box=MDDialog(title='Your Username  ',text='you need to add Title',size_hint=(0.93,0))
            self.box.open()
        else:
            MenuScreen.list1.add_widget(ThreeLineListItem(text=self.field1,secondary_text=self.field2,tertiary_text=self.field3))



sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))

class DemoApp(MDApp):
    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen



DemoApp().run()