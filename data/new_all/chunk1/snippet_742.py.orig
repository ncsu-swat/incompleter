#Source: https://stackoverflow.com/questions/63958900/attributeerror-snackbar-object-has-no-attribute-show
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar

KV = '''
BoxLayout:
    MDRaisedButton:
        text: "click"
        on_press: app.test_bar()
'''

class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def test_bar(self):
        Snackbar(text="Hello world!").show()

TestApp().run()