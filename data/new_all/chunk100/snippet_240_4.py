# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def position_max_min(nums):
    _l_(19250)

    max_val = _c_(19231, _n_(19229, "max", lambda: max), _n_(19230, "nums", lambda: nums))
    _l_(19232)
    max_result = [_n_(19233, "i", lambda: i) for (i, j) in _c_(19236, _n_(19234, "enumerate", lambda: enumerate), _n_(19235, "nums", lambda: nums)) if _n_(19237, "j", lambda: j) == _n_(19238, "max_val", lambda: max_val)]
    _l_(19239)
    min_result = [_n_(19240, "i", lambda: i) for (i, j) in _c_(19243, _n_(19241, "enumerate", lambda: enumerate), _n_(19242, "nums", lambda: nums)) if _n_(19244, "j", lambda: j) == _n_(19245, "min_val", lambda: min_val)]
    _l_(19246)
    aux = (_n_(19247, "max_result", lambda: max_result), _n_(19248, "min_result", lambda: min_result))
    _l_(19249)
    return aux
nums = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
_l_(19251)
_c_(19253, _n_(19252, "print", lambda: print), 'Original list:')
_l_(19254)
_c_(19257, _n_(19255, "print", lambda: print), _n_(19256, "nums", lambda: nums))
_l_(19258)
result = _c_(19261, _n_(19259, "position_max_min", lambda: position_max_min), _n_(19260, "nums", lambda: nums))
_l_(19262)
_c_(19264, _n_(19263, "print", lambda: print), '\nIndex positions of the maximum value of the said list:')
_l_(19265)
_c_(19268, _n_(19266, "print", lambda: print), _n_(19267, "result", lambda: result)[0])
_l_(19269)
_c_(19271, _n_(19270, "print", lambda: print), '\nIndex positions of the minimum value of the said list:')
_l_(19272)
_c_(19275, _n_(19273, "print", lambda: print), _n_(19274, "result", lambda: result)[1])
_l_(19276)