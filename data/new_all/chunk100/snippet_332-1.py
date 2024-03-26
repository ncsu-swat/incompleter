# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def max_min_list_tuples(nums):
    _l_(110831)

    _c_(110808, _n_(110806, "zip", lambda: zip), *_n_(110807, "nums", lambda: nums))
    _l_(110809)
    result1 = _c_(110815, _n_(110810, "map", lambda: map), _n_(110811, "max", lambda: max), _c_(110814, _n_(110812, "zip", lambda: zip), *_n_(110813, "nums", lambda: nums)))
    _l_(110816)
    result2 = _c_(110822, _n_(110817, "map", lambda: map), _n_(110818, "min", lambda: min), _c_(110821, _n_(110819, "zip", lambda: zip), *_n_(110820, "nums", lambda: nums)))
    _l_(110823)
    aux = (_c_(110826, _n_(110824, "list", lambda: list), _n_(110825, "result1", lambda: result1)), _c_(110829, _n_(110827, "list", lambda: list), _n_(110828, "result2", lambda: result2)))
    _l_(110830)
    return aux
_c_(110833, _n_(110832, "print", lambda: print), 'Original list:')
_l_(110834)
_c_(110837, _n_(110835, "print", lambda: print), _n_(110836, "nums", lambda: nums))
_l_(110838)
result = _c_(110841, _n_(110839, "max_min_list_tuples", lambda: max_min_list_tuples), _n_(110840, "nums", lambda: nums))
_l_(110842)
_c_(110844, _n_(110843, "print", lambda: print), '\nMaximum value  for each tuple position in the said list of tuples:')
_l_(110845)
_c_(110848, _n_(110846, "print", lambda: print), _n_(110847, "result", lambda: result)[0])
_l_(110849)
_c_(110851, _n_(110850, "print", lambda: print), '\nMinimum value  for each tuple position in the said list of tuples:')
_l_(110852)
_c_(110855, _n_(110853, "print", lambda: print), _n_(110854, "result", lambda: result)[1])
_l_(110856)