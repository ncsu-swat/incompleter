# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62983706/i-get-an-attribute-error-when-i-run-this-program-im-working-with-kivy-module-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(589366)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(589368)

except ImportError:
    pass
try:
    from kivy.uix.widget import Widget
    _l_(589370)

except ImportError:
    pass
try:
    from kivy.uix.gridlayout import GridLayout
    _l_(589372)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(589374)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(589376)

except ImportError:
    pass
try:
    from kivy.uix.screenmanager import Screen, ScreenManager
    _l_(589378)

except ImportError:
    pass
try:
    from kivy.uix.textinput import TextInput
    _l_(589380)

except ImportError:
    pass
try:
    from kivy.graphics import *
    _l_(589382)

except ImportError:
    pass


class Login(_n_(589383, "Widget", lambda: Widget)):
    _l_(589393)

    name = _c_(589385, _n_(589384, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(589386)
    email = _c_(589388, _n_(589387, "ObjectProperty", lambda: ObjectProperty), None)
    _l_(589389)
    _c_(589391, _n_(589390, "print", lambda: print), name, email)
    _l_(589392)

kv = _c_(589396, _a_(589395, _n_(589394, "Builder", lambda: Builder), "load_file"), "test_page.kv")
_l_(589397)

class MyApp(_n_(589398, "App", lambda: App)):
    _l_(589402)

    def build(self):
        _l_(589401)

        aux = _n_(589399, "kv", lambda: kv) 
        _l_(589400) 
        return aux 

if _n_(589403, "__name__", lambda: __name__) == '__main__':
    _l_(589409)

    _c_(589407, _a_(589406, _c_(589405, _n_(589404, "MyApp", lambda: MyApp)), "run"))
    _l_(589408)