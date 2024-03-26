# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_min_list_tuples(nums):
    _l_(110783)

    _c_(110760, _n_(110758, "zip", lambda: zip), *_n_(110759, "nums", lambda: nums))
    _l_(110761)
    result1 = _c_(110767, _n_(110762, "map", lambda: map), _n_(110763, "max", lambda: max), _c_(110766, _n_(110764, "zip", lambda: zip), *_n_(110765, "nums", lambda: nums)))
    _l_(110768)
    result2 = _c_(110774, _n_(110769, "map", lambda: map), _n_(110770, "min", lambda: min), _c_(110773, _n_(110771, "zip", lambda: zip), *_n_(110772, "nums", lambda: nums)))
    _l_(110775)
    aux = (_c_(110778, _n_(110776, "list", lambda: list), _n_(110777, "result1", lambda: result1)), _c_(110781, _n_(110779, "list", lambda: list), _n_(110780, "result2", lambda: result2)))
    _l_(110782)
    return aux
nums = [(2, 3), (2, 4), (0, 6), (7, 1)]
_l_(110784)
_c_(110786, _n_(110785, "print", lambda: print), 'Original list:')
_l_(110787)
_c_(110790, _n_(110788, "print", lambda: print), _n_(110789, "nums", lambda: nums))
_l_(110791)
_c_(110793, _n_(110792, "print", lambda: print), '\nMaximum value  for each tuple position in the said list of tuples:')
_l_(110794)
_c_(110797, _n_(110795, "print", lambda: print), _n_(110796, "result", lambda: result)[0])
_l_(110798)
_c_(110800, _n_(110799, "print", lambda: print), '\nMinimum value  for each tuple position in the said list of tuples:')
_l_(110801)
_c_(110804, _n_(110802, "print", lambda: print), _n_(110803, "result", lambda: result)[1])
_l_(110805)