# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66775462/error-typeerror-a-bytes-like-object-is-required-not-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import struct
    _l_(397599)

except ImportError:
    pass
oldfile = _c_(397601, _n_(397600, "open", lambda: open), "buscrash_diversion.uexp", "rb")
_l_(397602)
l = _c_(397607, _n_(397603, "list", lambda: list), _c_(397606, _a_(397605, _n_(397604, "oldfile", lambda: oldfile), "read")))
_l_(397608)
out = _c_(397610, _n_(397609, "open", lambda: open), "1", "wb")
_l_(397611)
for i in _n_(397612, "l", lambda: l):
    _l_(397621)

    _c_(397619, _a_(397614, _n_(397613, "out", lambda: out), "write"), _c_(397618, _a_(397616, _n_(397615, "struct", lambda: struct), "pack"), "b", _n_(397617, "i", lambda: i)))
    _l_(397620)