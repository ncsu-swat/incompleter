#Source: https://stackoverflow.com/questions/67486027/kivy-typeerror-nonetype-object-is-not-subscriptable
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.base import runTouchApp
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
import time
from kivy.core.window import Window
from kivy.uix.camera import Camera 

Window.size = (1600, 850)



class MainPage(Screen):
    pass

class AboutBtn(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class CameraClick(Screen):
    def capture(self):
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")

     
class ResizableDraggablePicture(Screen):
    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                if self.scale < 10:
                    self.scale = self.scale * 1.1
            elif touch.button == 'scrollup':
                if self.scale > 1:
                    self.scale = self.scale * 0.8

            

Builder.load_string("""

#:import utils kivy.utils
<WindowManager>:
    MainPage:
    CameraClick:
    ResizableDraggablePicture:
    AboutBtn:
    
    
<ResizableDraggablePicture>:
    name: "resizableDraggablePicture"
    
    
<RoundedButton@Button>:
    background_color:(0,0,0,0)
    bachground_normal: ""
    canvas.before:
        Color:
            rgba:(195/255.0,231/255.0,247/255.0,1)
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [35]     


<MainPage>:
    name: "main page"

    Image:
        source: 'images/MICC.png'
        allow_stretch: True
        keep_ratio: False
        
    BoxLayout:
        cols:1
        orientation: "horizontal"
        size: root.width , root.height
        spacing: 25
        padding: 80, 900 , 1300 , 250


        RoundedButton:
            text: "about"
            color: (200,250,210)
            pos_hint : {'center_x': 0.5}
            font_size: 50
            size_hint_x: 1
            height:40
            size_hint_y: None
            width:30
            on_release: app.root.current = "aboutBtn"

#             Image:
#                 source: 'images/information.png'
#                 height:40
#                 width:40
#                 center_x: 210
#                 center_y: self.parent.center_y
                
    BoxLayout:
        cols:1
        orientation: "horizontal"
        size: root.width , root.height
        spacing: 25
        padding: 530, 900 , 900 , 260

        RoundedButton:
            text: "take a picture"
            color: (200,250,210)
            font_size: 40
            size_hint_x: 1
            height:60
            size_hint_y: None
            width:500
            on_release: app.root.current = "camera"

#             Image:
#                 source: 'images/takePic.png'
#                 height:40
#                 width:40
#                 center_x: 500
#                 center_y: self.parent.center_y


    BoxLayout:
        cols:1
        orientation: "horizontal"
        size: root.width , root.height
        spacing: 25
        padding: 1200, 600, 50 , 220
#         
#         RoundedButton:
#             text: "Setting"
#             font_size: 50
#             size_hint_x: 1
#             height:60
#             size_hint_y: None
#             width:500
#             # on_release: app.root.current = "SettingBtn"

            Image:
                source: 'images/settings.png'
                height:40
                width:40
                center_x: 830
                center_y: self.parent.center_y
                
<AboutBtn>:
    name: "aboutBtn"

    Image:
        source: 'images/aboutBtn.png'
        allow_stretch: True
        keep_ratio: False    
            
            
    BoxLayout:
        orientation: 'vertical'
        padding: 90 , 800 , 1400 , 750
        spacing: 5   

        ToggleButton:
            text: 'HOME'
            on_release: app.root.current = "main page"
            size_hint_y: None
            height: '48dp'            
                
                
                
                
<CameraClick>:

    name: "camera"
    orientation: 'vertical'    
 
    Image:
        source: 'images/bck-g.png'
        allow_stretch: True
        keep_ratio: False

            

            
            
    Camera:
        id: camera
        play: True
        allow_stretch: True
    
    
    BoxLayout:
        orientation: 'vertical'
        padding: 50 , 50 , 50 , 50
        spacing: 5   

        ToggleButton:
            text: 'Play'
            on_press: camera.play = not camera.play
            size_hint_y: None
            height: '48dp'
        Button:
            text: 'Capture'
            size_hint_y: None
            height: '48dp'
            on_press: root.capture()
            
            
    BoxLayout:
        orientation: 'vertical'
        padding: 50 , 10 , 800 , 600
    

        ToggleButton:
            text: 'ZOOM'
            size_hint_y: None
            size_hint_x: None
            height: '48dp'
            pos:200,200
            font_size:12
            width: 100
            height: 50
            on_release: app.root.current = "resizableDraggablePicture"
            
            
            
    BoxLayout:
        orientation: 'vertical'
        padding: 50 , 10 , 800 , 700
    

        ToggleButton:
            text: 'HOME'
            size_hint_y: None
            size_hint_x: None
            height: '48dp'
            pos:200,200
            font_size:12
            width: 100
            height: 50
            on_release: app.root.current = "main page"               

""")

class Shenacell(MDApp):
    def build(self):
        # self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return WindowManager()

if __name__ == '__main__' :
    Shenacell().run()
    