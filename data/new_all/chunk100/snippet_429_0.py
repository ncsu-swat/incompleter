# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_none(nums):
    _l_(41971)

    result = [_n_(41965, "x", lambda: x) for x in _n_(41966, "nums", lambda: nums) if _n_(41967, "x", lambda: x) is not None]
    _l_(41968)
    aux = _n_(41969, "result", lambda: result)
    _l_(41970)
    return aux
_c_(41973, _n_(41972, "print", lambda: print), 'Original list:')
_l_(41974)
_c_(41977, _n_(41975, "print", lambda: print), _n_(41976, "nums", lambda: nums))
_l_(41978)
_c_(41980, _n_(41979, "print", lambda: print), '\nRemove None value from the said list:')
_l_(41981)
_c_(41986, _n_(41982, "print", lambda: print), _c_(41985, _n_(41983, "remove_none", lambda: remove_none), _n_(41984, "nums", lambda: nums)))
_l_(41987)