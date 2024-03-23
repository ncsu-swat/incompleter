# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def position_max_min(nums):
    _l_(19157)

    min_val = _c_(19138, _n_(19136, "min", lambda: min), _n_(19137, "nums", lambda: nums))
    _l_(19139)
    max_result = [_n_(19140, "i", lambda: i) for (i, j) in _c_(19143, _n_(19141, "enumerate", lambda: enumerate), _n_(19142, "nums", lambda: nums)) if _n_(19144, "j", lambda: j) == _n_(19145, "max_val", lambda: max_val)]
    _l_(19146)
    min_result = [_n_(19147, "i", lambda: i) for (i, j) in _c_(19150, _n_(19148, "enumerate", lambda: enumerate), _n_(19149, "nums", lambda: nums)) if _n_(19151, "j", lambda: j) == _n_(19152, "min_val", lambda: min_val)]
    _l_(19153)
    aux = (_n_(19154, "max_result", lambda: max_result), _n_(19155, "min_result", lambda: min_result))
    _l_(19156)
    return aux
nums = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
_l_(19158)
_c_(19160, _n_(19159, "print", lambda: print), 'Original list:')
_l_(19161)
_c_(19164, _n_(19162, "print", lambda: print), _n_(19163, "nums", lambda: nums))
_l_(19165)
result = _c_(19168, _n_(19166, "position_max_min", lambda: position_max_min), _n_(19167, "nums", lambda: nums))
_l_(19169)
_c_(19171, _n_(19170, "print", lambda: print), '\nIndex positions of the maximum value of the said list:')
_l_(19172)
_c_(19175, _n_(19173, "print", lambda: print), _n_(19174, "result", lambda: result)[0])
_l_(19176)
_c_(19178, _n_(19177, "print", lambda: print), '\nIndex positions of the minimum value of the said list:')
_l_(19179)
_c_(19182, _n_(19180, "print", lambda: print), _n_(19181, "result", lambda: result)[1])
_l_(19183)