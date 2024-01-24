# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62918598/how-to-solve-attributeerror-in-kivy-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.app import App
    _l_(538671)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(538673)

except ImportError:
    pass

kv = _c_(538676, _a_(538675, _n_(538674, "Builder", lambda: Builder), "load_string"), "login.kv")
_l_(538677)


class MyMainApp(_n_(538678, "App", lambda: App)):
    _l_(538682)

    def build(self):
        _l_(538681)

        aux = _n_(538679, "kv", lambda: kv)
        _l_(538680)
        return aux


if _n_(538683, "__name__", lambda: __name__) == '__main__':
    _l_(538689)

    _c_(538687, _a_(538686, _c_(538685, _n_(538684, "MyMainApp", lambda: MyMainApp)), "run"))
    _l_(538688)