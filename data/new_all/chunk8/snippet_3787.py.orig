#Source: https://stackoverflow.com/questions/68046076/sm-current-does-not-switch-screen-and-gives-me-attribute-error-str-object-ha
from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.properties import ObjectProperty

Window.size = (350, 580)


class Welcome(Screen):
    emailInput = ObjectProperty(None)
    passwordInput = ObjectProperty(None)

    def validatelogin(self):
        if self.emailInput.text == "123" and self.passwordInput.text == "123":
            print("????", self.manager)
            self.manager.current = 'selection'


class SelectionOption(Screen):
    pass


class windowManager(ScreenManager):
    pass


class Console(MDApp):

    def build(self):
        return Builder.load_file('../Files/ScreenManager.kv')


if __name__ == '__main__':
    Console().run()