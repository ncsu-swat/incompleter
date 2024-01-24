# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2600191/how-do-i-count-the-occurrences-of-a-list-item
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(1548073, _n_(1548066, "dict", lambda: dict), ((_n_(1548067, "i", lambda: i),_c_(1548071, _a_(1548069, _n_(1548068, "a", lambda: a), "count"), _n_(1548070, "i", lambda: i))) for i in _n_(1548072, "a", lambda: a)))
_l_(1548074)

def occurDict(items):
    _l_(1548089)

    d = {}
    _l_(1548075)
    for i in _n_(1548076, "items", lambda: items):
        _l_(1548088)

        if _n_(1548077, "i", lambda: i) in _n_(1548078, "d", lambda: d):
            _l_(1548087)

            _n_(1548079, "d", lambda: d)[_n_(1548080, "i", lambda: i)] = _n_(1548081, "d", lambda: d)[_n_(1548082, "i", lambda: i)]+1
            _l_(1548083)
        else:
            _n_(1548084, "d", lambda: d)[_n_(1548085, "i", lambda: i)] = 1
            _l_(1548086)
aux = _n_(1548090, "d", lambda: d)
_l_(1548091)
return aux

