# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/63807388/kivy-scrollview-attributeerror-nonetype-object-has-no-attribute-bind
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.properties import ObjectProperty
    _l_(429008)

except ImportError:
    pass
try:
    from kivymd.app import MDApp
    _l_(429010)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(429012)

except ImportError:
    pass
try:
    from kivy.uix.scrollview import ScrollView
    _l_(429014)

except ImportError:
    pass
try:
    from kivy.uix.floatlayout import FloatLayout
    _l_(429016)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(429018)

except ImportError:
    pass
try:
    from kivy.uix.gridlayout import GridLayout
    _l_(429020)

except ImportError:
    pass
try:
    from kivy.app import runTouchApp
    _l_(429022)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(429024)

except ImportError:
    pass

KV = """
Screen:
    Controller:
        layout_content: layout_content
        BoxLayout:
            id: bl
            orientation: 'vertical'
            padding: 10, 10
            row_default_height: '48dp'
            row_force_default: True
            spacing: 10, 10
            ScrollView:
                size: self.size
                GridLayout:
                    id: layout_content
                    size_hint_y: None
                    cols: 1
                    row_default_height: '20dp'
                    row_force_default: True
                    spacing: 0, 0
                    padding: 0, 0
                    
                    MDCard:
                        id: tel1
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "180dp", "280dp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        MDLabel: 
                            text: "Tele 1"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDSeparator:
                            height: "5dp"
                            width: "5dp"
                        MDLabel: 
                            text: "Descrizione del primo"
                    MDCard:
                        id: tel2
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "180dp", "280dp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        MDLabel: 
                            text: "Tele 2"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDSeparator:
                            height: "5dp"
                            width: "5dp"
                        MDLabel: 
                            text: "Descrizione del secondo"
                    MDCard:
                        id: tel2
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "180dp", "280dp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        MDLabel: 
                            text: "Tele 3"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]     
                        MDSeparator:
                            height: "5dp"
                            width: "5dp"
                        MDLabel: 
                            text: "Descrizione del terzo" 
                    MDCard:
                        id:tel4
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "180dp", "280dp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        MDLabel: 
                            text: "Telefilm 4"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDSeparator:
                            height: "5dp"
                            width: "5dp"
                        MDLabel: 
                            text: "Descrizione del quarto"
                    MDCard:
                        id:tel5
                        orientation: "vertical"
                        padding: "8dp"
                        size_hint: None, None
                        size: "180dp", "280dp"
                        pos_hint: {"center_x": 0.5, "center_y": 0.5}
                        MDLabel: 
                            text: "Tele 5"
                            theme_text_color: "Secondary"
                            size_hint_y: None
                            height: self.texture_size[1]
                        MDSeparator:
                            height: "5dp"
                            width: "5dp"
                        MDLabel: 
                            text: "Descrizione del quinto"                 
"""
_l_(429025)

class Controller(_n_(429026, "FloatLayout", lambda: FloatLayout)):
    _l_(429047)

    layout_content = _c_(429028, _n_(429027, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(429029)

    def __init__(self, **kwargs):
        _l_(429046)

        _c_(429035, _a_(429033, _n_(429030, "super", lambda: super)(_n_(429031, "Controller", lambda: Controller), _n_(429032, "self", lambda: self)), "__init__"), **_n_(429034, "kwargs", lambda: kwargs))
        _l_(429036)
        _c_(429044, _a_(429039, _a_(429038, _n_(429037, "self", lambda: self), "layout_content"), "bind"), minimum_height=_c_(429043, _a_(429042, _a_(429041, _n_(429040, "self", lambda: self), "layout_content"), "setter"), 'height'))
        _l_(429045)

class MainApp(_n_(429048, "MDApp", lambda: MDApp)):
    _l_(429063)

    def build(self):
        _l_(429062)

        _n_(429049, "self", lambda: self).title = "LukeFlix"
        _l_(429050)
        _a_(429052, _n_(429051, "self", lambda: self), "theme_cls").theme_style = "Light"
        _l_(429053)
        _a_(429055, _n_(429054, "self", lambda: self), "theme_cls").primary_palette = "Red"
        _l_(429056)
        aux = _c_(429060, _a_(429058, _n_(429057, "Builder", lambda: Builder), "load_string"), _n_(429059, "KV", lambda: KV))
        _l_(429061)
        return aux

_c_(429067, _a_(429066, _c_(429065, _n_(429064, "MainApp", lambda: MainApp)), "run"))
_l_(429068)