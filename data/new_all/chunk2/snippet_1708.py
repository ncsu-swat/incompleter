# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59637293/attributeerror-float-object-has-no-attribute-texty
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import psutil
    _l_(451031)

except ImportError:
    pass
try:
    import time
    _l_(451033)

except ImportError:
    pass
try:
    import threading
    _l_(451035)

except ImportError:
    pass
try:
    from kivy.clock import Clock
    _l_(451037)

except ImportError:
    pass
try:
    from kivy.app import App
    _l_(451039)

except ImportError:
    pass
try:
    from kivy.uix.label import Label
    _l_(451041)

except ImportError:
    pass
try:
    from kivy.uix.boxlayout import BoxLayout
    _l_(451043)

except ImportError:
    pass

class ExampleApp(_n_(451044, "App", lambda: App)):
    _l_(451079)

    def build(self):
        _l_(451065)

        b = _c_(451046, _n_(451045, "BoxLayout", lambda: BoxLayout))
        _l_(451047)
        _n_(451048, "self", lambda: self).texty = _c_(451055, _n_(451049, "Label", lambda: Label), text=_c_(451054, _n_(451050, "str", lambda: str), _c_(451053, _a_(451052, _n_(451051, "psutil", lambda: psutil), "cpu_percent"))))
        _l_(451056)
        _c_(451061, _a_(451058, _n_(451057, "b", lambda: b), "add_widget"), _a_(451060, _n_(451059, "self", lambda: self), "texty"))
        _l_(451062)
        aux = _n_(451063, "b", lambda: b)
        _l_(451064)
        return aux

    def update(self):
        _l_(451074)

        _a_(451067, _n_(451066, "self", lambda: self), "texty").text = _c_(451072, _n_(451068, "str", lambda: str), _c_(451071, _a_(451070, _n_(451069, "psutil", lambda: psutil), "cpu_percent")))
        _l_(451073)

    _c_(451077, _a_(451076, _n_(451075, "Clock", lambda: Clock), "schedule_interval"), update, 1.0)
    _l_(451078)

_c_(451083, _a_(451082, _c_(451081, _n_(451080, "ExampleApp", lambda: ExampleApp)), "run"))
_l_(451084)