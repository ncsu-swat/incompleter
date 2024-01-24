# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56587543/trying-to-use-a-class-but-get-a-nonetype-error-with-kivy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.app import App
    _l_(685316)

except ImportError:
    pass
try:
    from kivy.uix.widget import Widget
    _l_(685318)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(685320)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
    _l_(685322)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(685324)

except ImportError:
    pass



#The different screens
class MainScreen(_n_(685325, "Screen", lambda: Screen)):
    _l_(685327)

    pass
    _l_(685326)
class SpaceGame(_n_(685328, "Screen", lambda: Screen)):
    _l_(685330)

    pass
    _l_(685329)
class Installningar(_n_(685331, "Screen", lambda: Screen)):
    _l_(685333)

    pass
    _l_(685332)
class ScreenManagement(_n_(685334, "ScreenManager", lambda: ScreenManager)):
    _l_(685336)

    pass
    _l_(685335)


# The game
class SpaceShip(_n_(685337, "Widget", lambda: Widget)):
    _l_(685339)

    pass
    _l_(685338)


class SpaceGame_TheGame(_n_(685340, "Widget", lambda: Widget)):
    _l_(685356)

    player = _c_(685342, _n_(685341, "ObjectProperty", lambda: ObjectProperty), None) #I want the ship to be an object that can get hit and stuff
    _l_(685343) #I want the ship to be an object that can get hit and stuff

    def on_touch_move(self,touch):
        _l_(685355)

        pass
        _l_(685344)
        _a_(685346, _n_(685345, "self", lambda: self), "player").center_x = _a_(685348, _n_(685347, "touch", lambda: touch), "x")
        _l_(685349)
        _a_(685351, _n_(685350, "self", lambda: self), "player").center_y = _a_(685353, _n_(685352, "touch", lambda: touch), "y")
        _l_(685354)


#Start up stuff
presentation = _c_(685359, _a_(685358, _n_(685357, "Builder", lambda: Builder), "load_file"), "space.kv") #Presentation är bara ett namn på detta som han valde
_l_(685360) #Presentation är bara ett namn på detta som han valde
class MainApp(_n_(685361, "App", lambda: App)):
    _l_(685365)

    def build(self):
        _l_(685364)

        aux = _n_(685362, "presentation", lambda: presentation)
        _l_(685363)
        return aux

if _n_(685366, "__name__", lambda: __name__) == '__main__':
    _l_(685372)

    _c_(685370, _a_(685369, _c_(685368, _n_(685367, "MainApp", lambda: MainApp)), "run"))
    _l_(685371)