# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_min_list_tuples(nums):
    _l_(33171)

    _c_(33148, _n_(33146, "zip", lambda: zip), *_n_(33147, "nums", lambda: nums))
    _l_(33149)
    result1 = _c_(33155, _n_(33150, "map", lambda: map), _n_(33151, "max", lambda: max), _c_(33154, _n_(33152, "zip", lambda: zip), *_n_(33153, "nums", lambda: nums)))
    _l_(33156)
    result2 = _c_(33162, _n_(33157, "map", lambda: map), _n_(33158, "min", lambda: min), _c_(33161, _n_(33159, "zip", lambda: zip), *_n_(33160, "nums", lambda: nums)))
    _l_(33163)
    aux = (_c_(33166, _n_(33164, "list", lambda: list), _n_(33165, "result1", lambda: result1)), _c_(33169, _n_(33167, "list", lambda: list), _n_(33168, "result2", lambda: result2)))
    _l_(33170)
    return aux
nums = [(2, 3), (2, 4), (0, 6), (7, 1)]
_l_(33172)
_c_(33174, _n_(33173, "print", lambda: print), 'Original list:')
_l_(33175)
_c_(33178, _n_(33176, "print", lambda: print), _n_(33177, "nums", lambda: nums))
_l_(33179)
_c_(33181, _n_(33180, "print", lambda: print), '\nMaximum value  for each tuple position in the said list of tuples:')
_l_(33182)
_c_(33185, _n_(33183, "print", lambda: print), _n_(33184, "result", lambda: result)[0])
_l_(33186)
_c_(33188, _n_(33187, "print", lambda: print), '\nMinimum value  for each tuple position in the said list of tuples:')
_l_(33189)
_c_(33192, _n_(33190, "print", lambda: print), _n_(33191, "result", lambda: result)[1])
_l_(33193)