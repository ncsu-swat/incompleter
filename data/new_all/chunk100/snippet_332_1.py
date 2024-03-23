# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_min_list_tuples(nums):
    _l_(33219)

    _c_(33196, _n_(33194, "zip", lambda: zip), *_n_(33195, "nums", lambda: nums))
    _l_(33197)
    result1 = _c_(33203, _n_(33198, "map", lambda: map), _n_(33199, "max", lambda: max), _c_(33202, _n_(33200, "zip", lambda: zip), *_n_(33201, "nums", lambda: nums)))
    _l_(33204)
    result2 = _c_(33210, _n_(33205, "map", lambda: map), _n_(33206, "min", lambda: min), _c_(33209, _n_(33207, "zip", lambda: zip), *_n_(33208, "nums", lambda: nums)))
    _l_(33211)
    aux = (_c_(33214, _n_(33212, "list", lambda: list), _n_(33213, "result1", lambda: result1)), _c_(33217, _n_(33215, "list", lambda: list), _n_(33216, "result2", lambda: result2)))
    _l_(33218)
    return aux
_c_(33221, _n_(33220, "print", lambda: print), 'Original list:')
_l_(33222)
_c_(33225, _n_(33223, "print", lambda: print), _n_(33224, "nums", lambda: nums))
_l_(33226)
result = _c_(33229, _n_(33227, "max_min_list_tuples", lambda: max_min_list_tuples), _n_(33228, "nums", lambda: nums))
_l_(33230)
_c_(33232, _n_(33231, "print", lambda: print), '\nMaximum value  for each tuple position in the said list of tuples:')
_l_(33233)
_c_(33236, _n_(33234, "print", lambda: print), _n_(33235, "result", lambda: result)[0])
_l_(33237)
_c_(33239, _n_(33238, "print", lambda: print), '\nMinimum value  for each tuple position in the said list of tuples:')
_l_(33240)
_c_(33243, _n_(33241, "print", lambda: print), _n_(33242, "result", lambda: result)[1])
_l_(33244)