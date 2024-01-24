# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65094355/getting-nameerror-even-though-variable-is-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a = [2, 4]
_l_(532629)
b = [16, 32, 96]
_l_(532630)
maxOfb = _c_(532633, _n_(532631, "max", lambda: max), _n_(532632, "b", lambda: b))
_l_(532634)
factorOfb = []
_l_(532635)
for i in _c_(532640, _n_(532636, "range", lambda: range), 1, _c_(532639, _n_(532637, "int", lambda: int), _n_(532638, "maxOfb", lambda: maxOfb)/2)):
    _l_(532652)

    if _c_(532645, _n_(532641, "all", lambda: all), (_n_(532642, "j", lambda: j) % _n_(532643, "i", lambda: i) == 0 for j in _n_(532644, "b", lambda: b))):
        _l_(532651)

        _c_(532649, _a_(532647, _n_(532646, "factorOfb", lambda: factorOfb), "append"), _n_(532648, "j", lambda: j))
        _l_(532650)
_c_(532655, _n_(532653, "print", lambda: print), _n_(532654, "factorOfb", lambda: factorOfb))
_l_(532656)