# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/30903813/cant-set-parent-using-gtk-in-python-typeerror-argument-parent-expected-gtk-wi
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Windows(_a_(426895, _n_(426894, "Gtk", lambda: Gtk), "Window")):
    _l_(426914)

    def About(self):
        _l_(426913)

        about = _c_(426898, _a_(426897, _n_(426896, "Gtk", lambda: Gtk), "Window"), title="About")
        _l_(426899)
        _c_(426902, _a_(426901, _n_(426900, "about", lambda: about), "set_border_width"), 10)
        _l_(426903)
        _c_(426906, _a_(426905, _n_(426904, "about", lambda: about), "set_resizable"), False)
        _l_(426907)
        _c_(426911, _a_(426909, _n_(426908, "about", lambda: about), "set_transient_for"), _n_(426910, "__init__", lambda: __init__))
        _l_(426912)