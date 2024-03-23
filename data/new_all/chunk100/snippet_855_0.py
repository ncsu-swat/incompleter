# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import collections
    _l_(84523)

except ImportError:
    pass
d = _c_(84527, _a_(84525, _n_(84524, "collections", lambda: collections), "defaultdict"), _n_(84526, "int", lambda: int))
_l_(84528)
for c in _n_(84529, "str1", lambda: str1):
    _l_(84533)

    _n_(84530, "d", lambda: d)[_n_(84531, "c", lambda: c)] += 1
    _l_(84532)
for c in _c_(84538, _n_(84534, "sorted", lambda: sorted), _n_(84535, "d", lambda: d), key=_a_(84537, _n_(84536, "d", lambda: d), "get"), reverse=True):
    _l_(84548)

    if _n_(84539, "d", lambda: d)[_n_(84540, "c", lambda: c)] > 1:
        _l_(84547)

        _c_(84545, _n_(84541, "print", lambda: print), '%s %d' % (_n_(84542, "c", lambda: c), _n_(84543, "d", lambda: d)[_n_(84544, "c", lambda: c)]))
        _l_(84546)