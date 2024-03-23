# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def position_max_min(nums):
    _l_(19202)

    max_val = _c_(19186, _n_(19184, "max", lambda: max), _n_(19185, "nums", lambda: nums))
    _l_(19187)
    min_val = _c_(19190, _n_(19188, "min", lambda: min), _n_(19189, "nums", lambda: nums))
    _l_(19191)
    max_result = [_n_(19192, "i", lambda: i) for (i, j) in _c_(19195, _n_(19193, "enumerate", lambda: enumerate), _n_(19194, "nums", lambda: nums)) if _n_(19196, "j", lambda: j) == _n_(19197, "max_val", lambda: max_val)]
    _l_(19198)
    aux = (_n_(19199, "max_result", lambda: max_result), _n_(19200, "min_result", lambda: min_result))
    _l_(19201)
    return aux
nums = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]
_l_(19203)
_c_(19205, _n_(19204, "print", lambda: print), 'Original list:')
_l_(19206)
_c_(19209, _n_(19207, "print", lambda: print), _n_(19208, "nums", lambda: nums))
_l_(19210)
result = _c_(19213, _n_(19211, "position_max_min", lambda: position_max_min), _n_(19212, "nums", lambda: nums))
_l_(19214)
_c_(19216, _n_(19215, "print", lambda: print), '\nIndex positions of the maximum value of the said list:')
_l_(19217)
_c_(19220, _n_(19218, "print", lambda: print), _n_(19219, "result", lambda: result)[0])
_l_(19221)
_c_(19223, _n_(19222, "print", lambda: print), '\nIndex positions of the minimum value of the said list:')
_l_(19224)
_c_(19227, _n_(19225, "print", lambda: print), _n_(19226, "result", lambda: result)[1])
_l_(19228)