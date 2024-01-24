# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61684725/getting-typeerror-object-init-takes-no-parameters-kivy
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.uix.floatlayout import FloatLayout
    _l_(558435)

except ImportError:
    pass
try:
    from kivy.uix.gridlayout import GridLayout
    _l_(558437)

except ImportError:
    pass
try:
    from kivy.uix.button import Button
    _l_(558439)

except ImportError:
    pass
try:
    from kivy.uix.label import Label
    _l_(558441)

except ImportError:
    pass

class ClinicBanner(_n_(558442, "GridLayout", lambda: GridLayout)):
    _l_(558469)

    rows = 1
    _l_(558443)

    def __init__(self, **kwargs):
        _l_(558468)

        _c_(558449, _a_(558447, _n_(558444, "super", lambda: super)(_n_(558445, "ClinicBanner", lambda: ClinicBanner), _n_(558446, "self", lambda: self)), "__init__"), **_n_(558448, "kwargs", lambda: kwargs))
        _l_(558450)

        centre = _c_(558452, _n_(558451, "FloatLayout", lambda: FloatLayout))
        _l_(558453)
        centre_label = _c_(558456, _n_(558454, "Label", lambda: Label), text=_n_(558455, "kwargs", lambda: kwargs)['cities'], size_hint=(1, .2), pos_hint={"top": .2,  "left": 1})
        _l_(558457)
        _c_(558461, _a_(558459, _n_(558458, "centre", lambda: centre), "add_widget"), _n_(558460, "centre_label", lambda: centre_label))
        _l_(558462)

        _c_(558466, _a_(558464, _n_(558463, "self", lambda: self), "add_widget"), _n_(558465, "centre", lambda: centre))
        _l_(558467)