# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
items = []
_l_(75421)
for p in _n_(75422, "num", lambda: num):
    _l_(75434)

    x = _c_(75425, _n_(75423, "int", lambda: int), _n_(75424, "p", lambda: p), 2)
    _l_(75426)
    if not _n_(75427, "x", lambda: x) % 5:
        _l_(75433)

        _c_(75431, _a_(75429, _n_(75428, "items", lambda: items), "append"), _n_(75430, "p", lambda: p))
        _l_(75432)
_c_(75439, _n_(75435, "print", lambda: print), _c_(75438, _a_(75436, ',', "join"), _n_(75437, "items", lambda: items)))
_l_(75440)