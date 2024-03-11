#Source: https://stackoverflow.com/questions/67949407/typeerror-when-using-colorproperty-for-animation
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.properties import ColorProperty
from kivy.uix.button import Button
from kivy.app import App


class Custom(Button):
    
    def change_color(self):
        Animation(background_color=Example.fill_color).start(self)

class Example(App):
    fill_color = ColorProperty([1, 0, 0, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kv = Builder.load_string('''
<Custom>:
    background_normal: ""
    background_color: 0, 0, 1, 1
    on_release: root.change_color()
Custom:
    text: "Turn me into Red!!"
    font_size: 32
''')

    def build(self):
        return self.kv


if __name__ == "__main__":
    Example().run()