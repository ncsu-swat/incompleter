# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_none(nums):
    _l_(115921)

    result = [_n_(115915, "x", lambda: x) for x in _n_(115916, "nums", lambda: nums) if _n_(115917, "x", lambda: x) is not None]
    _l_(115918)
    aux = _n_(115919, "result", lambda: result)
    _l_(115920)
    return aux
_c_(115923, _n_(115922, "print", lambda: print), 'Original list:')
_l_(115924)
_c_(115927, _n_(115925, "print", lambda: print), _n_(115926, "nums", lambda: nums))
_l_(115928)
_c_(115930, _n_(115929, "print", lambda: print), '\nRemove None value from the said list:')
_l_(115931)
_c_(115936, _n_(115932, "print", lambda: print), _c_(115935, _n_(115933, "remove_none", lambda: remove_none), _n_(115934, "nums", lambda: nums)))
_l_(115937)