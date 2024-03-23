# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
_l_(69959)
dup_items = _c_(69961, _n_(69960, "set", lambda: set))
_l_(69962)
for x in _n_(69963, "a", lambda: a):
    _l_(69977)

    if _n_(69964, "x", lambda: x) not in _n_(69965, "dup_items", lambda: dup_items):
        _l_(69976)

        _c_(69969, _a_(69967, _n_(69966, "uniq_items", lambda: uniq_items), "append"), _n_(69968, "x", lambda: x))
        _l_(69970)
        _c_(69974, _a_(69972, _n_(69971, "dup_items", lambda: dup_items), "add"), _n_(69973, "x", lambda: x))
        _l_(69975)
_c_(69980, _n_(69978, "print", lambda: print), _n_(69979, "dup_items", lambda: dup_items))
_l_(69981)