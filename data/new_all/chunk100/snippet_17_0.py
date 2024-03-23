# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def position_max_min(nums):
    _l_(14183)

    min_result = _c_(14178, _n_(14173, "min", lambda: min), _c_(14176, _n_(14174, "enumerate", lambda: enumerate), _n_(14175, "nums", lambda: nums)), key=lambda x: _n_(14177, "x", lambda: x)[1])
    _l_(14179)
    aux = (_n_(14180, "max_result", lambda: max_result), _n_(14181, "min_result", lambda: min_result))
    _l_(14182)
    return aux
nums = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
_l_(14184)
_c_(14186, _n_(14185, "print", lambda: print), 'Original list:')
_l_(14187)
_c_(14190, _n_(14188, "print", lambda: print), _n_(14189, "nums", lambda: nums))
_l_(14191)
result = _c_(14194, _n_(14192, "position_max_min", lambda: position_max_min), _n_(14193, "nums", lambda: nums))
_l_(14195)
_c_(14197, _n_(14196, "print", lambda: print), '\nIndex position and value of the maximum value of the said list:')
_l_(14198)
_c_(14201, _n_(14199, "print", lambda: print), _n_(14200, "result", lambda: result)[0])
_l_(14202)
_c_(14204, _n_(14203, "print", lambda: print), '\nIndex position and value of the minimum value of the said list:')
_l_(14205)
_c_(14208, _n_(14206, "print", lambda: print), _n_(14207, "result", lambda: result)[1])
_l_(14209)