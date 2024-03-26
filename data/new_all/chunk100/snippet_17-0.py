# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def position_max_min(nums):
    _l_(103227)

    max_result = _c_(103215, _n_(103210, "max", lambda: max), _c_(103213, _n_(103211, "enumerate", lambda: enumerate), _n_(103212, "nums", lambda: nums)), key=lambda x: _n_(103214, "x", lambda: x)[1])
    _l_(103216)
    min_result = _c_(103222, _n_(103217, "min", lambda: min), _c_(103220, _n_(103218, "enumerate", lambda: enumerate), _n_(103219, "nums", lambda: nums)), key=lambda x: _n_(103221, "x", lambda: x)[1])
    _l_(103223)
    aux = (_n_(103224, "max_result", lambda: max_result), _n_(103225, "min_result", lambda: min_result))
    _l_(103226)
    return aux
_c_(103229, _n_(103228, "print", lambda: print), 'Original list:')
_l_(103230)
_c_(103233, _n_(103231, "print", lambda: print), _n_(103232, "nums", lambda: nums))
_l_(103234)
result = _c_(103237, _n_(103235, "position_max_min", lambda: position_max_min), _n_(103236, "nums", lambda: nums))
_l_(103238)
_c_(103240, _n_(103239, "print", lambda: print), '\nIndex position and value of the maximum value of the said list:')
_l_(103241)
_c_(103244, _n_(103242, "print", lambda: print), _n_(103243, "result", lambda: result)[0])
_l_(103245)
_c_(103247, _n_(103246, "print", lambda: print), '\nIndex position and value of the minimum value of the said list:')
_l_(103248)
_c_(103251, _n_(103249, "print", lambda: print), _n_(103250, "result", lambda: result)[1])
_l_(103252)