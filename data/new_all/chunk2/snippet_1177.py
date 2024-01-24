# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58469331/kivy-attributeerror-with-property-defined-in-kv-file
# File name: drawingspace.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from kivy.properties import ObjectProperty
    _l_(450268)

except ImportError:
    pass
try:
    from kivy.uix.relativelayout import RelativeLayout
    _l_(450270)

except ImportError:
    pass


class DrawingSpace(_n_(450271, "RelativeLayout", lambda: RelativeLayout)):
    _l_(450280)

    def on_children(self, instance, value):
        _l_(450279)

        _a_(450273, _n_(450272, "self", lambda: self), "status_bar").counter = _c_(450277, _n_(450274, "len", lambda: len), _a_(450276, _n_(450275, "self", lambda: self), "children"))  # Here the error states that
        _l_(450278)  # Here the error states that