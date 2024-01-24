# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76171186/i-cant-add-a-widget-in-a-kivy-app-from-python3-class-error-message-attributee
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.app import App
    _l_(426922)

except ImportError:
    pass
try:
    from kivy.lang.builder import Builder
    _l_(426924)

except ImportError:
    pass
try:
    from kivy.uix.gridlayout import GridLayout
    _l_(426926)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(426928)

except ImportError:
    pass
class Grid(_n_(426929, "GridLayout", lambda: GridLayout)):
    _l_(426940)

    cols=2
    _l_(426930)
    def doet(self):
        _l_(426939)

        _c_(426937, _a_(426934, _a_(426933, _a_(426932, _n_(426931, "self", lambda: self), "ids"), "grid_id"), "add_widget"), _c_(426936, _n_(426935, "Button", lambda: Button)))
        _l_(426938)
class app(_n_(426941, "App", lambda: App)):
    _l_(426951)

    def build(self):
        _l_(426950)

        _n_(426942, "self", lambda: self).grid=_c_(426944, _n_(426943, "Grid", lambda: Grid))
        _l_(426945)
        aux = _c_(426948, _a_(426947, _n_(426946, "Builder", lambda: Builder), "load_file"), 'lab.kv')
        _l_(426949)
        return aux
_c_(426955, _a_(426954, _c_(426953, _n_(426952, "app", lambda: app)), "run"))
_l_(426956)