# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
num = [_n_(75441, "x", lambda: x) for x in _c_(75445, _a_(75444, _c_(75443, _n_(75442, "input", lambda: input)), "split"), ',')]
_l_(75446)
for p in _n_(75447, "num", lambda: num):
    _l_(75459)

    x = _c_(75450, _n_(75448, "int", lambda: int), _n_(75449, "p", lambda: p), 2)
    _l_(75451)
    if not _n_(75452, "x", lambda: x) % 5:
        _l_(75458)

        _c_(75456, _a_(75454, _n_(75453, "items", lambda: items), "append"), _n_(75455, "p", lambda: p))
        _l_(75457)
_c_(75464, _n_(75460, "print", lambda: print), _c_(75463, _a_(75461, ',', "join"), _n_(75462, "items", lambda: items)))
_l_(75465)