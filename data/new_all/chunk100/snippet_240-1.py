# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def position_max_min(nums):
    _l_(106710)

    max_val = _c_(106687, _n_(106685, "max", lambda: max), _n_(106686, "nums", lambda: nums))
    _l_(106688)
    min_val = _c_(106691, _n_(106689, "min", lambda: min), _n_(106690, "nums", lambda: nums))
    _l_(106692)
    max_result = [_n_(106693, "i", lambda: i) for i, j in _c_(106696, _n_(106694, "enumerate", lambda: enumerate), _n_(106695, "nums", lambda: nums)) if _n_(106697, "j", lambda: j) == _n_(106698, "max_val", lambda: max_val)]
    _l_(106699)
    min_result = [_n_(106700, "i", lambda: i) for i, j in _c_(106703, _n_(106701, "enumerate", lambda: enumerate), _n_(106702, "nums", lambda: nums)) if _n_(106704, "j", lambda: j) == _n_(106705, "min_val", lambda: min_val)]
    _l_(106706)
    aux = (_n_(106707, "max_result", lambda: max_result), _n_(106708, "min_result", lambda: min_result))
    _l_(106709)
    return aux
_c_(106712, _n_(106711, "print", lambda: print), 'Original list:')
_l_(106713)
_c_(106716, _n_(106714, "print", lambda: print), _n_(106715, "nums", lambda: nums))
_l_(106717)
result = _c_(106720, _n_(106718, "position_max_min", lambda: position_max_min), _n_(106719, "nums", lambda: nums))
_l_(106721)
_c_(106723, _n_(106722, "print", lambda: print), '\nIndex positions of the maximum value of the said list:')
_l_(106724)
_c_(106727, _n_(106725, "print", lambda: print), _n_(106726, "result", lambda: result)[0])
_l_(106728)
_c_(106730, _n_(106729, "print", lambda: print), '\nIndex positions of the minimum value of the said list:')
_l_(106731)
_c_(106734, _n_(106732, "print", lambda: print), _n_(106733, "result", lambda: result)[1])
_l_(106735)