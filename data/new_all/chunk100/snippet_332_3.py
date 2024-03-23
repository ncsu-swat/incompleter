# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_min_list_tuples(nums):
    _l_(33308)

    _c_(33292, _n_(33290, "zip", lambda: zip), *_n_(33291, "nums", lambda: nums))
    _l_(33293)
    result2 = _c_(33299, _n_(33294, "map", lambda: map), _n_(33295, "min", lambda: min), _c_(33298, _n_(33296, "zip", lambda: zip), *_n_(33297, "nums", lambda: nums)))
    _l_(33300)
    aux = (_c_(33303, _n_(33301, "list", lambda: list), _n_(33302, "result1", lambda: result1)), _c_(33306, _n_(33304, "list", lambda: list), _n_(33305, "result2", lambda: result2)))
    _l_(33307)
    return aux
nums = [(2, 3), (2, 4), (0, 6), (7, 1)]
_l_(33309)
_c_(33311, _n_(33310, "print", lambda: print), 'Original list:')
_l_(33312)
_c_(33315, _n_(33313, "print", lambda: print), _n_(33314, "nums", lambda: nums))
_l_(33316)
result = _c_(33319, _n_(33317, "max_min_list_tuples", lambda: max_min_list_tuples), _n_(33318, "nums", lambda: nums))
_l_(33320)
_c_(33322, _n_(33321, "print", lambda: print), '\nMaximum value  for each tuple position in the said list of tuples:')
_l_(33323)
_c_(33326, _n_(33324, "print", lambda: print), _n_(33325, "result", lambda: result)[0])
_l_(33327)
_c_(33329, _n_(33328, "print", lambda: print), '\nMinimum value  for each tuple position in the said list of tuples:')
_l_(33330)
_c_(33333, _n_(33331, "print", lambda: print), _n_(33332, "result", lambda: result)[1])
_l_(33334)