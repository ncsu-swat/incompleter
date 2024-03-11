#Source: https://stackoverflow.com/questions/76718942/attributeerror-super-object-has-no-attribute-getattr-did-you-mean
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
from kivy.core.window import Window
Window.size = (360,640)

class Main(MDApp):
    def build(self):
        screenmanager = ScreenManager()
        screenmanager.add_widget(Builder.load_file("kv/key.kv"))
        screenmanager.add_widget(Builder.load_file("kv/home.kv"))
        screenmanager.add_widget(Builder.load_file("kv/menu.kv"))
        return screenmanager
    def keylogin(self, kode_key, nohp):
        pass
    def kodee(self):
        kode_key = self.root.ids.key_login.text
        nohp = self.root.ids.nomor_hp.text
        self.keylogin(kode_key, nohp)



if __name__ == "__main__":
    Main().run()