# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def position_max_min(nums):
    _l_(103270)

    max_result = _c_(103258, _n_(103253, "max", lambda: max), _c_(103256, _n_(103254, "enumerate", lambda: enumerate), _n_(103255, "nums", lambda: nums)), key=lambda x: _n_(103257, "x", lambda: x)[1])
    _l_(103259)
    min_result = _c_(103265, _n_(103260, "min", lambda: min), _c_(103263, _n_(103261, "enumerate", lambda: enumerate), _n_(103262, "nums", lambda: nums)), key=lambda x: _n_(103264, "x", lambda: x)[1])
    _l_(103266)
    aux = (_n_(103267, "max_result", lambda: max_result), _n_(103268, "min_result", lambda: min_result))
    _l_(103269)
    return aux
nums = [12, 33, 23, 10.11, 67, 89, 45, 66.7, 23, 12, 11, 10.25, 54]
_l_(103271)
_c_(103273, _n_(103272, "print", lambda: print), 'Original list:')
_l_(103274)
_c_(103277, _n_(103275, "print", lambda: print), _n_(103276, "nums", lambda: nums))
_l_(103278)
_c_(103280, _n_(103279, "print", lambda: print), '\nIndex position and value of the maximum value of the said list:')
_l_(103281)
_c_(103284, _n_(103282, "print", lambda: print), _n_(103283, "result", lambda: result)[0])
_l_(103285)
_c_(103287, _n_(103286, "print", lambda: print), '\nIndex position and value of the minimum value of the said list:')
_l_(103288)
_c_(103291, _n_(103289, "print", lambda: print), _n_(103290, "result", lambda: result)[1])
_l_(103292)