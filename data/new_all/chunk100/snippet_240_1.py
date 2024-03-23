# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def position_max_min(nums):
    _l_(19109)

    max_val = _c_(19093, _n_(19091, "max", lambda: max), _n_(19092, "nums", lambda: nums))
    _l_(19094)
    min_val = _c_(19097, _n_(19095, "min", lambda: min), _n_(19096, "nums", lambda: nums))
    _l_(19098)
    min_result = [_n_(19099, "i", lambda: i) for (i, j) in _c_(19102, _n_(19100, "enumerate", lambda: enumerate), _n_(19101, "nums", lambda: nums)) if _n_(19103, "j", lambda: j) == _n_(19104, "min_val", lambda: min_val)]
    _l_(19105)
    aux = (_n_(19106, "max_result", lambda: max_result), _n_(19107, "min_result", lambda: min_result))
    _l_(19108)
    return aux
nums = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
_l_(19110)
_c_(19112, _n_(19111, "print", lambda: print), 'Original list:')
_l_(19113)
_c_(19116, _n_(19114, "print", lambda: print), _n_(19115, "nums", lambda: nums))
_l_(19117)
result = _c_(19120, _n_(19118, "position_max_min", lambda: position_max_min), _n_(19119, "nums", lambda: nums))
_l_(19121)
_c_(19123, _n_(19122, "print", lambda: print), '\nIndex positions of the maximum value of the said list:')
_l_(19124)
_c_(19127, _n_(19125, "print", lambda: print), _n_(19126, "result", lambda: result)[0])
_l_(19128)
_c_(19130, _n_(19129, "print", lambda: print), '\nIndex positions of the minimum value of the said list:')
_l_(19131)
_c_(19134, _n_(19132, "print", lambda: print), _n_(19133, "result", lambda: result)[1])
_l_(19135)