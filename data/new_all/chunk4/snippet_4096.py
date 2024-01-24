# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62983706/i-get-an-attribute-error-when-i-run-this-program-im-working-with-kivy-module-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(581214)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(581216)

except ImportError:
    pass
try:
    from kivy.uix.widget import Widget
    _l_(581218)

except ImportError:
    pass
try:
    from kivy.uix.gridlayout import GridLayout
    _l_(581220)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(581222)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(581224)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import Screen, ScreenManager
    _l_(581226)

except ImportError:
    pass
try:
    from kivy.uix.textinput import TextInput
    _l_(581228)

except ImportError:
    pass
try:
    from kivy.graphics import *
    _l_(581230)

except ImportError:
    pass


class Login(_n_(581231, "Widget", lambda: Widget)):
    _l_(581241)

    name = _c_(581233, _n_(581232, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(581234)
    email = _c_(581236, _n_(581235, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(581237)
    _c_(581239, _n_(581238, "print", lambda: print), name, email)
    _l_(581240)

kv = _c_(581244, _a_(581243, _n_(581242, "Builder", lambda: Builder), "load_file"), "test_page.kv")
_l_(581245)

class MyApp(_n_(581246, "App", lambda: App)):
    _l_(581250)

    def build(self):
        _l_(581249)

        aux = _n_(581247, "kv", lambda: kv) 
        _l_(581248) 
        return aux 

if _n_(581251, "__name__", lambda: __name__) == '__main__':
    _l_(581257)

    _c_(581255, _a_(581254, _c_(581253, _n_(581252, "MyApp", lambda: MyApp)), "run"))
    _l_(581256)