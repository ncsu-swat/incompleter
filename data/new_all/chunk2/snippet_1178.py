# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58469331/kivy-attributeerror-with-property-defined-in-kv-file
# File name: statusbar.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import kivy
    _l_(472449)

except ImportError:
    pass
_c_(472452, _a_(472451, _n_(472450, "kivy", lambda: kivy), "require"), '1.9.0')
_l_(472453)
try:
    from kivy.uix.boxlayout import BoxLayout
    _l_(472455)

except ImportError:
    pass
try:
    from kivy.properties import NumericProperty, ObjectProperty
    _l_(472457)

except ImportError:
    pass


class StatusBar(_n_(472458, "BoxLayout", lambda: BoxLayout)):
    _l_(472488)

    counter = _c_(472460, _n_(472459, "NumericProperty", lambda: NumericProperty), 0)
    _l_(472461)
    previous_counter = 0
    _l_(472462)

    def on_counter(self, instance, value):
        _l_(472487)

        if _n_(472463, "value", lambda: value) == 0:
            _l_(472482)

            _a_(472465, _n_(472464, "self", lambda: self), "msg_label").text = "Drawing space cleared"
            _l_(472466)
        elif _n_(472467, "value", lambda: value) - 1 == _a_(472470, _a_(472469, _n_(472468, "self", lambda: self), "__class__"), "previous_counter"):
            _l_(472481)

            _a_(472472, _n_(472471, "self", lambda: self), "msg_label").text = "Widget added"
            _l_(472473)
        elif _n_(472474, "value", lambda: value) + 1 == _a_(472476, _n_(472475, "StatusBar", lambda: StatusBar), "previous_counter"):
            _l_(472480)

            _a_(472478, _n_(472477, "self", lambda: self), "msg_label").text = "Widget removed"
            _l_(472479)
        _a_(472484, _n_(472483, "self", lambda: self), "__class__").previous_counter = _n_(472485, "value", lambda: value)
        _l_(472486)