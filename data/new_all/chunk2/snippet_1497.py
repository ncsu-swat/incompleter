# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50412552/kivy-callback-custom-widget-call-from-ids-raise-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.app import App
    _l_(459436)

except ImportError:
    pass
try:
    from kivy.uix.tabbedpanel import TabbedPanel
    _l_(459438)

except ImportError:
    pass
try:
    from kivy.uix.boxlayout import BoxLayout
    _l_(459440)

except ImportError:
    pass
try:
    from kivy.lang import Builder
    _l_(459442)

except ImportError:
    pass

_c_(459445, _a_(459444, _n_(459443, "Builder", lambda: Builder), "load_file"), "panel.kv")
_l_(459446)

class LabelBox(_n_(459447, "BoxLayout", lambda: BoxLayout)):
    _l_(459463)

    def __init__(self, *args, **kwargs):
        _l_(459456)

        _c_(459454, _a_(459451, _n_(459448, "super", lambda: super)(_n_(459449, "LabelBox", lambda: LabelBox), _n_(459450, "self", lambda: self)), "__init__"), *_n_(459452, "args", lambda: args), **_n_(459453, "kwargs", lambda: kwargs))
        _l_(459455)

    def change_first_text(self, text):
        _l_(459462)

        _a_(459459, _a_(459458, _n_(459457, "self", lambda: self), "ids"), "first").text = _n_(459460, "text", lambda: text)
        _l_(459461)

class ButtonList(_n_(459464, "BoxLayout", lambda: BoxLayout)):
    _l_(459466)

    pass
    _l_(459465)

class Test(_n_(459467, "TabbedPanel", lambda: TabbedPanel)):
    _l_(459469)

    pass
    _l_(459468)


class TabbedPanelApp(_n_(459470, "App", lambda: App)):
    _l_(459516)

    def build(self):
        _l_(459500)

        _n_(459471, "self", lambda: self).test = _c_(459473, _n_(459472, "Test", lambda: Test))
        _l_(459474)
        _n_(459475, "self", lambda: self).btn_list = _c_(459477, _n_(459476, "ButtonList", lambda: ButtonList))
        _l_(459478)
        _n_(459479, "self", lambda: self).vbox = _c_(459481, _n_(459480, "BoxLayout", lambda: BoxLayout), orientation="vertical")
        _l_(459482)
        _c_(459488, _a_(459485, _a_(459484, _n_(459483, "self", lambda: self), "vbox"), "add_widget"), _a_(459487, _n_(459486, "self", lambda: self), "btn_list"))
        _l_(459489)
        _c_(459495, _a_(459492, _a_(459491, _n_(459490, "self", lambda: self), "vbox"), "add_widget"), _a_(459494, _n_(459493, "self", lambda: self), "test"))
        _l_(459496)
        aux = _a_(459498, _n_(459497, "self", lambda: self), "vbox")
        _l_(459499)
        return aux

    def change_first(self, value):
        _l_(459515)

        _c_(459505, _n_(459501, "print", lambda: print), _c_(459504, _a_(459502, "Button clicked and new value is: '{}'", "format"), _n_(459503, "value", lambda: value)))
        _l_(459506)
        _c_(459513, _a_(459511, _a_(459510, _a_(459509, _a_(459508, _n_(459507, "self", lambda: self), "test"), "ids"), "lbs"), "change_first_text"), _n_(459512, "value", lambda: value))
        _l_(459514)


if _n_(459517, "__name__", lambda: __name__) == '__main__':
    _l_(459523)

    _c_(459521, _a_(459520, _c_(459519, _n_(459518, "TabbedPanelApp", lambda: TabbedPanelApp)), "run"))
    _l_(459522)