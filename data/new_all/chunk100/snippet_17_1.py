# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def position_max_min(nums):
    _l_(14227)

    max_result = _c_(14215, _n_(14210, "max", lambda: max), _c_(14213, _n_(14211, "enumerate", lambda: enumerate), _n_(14212, "nums", lambda: nums)), key=lambda x: _n_(14214, "x", lambda: x)[1])
    _l_(14216)
    min_result = _c_(14222, _n_(14217, "min", lambda: min), _c_(14220, _n_(14218, "enumerate", lambda: enumerate), _n_(14219, "nums", lambda: nums)), key=lambda x: _n_(14221, "x", lambda: x)[1])
    _l_(14223)
    aux = (_n_(14224, "max_result", lambda: max_result), _n_(14225, "min_result", lambda: min_result))
    _l_(14226)
    return aux
_c_(14229, _n_(14228, "print", lambda: print), 'Original list:')
_l_(14230)
_c_(14233, _n_(14231, "print", lambda: print), _n_(14232, "nums", lambda: nums))
_l_(14234)
result = _c_(14237, _n_(14235, "position_max_min", lambda: position_max_min), _n_(14236, "nums", lambda: nums))
_l_(14238)
_c_(14240, _n_(14239, "print", lambda: print), '\nIndex position and value of the maximum value of the said list:')
_l_(14241)
_c_(14244, _n_(14242, "print", lambda: print), _n_(14243, "result", lambda: result)[0])
_l_(14245)
_c_(14247, _n_(14246, "print", lambda: print), '\nIndex position and value of the minimum value of the said list:')
_l_(14248)
_c_(14251, _n_(14249, "print", lambda: print), _n_(14250, "result", lambda: result)[1])
_l_(14252)