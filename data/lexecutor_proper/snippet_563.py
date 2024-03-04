# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/993984/what-are-the-advantages-of-numpy-over-regular-python-lists
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
x = _c_(63659, _a_(63658, _c_(63657, _a_(63653, _n_(63652, "numpy", lambda: numpy), "fromfile"), file=_c_(63655, _n_(63654, "open", lambda: open), "data"), dtype=_n_(63656, "float", lambda: float)), "reshape"), (100, 100, 100))
_l_(63660)

s = _c_(63663, _a_(63662, _n_(63661, "x", lambda: x), "sum"), axis=1)
_l_(63664)

_c_(63667, _a_(63666, (_n_(63665, "x", lambda: x) > 0.5), "nonzero"))
_l_(63668)

_n_(63669, "x", lambda: x)[:, :, ::2]
_l_(63670)

