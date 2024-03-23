#Source: https://stackoverflow.com/questions/62942634/attributeerror-nonetype-object-has-no-attribute-ids-in-kivy-when-clock-sche
import kivy
from kivy.app import App
from kivy.lang import Builder

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.config import Config

# You can create your kv code in the Python file

# Create a class for all screens in which you can include
# helpful methods specific to that screen
kv = Builder.load_file("main.kv")

class MainWindow(Screen):
    cloud_texture = ObjectProperty(None)
    floor_texture = ObjectProperty(None)
    sound = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cloud_texture = Image(source = "cloud4.png").texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (Window.width/self.cloud_texture.width,-1)
        self.floor_texture = Image(source = "floor2.jpg").texture
        self.floor_texture.wrap = 'repeat'
        self.floor_texture.uvsize = (Window.width/self.floor_texture.width,-1)
        self.sun_texture = Image(source = "sun.png").texture
        self.sun_texture.uvsize = (Window.width/self.sun_texture.width,-1)
        self.sound = SoundLoader.load('8bitmenu.wav')
        self.sound.play()

    def scroll_textures(self, time_passed):
        #Update the uvpos
        self.cloud_texture.uvpos = ((self.cloud_texture.uvpos[0] - time_passed/20) % Window.width, self.cloud_texture.uvpos[1])
        self.floor_texture.uvpos = ((self.floor_texture.uvpos[0] + time_passed/8) % Window.width, self.floor_texture.uvpos[1])
        #Redraw textures
        texture = self.property('cloud_texture')
        texture.dispatch(self)

        texture = self.property('floor_texture')
        texture.dispatch(self)

class Window1(Screen):
    pass

class WindowManager(ScreenManager):
    pass


#Config.write()
class MyApp(App):
    def on_start(self):
        Clock.schedule_interval(self.root.ids.mainwindow.scroll_textures, 1/60.)
        pass
    def build(self):
        return kv


MyApp().run()