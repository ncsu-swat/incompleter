# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def position_max_min(nums):
    _l_(106662)

    max_val = _c_(106639, _n_(106637, "max", lambda: max), _n_(106638, "nums", lambda: nums))
    _l_(106640)
    min_val = _c_(106643, _n_(106641, "min", lambda: min), _n_(106642, "nums", lambda: nums))
    _l_(106644)
    max_result = [_n_(106645, "i", lambda: i) for i, j in _c_(106648, _n_(106646, "enumerate", lambda: enumerate), _n_(106647, "nums", lambda: nums)) if _n_(106649, "j", lambda: j) == _n_(106650, "max_val", lambda: max_val)]
    _l_(106651)
    min_result = [_n_(106652, "i", lambda: i) for i, j in _c_(106655, _n_(106653, "enumerate", lambda: enumerate), _n_(106654, "nums", lambda: nums)) if _n_(106656, "j", lambda: j) == _n_(106657, "min_val", lambda: min_val)]
    _l_(106658)
    aux = (_n_(106659, "max_result", lambda: max_result), _n_(106660, "min_result", lambda: min_result))
    _l_(106661)
    return aux
nums = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
_l_(106663)
_c_(106665, _n_(106664, "print", lambda: print), 'Original list:')
_l_(106666)
_c_(106669, _n_(106667, "print", lambda: print), _n_(106668, "nums", lambda: nums))
_l_(106670)
_c_(106672, _n_(106671, "print", lambda: print), '\nIndex positions of the maximum value of the said list:')
_l_(106673)
_c_(106676, _n_(106674, "print", lambda: print), _n_(106675, "result", lambda: result)[0])
_l_(106677)
_c_(106679, _n_(106678, "print", lambda: print), '\nIndex positions of the minimum value of the said list:')
_l_(106680)
_c_(106683, _n_(106681, "print", lambda: print), _n_(106682, "result", lambda: result)[1])
_l_(106684)