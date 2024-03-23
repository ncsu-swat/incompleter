# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_none(nums):
    _l_(73625)

    result = _c_(73619, _n_(73616, "filter", lambda: filter), lambda v: _n_(73617, "v", lambda: v) is not None, _n_(73618, "nums", lambda: nums))
    _l_(73620)
    aux = _c_(73623, _n_(73621, "list", lambda: list), _n_(73622, "result", lambda: result))
    _l_(73624)
    return aux
_c_(73627, _n_(73626, "print", lambda: print), 'Original list:')
_l_(73628)
_c_(73631, _n_(73629, "print", lambda: print), _n_(73630, "nums", lambda: nums))
_l_(73632)
_c_(73634, _n_(73633, "print", lambda: print), '\nRemove None value from the said list:')
_l_(73635)
_c_(73640, _n_(73636, "print", lambda: print), _c_(73639, _n_(73637, "remove_none", lambda: remove_none), _n_(73638, "nums", lambda: nums)))
_l_(73641)