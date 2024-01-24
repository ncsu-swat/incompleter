# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51381763/python-3-6-pynput-nameerror-name-keyboard-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pynput import keyboard
    _l_(426246)

except ImportError:
    pass

def on_press(key):
    _l_(426263)

    try:
        _l_(426262)

        _c_(426252, _n_(426247, "print", lambda: print), _c_(426251, _a_(426248, 'alphanumeric key {0} pressed', "format"), _a_(426250, _n_(426249, "key", lambda: key), "char")))
        _l_(426253)
    except _n_(426254, "AttributeError", lambda: AttributeError):
        _l_(426261)

        _c_(426259, _n_(426255, "print", lambda: print), _c_(426258, _a_(426256, 'special key {0} pressed', "format"), _n_(426257, "key", lambda: key)))
        _l_(426260)

def on_release(key):
    _l_(426276)

    _c_(426268, _n_(426264, "print", lambda: print), _c_(426267, _a_(426265, '{0} released', "format"), _n_(426266, "key", lambda: key)))
    _l_(426269)
    if _n_(426270, "key", lambda: key) == _a_(426273, _a_(426272, _n_(426271, "keyboard", lambda: keyboard), "Key"), "esc"):
        _l_(426275)

        aux = False
        _l_(426274)
        # Stop listener
        return aux

# Collect events until released
with _c_(426281, _a_(426278, _n_(426277, "keyboard", lambda: keyboard), "Listener"), on_press=_n_(426279, "on_press", lambda: on_press),
        on_release=_n_(426280, "on_release", lambda: on_release)) as listener:
    _l_(426286)

    _c_(426284, _a_(426283, _n_(426282, "listener", lambda: listener), "join"))
    _l_(426285)