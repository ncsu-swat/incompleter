#Source: https://stackoverflow.com/questions/56535875/attributeerror-mygrid-object-has-no-attribute-for-my-function
#!/usr/bin/env python3
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

class ButtonHolder(BoxLayout):
    def colorChange1(self, *args):
        print("this function works")

Builder.load_string("""
<MyGrid>:
  rows: 3
  Label:
    canvas.before:
      Color:
        rgba: 1,0,0,1
      Rectangle:
        pos: self.pos
        size: self.size
    id: toplabel
  Label:
    canvas.before:
      Color:
        rgba:  0,1,0,1
      Rectangle:
        pos: self.pos
        size: self.size
    id: bottomlabel
  ButtonHolder:
    Button:
      effectwidget: toplabel
      on_press: root.colorChange1()
""")

class MyGrid(GridLayout):
    pass

class TheApp(App):
    def build(self):
        return MyGrid()

TheApp().run()