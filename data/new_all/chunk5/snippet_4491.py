# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56587543/trying-to-use-a-class-but-get-a-nonetype-error-with-kivy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.app import App
    _l_(671358)

except ImportError:
    pass
try:
    from kivy.uix.widget import Widget
    _l_(671360)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(671362)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
    _l_(671364)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(671366)

except ImportError:
    pass



#The different screens
class MainScreen(_n_(671367, "Screen", lambda: Screen)):
    _l_(671369)

    pass
    _l_(671368)
class SpaceGame(_n_(671370, "Screen", lambda: Screen)):
    _l_(671372)

    pass
    _l_(671371)
class Installningar(_n_(671373, "Screen", lambda: Screen)):
    _l_(671375)

    pass
    _l_(671374)
class ScreenManagement(_n_(671376, "ScreenManager", lambda: ScreenManager)):
    _l_(671378)

    pass
    _l_(671377)


# The game
class SpaceShip(_n_(671379, "Widget", lambda: Widget)):
    _l_(671381)

    pass
    _l_(671380)


class SpaceGame_TheGame(_n_(671382, "Widget", lambda: Widget)):
    _l_(671398)

    player = _c_(671384, _n_(671383, "ObjectProperty", lambda: ObjectProperty), None) #I want the ship to be an object that can get hit and stuff
    _l_(671385) #I want the ship to be an object that can get hit and stuff

    def on_touch_move(self,touch):
        _l_(671397)

        pass
        _l_(671386)
        _a_(671388, _n_(671387, "self", lambda: self), "player").center_x = _a_(671390, _n_(671389, "touch", lambda: touch), "x")
        _l_(671391)
        _a_(671393, _n_(671392, "self", lambda: self), "player").center_y = _a_(671395, _n_(671394, "touch", lambda: touch), "y")
        _l_(671396)


#Start up stuff
presentation = _c_(671401, _a_(671400, _n_(671399, "Builder", lambda: Builder), "load_file"), "space.kv") #Presentation är bara ett namn på detta som han valde
_l_(671402) #Presentation är bara ett namn på detta som han valde
class MainApp(_n_(671403, "App", lambda: App)):
    _l_(671407)

    def build(self):
        _l_(671406)

        aux = _n_(671404, "presentation", lambda: presentation)
        _l_(671405)
        return aux

if _n_(671408, "__name__", lambda: __name__) == '__main__':
    _l_(671414)

    _c_(671412, _a_(671411, _c_(671410, _n_(671409, "MainApp", lambda: MainApp)), "run"))
    _l_(671413)