# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67486027/kivy-typeerror-nonetype-object-is-not-subscriptable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.app import App
    _l_(349576)

except ImportError:
    pass
try:
    from kivy.uix.widget import Widget
    _l_(349578)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(349580)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(349582)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager , Screen
    _l_(349584)

except ImportError:
    pass
try:
    from kivy.uix.image import Image
    _l_(349586)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(349588)

except ImportError:
    pass
try:
    from kivy.base import runTouchApp
    _l_(349590)

except ImportError:
    pass
try:
    from kivymd.app import MDApp
    _l_(349592)

except ImportError:
    pass
try:
    from kivy.uix.boxlayout import BoxLayout
    _l_(349594)

except ImportError:
    pass
try:
    import time
    _l_(349596)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(349598)

except ImportError:
    pass
try:
    from kivy.uix.camera import Camera
    _l_(349600)

except ImportError:
    pass

_n_(349601, "Window", lambda: Window).size = (1600, 850)
_l_(349602)



class MainPage(_n_(349603, "Screen", lambda: Screen)):
    _l_(349605)

    pass
    _l_(349604)

class AboutBtn(_n_(349606, "Screen", lambda: Screen)):
    _l_(349608)

    pass
    _l_(349607)

class WindowManager(_n_(349609, "ScreenManager", lambda: ScreenManager)):
    _l_(349611)

    pass
    _l_(349610)

class CameraClick(_n_(349612, "Screen", lambda: Screen)):
    _l_(349631)

    def capture(self):
        _l_(349630)

        camera = _a_(349614, _n_(349613, "self", lambda: self), "ids")['camera']
        _l_(349615)
        timestr = _c_(349618, _a_(349617, _n_(349616, "time", lambda: time), "strftime"), "%Y%m%d_%H%M%S")
        _l_(349619)
        _c_(349625, _a_(349621, _n_(349620, "camera", lambda: camera), "export_to_png"), _c_(349624, _a_(349622, "IMG_{}.png", "format"), _n_(349623, "timestr", lambda: timestr)))
        _l_(349626)
        _c_(349628, _n_(349627, "print", lambda: print), "Captured")
        _l_(349629)
class ResizableDraggablePicture(_n_(349632, "Screen", lambda: Screen)):
    _l_(349657)

    def on_touch_down(self, touch):
        _l_(349656)

        if _a_(349634, _n_(349633, "touch", lambda: touch), "is_mouse_scrolling"):
            _l_(349655)

            if _a_(349636, _n_(349635, "touch", lambda: touch), "button") == 'scrolldown':
                _l_(349654)

                if _a_(349638, _n_(349637, "self", lambda: self), "scale") < 10:
                    _l_(349643)

                    _n_(349639, "self", lambda: self).scale = _a_(349641, _n_(349640, "self", lambda: self), "scale") * 1.1
                    _l_(349642)
            elif _a_(349645, _n_(349644, "touch", lambda: touch), "button") == 'scrollup':
                _l_(349653)

                if _a_(349647, _n_(349646, "self", lambda: self), "scale") > 1:
                    _l_(349652)

                    _n_(349648, "self", lambda: self).scale = _a_(349650, _n_(349649, "self", lambda: self), "scale") * 0.8
                    _l_(349651)

_c_(349660, _a_(349659, _n_(349658, "Builder", lambda: Builder), "load_string"), """

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
_l_(349661)

class Shenacell(_n_(349662, "MDApp", lambda: MDApp)):
    _l_(349670)

    def build(self):
        _l_(349669)

        # self.theme_cls.theme_style = "Dark"
        _a_(349664, _n_(349663, "self", lambda: self), "theme_cls").primary_palette = "BlueGray"
        _l_(349665)
        aux = _c_(349667, _n_(349666, "WindowManager", lambda: WindowManager))
        _l_(349668)
        return aux

if _n_(349671, "__name__", lambda: __name__) == '__main__' :
    _l_(349677)

    _c_(349675, _a_(349674, _c_(349673, _n_(349672, "Shenacell", lambda: Shenacell)), "run"))
    _l_(349676)