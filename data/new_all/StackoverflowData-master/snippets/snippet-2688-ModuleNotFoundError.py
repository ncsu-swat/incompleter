#Source: https://stackoverflow.com/questions/66800565/attributeerror-screen-object-has-no-attribute-text-in-python-kivymd
from kivy.lang import Builder
from kivymd.uix.screen import Screen
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.chip import MDChip
from kivymd.uix.floatlayout import FloatLayout

button = '''
Screen:
    MDRaisedButton:
        id: button_id
        text: "PRESS ME"
        pos_hint: {"center_x": .35, "center_y": .8}
        on_release: app.drop.open()
'''

button1 = '''
Screen:
    MDRaisedButton:
        id: button1_id
        text: "PRESS ME 2"
        pos_hint: {"center_x": .5, "center_y": .8}
        on_release: app.clear()
'''

list1 = (['Item 1','Item 2','Item 3'], ['Item 4', 'Item 5', 'Item 6'])
class Test(MDApp):
    def build(self):
        self.screen = Screen()
        self.btn = Builder.load_string(button)
        self.btn1 = Builder.load_string(button1)

        self.screen.add_widget(self.btn1)
        self.screen.add_widget(self.btn)


        self.drop = MDDropdownMenu(
            caller = self.btn.ids.button_id,
            items = [{'text':'Show Chips'}],
            width_mult = 4,
        )
        self.drop.bind(on_release=self.testing)

        return self.screen
    
    def testing(self, menu, menu_item):
        objects = {0.2 : "Item 1", 0.5 : "Item 2", 0.8 : "Item 3"}
        for pos, item in objects.items():
            self.chip = MDChip(
                text = item,
                check = True,
                pos_hint = {"center_x":pos, "center_y":0.4},
                
            )
            self.screen.add_widget(self.chip)

    def clear(self):
        for child in self.root.children[:]:
            if child.text in list1[0]:
                self.root.remove_widget(child)

Test().run()