#Source: https://stackoverflow.com/questions/68688113/python-kivymd-typeerror-init-takes-1-positional-argument-but-2-were-given
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import *

KV = '''
ScrollView:

    MDList:
        id: list
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):

        ib = IconLeftWidget(icon='github')
        ibn = OneLineAvatarIconListItem(
            IconLeftWidget(icon='github')
            )
        
        self.root.ids.list.add_widget(ib)

MainApp().run()