# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def position_max_min(nums):
    _l_(19068)

    max_val = _c_(19045, _n_(19043, "max", lambda: max), _n_(19044, "nums", lambda: nums))
    _l_(19046)
    min_val = _c_(19049, _n_(19047, "min", lambda: min), _n_(19048, "nums", lambda: nums))
    _l_(19050)
    max_result = [_n_(19051, "i", lambda: i) for (i, j) in _c_(19054, _n_(19052, "enumerate", lambda: enumerate), _n_(19053, "nums", lambda: nums)) if _n_(19055, "j", lambda: j) == _n_(19056, "max_val", lambda: max_val)]
    _l_(19057)
    min_result = [_n_(19058, "i", lambda: i) for (i, j) in _c_(19061, _n_(19059, "enumerate", lambda: enumerate), _n_(19060, "nums", lambda: nums)) if _n_(19062, "j", lambda: j) == _n_(19063, "min_val", lambda: min_val)]
    _l_(19064)
    aux = (_n_(19065, "max_result", lambda: max_result), _n_(19066, "min_result", lambda: min_result))
    _l_(19067)
    return aux
nums = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
_l_(19069)
_c_(19071, _n_(19070, "print", lambda: print), 'Original list:')
_l_(19072)
_c_(19075, _n_(19073, "print", lambda: print), _n_(19074, "nums", lambda: nums))
_l_(19076)
_c_(19078, _n_(19077, "print", lambda: print), '\nIndex positions of the maximum value of the said list:')
_l_(19079)
_c_(19082, _n_(19080, "print", lambda: print), _n_(19081, "result", lambda: result)[0])
_l_(19083)
_c_(19085, _n_(19084, "print", lambda: print), '\nIndex positions of the minimum value of the said list:')
_l_(19086)
_c_(19089, _n_(19087, "print", lambda: print), _n_(19088, "result", lambda: result)[1])
_l_(19090)