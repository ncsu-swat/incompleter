# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def position_max_min(nums):
    _l_(14303)

    max_result = _c_(14298, _n_(14293, "max", lambda: max), _c_(14296, _n_(14294, "enumerate", lambda: enumerate), _n_(14295, "nums", lambda: nums)), key=lambda x: _n_(14297, "x", lambda: x)[1])
    _l_(14299)
    aux = (_n_(14300, "max_result", lambda: max_result), _n_(14301, "min_result", lambda: min_result))
    _l_(14302)
    return aux
nums = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
_l_(14304)
_c_(14306, _n_(14305, "print", lambda: print), 'Original list:')
_l_(14307)
_c_(14310, _n_(14308, "print", lambda: print), _n_(14309, "nums", lambda: nums))
_l_(14311)
result = _c_(14314, _n_(14312, "position_max_min", lambda: position_max_min), _n_(14313, "nums", lambda: nums))
_l_(14315)
_c_(14317, _n_(14316, "print", lambda: print), '\nIndex position and value of the maximum value of the said list:')
_l_(14318)
_c_(14321, _n_(14319, "print", lambda: print), _n_(14320, "result", lambda: result)[0])
_l_(14322)
_c_(14324, _n_(14323, "print", lambda: print), '\nIndex position and value of the minimum value of the said list:')
_l_(14325)
_c_(14328, _n_(14326, "print", lambda: print), _n_(14327, "result", lambda: result)[1])
_l_(14329)