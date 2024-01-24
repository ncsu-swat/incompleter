# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66071056/getting-typeerror-nonetype-object-is-not-subscriptable-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(546025)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(546027)

except ImportError:
    pass
try:
    from kivy.uix.widget import Widget
    _l_(546029)

except ImportError:
    pass
try:
    from kivy.properties import ObjectProperty
    _l_(546031)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(546033)

except ImportError:
    pass
try:
    from kivy.core.window import Window
    _l_(546035)

except ImportError:
    pass

_c_(546038, _a_(546037, _n_(546036, "Builder", lambda: Builder), "load_file"), 'float_layout.kv')
_l_(546039)

class MyLayout(_n_(546040, "Widget", lambda: Widget)):
    _l_(546042)

    pass
    _l_(546041)

class AwesomeApp(_n_(546043, "App", lambda: App)):
    _l_(546050)

    def build(self):
        _l_(546049)

        _n_(546044, "Window", lambda: Window).clearcolor = (1,1,1,1)
        _l_(546045)
        aux = _c_(546047, _n_(546046, "MyLayout", lambda: MyLayout))
        _l_(546048)
        return aux

if _n_(546051, "__name__", lambda: __name__) == '__main__':
    _l_(546057)

    _c_(546055, _a_(546054, _c_(546053, _n_(546052, "AwesomeApp", lambda: AwesomeApp)), "run"))
    _l_(546056)