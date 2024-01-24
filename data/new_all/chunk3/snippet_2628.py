# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/68341487/python-keyboard-module-error-typeerror-nonetype-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import keyboard
    _l_(578172)

except ImportError:
    pass

pressed = ""
_l_(578173)

def on_key_press():
    _l_(578203)

    _c_(578175, _n_(578174, "print", lambda: print), "Key pressed.")
    _l_(578176)
    global pressed
    _l_(578177)
    # Took me 1 hour to figure out this.
    if _c_(578184, _a_(578180, _a_(578179, _n_(578178, "charset", lambda: charset), "chars"), "__contains__"), _c_(578183, _a_(578182, _n_(578181, "keyboard", lambda: keyboard), "read_key"))):
        _l_(578198)

        _c_(578186, _n_(578185, "print", lambda: print), "processing slangs...")
        _l_(578187)
        _c_(578189, _n_(578188, "print", lambda: print), "*process*")
        _l_(578190)
    else:
        _c_(578192, _n_(578191, "print", lambda: print), "registered key.")
        _l_(578193)
        pressed += _c_(578196, _a_(578195, _n_(578194, "keyboard", lambda: keyboard), "read_key"))
        _l_(578197)
    _c_(578201, _n_(578199, "print", lambda: print), _n_(578200, "pressed", lambda: pressed))
    _l_(578202)

_c_(578208, _a_(578205, _n_(578204, "keyboard", lambda: keyboard), "on_press"), _c_(578207, _n_(578206, "on_key_press", lambda: on_key_press)))
_l_(578209)
_c_(578212, _a_(578211, _n_(578210, "keyboard", lambda: keyboard), "wait"))
_l_(578213)