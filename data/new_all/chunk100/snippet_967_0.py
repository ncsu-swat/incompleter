# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def list_count_4(nums):
    _l_(97193)

    for num in _n_(97185, "nums", lambda: nums):
        _l_(97190)

        if _n_(97186, "num", lambda: num) == 4:
            _l_(97189)

            count = _n_(97187, "count", lambda: count) + 1
            _l_(97188)
    aux = _n_(97191, "count", lambda: count)
    _l_(97192)
    return aux
_c_(97197, _n_(97194, "print", lambda: print), _c_(97196, _n_(97195, "list_count_4", lambda: list_count_4), [1, 4, 6, 7, 4]))
_l_(97198)
_c_(97202, _n_(97199, "print", lambda: print), _c_(97201, _n_(97200, "list_count_4", lambda: list_count_4), [1, 4, 6, 4, 7, 4]))
_l_(97203)