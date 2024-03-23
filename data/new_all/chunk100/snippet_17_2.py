# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def position_max_min(nums):
    _l_(14270)

    max_result = _c_(14258, _n_(14253, "max", lambda: max), _c_(14256, _n_(14254, "enumerate", lambda: enumerate), _n_(14255, "nums", lambda: nums)), key=lambda x: _n_(14257, "x", lambda: x)[1])
    _l_(14259)
    min_result = _c_(14265, _n_(14260, "min", lambda: min), _c_(14263, _n_(14261, "enumerate", lambda: enumerate), _n_(14262, "nums", lambda: nums)), key=lambda x: _n_(14264, "x", lambda: x)[1])
    _l_(14266)
    aux = (_n_(14267, "max_result", lambda: max_result), _n_(14268, "min_result", lambda: min_result))
    _l_(14269)
    return aux
nums = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
_l_(14271)
_c_(14273, _n_(14272, "print", lambda: print), 'Original list:')
_l_(14274)
_c_(14277, _n_(14275, "print", lambda: print), _n_(14276, "nums", lambda: nums))
_l_(14278)
_c_(14280, _n_(14279, "print", lambda: print), '\nIndex position and value of the maximum value of the said list:')
_l_(14281)
_c_(14284, _n_(14282, "print", lambda: print), _n_(14283, "result", lambda: result)[0])
_l_(14285)
_c_(14287, _n_(14286, "print", lambda: print), '\nIndex position and value of the minimum value of the said list:')
_l_(14288)
_c_(14291, _n_(14289, "print", lambda: print), _n_(14290, "result", lambda: result)[1])
_l_(14292)