# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
_l_(69915)
uniq_items = []
_l_(69916)
for x in _n_(69917, "a", lambda: a):
    _l_(69931)

    if _n_(69918, "x", lambda: x) not in _n_(69919, "dup_items", lambda: dup_items):
        _l_(69930)

        _c_(69923, _a_(69921, _n_(69920, "uniq_items", lambda: uniq_items), "append"), _n_(69922, "x", lambda: x))
        _l_(69924)
        _c_(69928, _a_(69926, _n_(69925, "dup_items", lambda: dup_items), "add"), _n_(69927, "x", lambda: x))
        _l_(69929)
_c_(69934, _n_(69932, "print", lambda: print), _n_(69933, "dup_items", lambda: dup_items))
_l_(69935)