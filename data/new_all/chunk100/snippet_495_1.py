# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unique_values_in_list_of_lists(lst):
    _l_(51831)

    result = _c_(51825, _n_(51821, "set", lambda: set), (_n_(51822, "x", lambda: x) for l in _n_(51823, "lst", lambda: lst) for x in _n_(51824, "l", lambda: l)))
    _l_(51826)
    aux = _c_(51829, _n_(51827, "list", lambda: list), _n_(51828, "result", lambda: result))
    _l_(51830)
    return aux
nums = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
_l_(51832)
_c_(51834, _n_(51833, "print", lambda: print), 'Original list:')
_l_(51835)
_c_(51838, _n_(51836, "print", lambda: print), _n_(51837, "nums", lambda: nums))
_l_(51839)
_c_(51841, _n_(51840, "print", lambda: print), 'Unique values of the said list of lists:')
_l_(51842)
_c_(51847, _n_(51843, "print", lambda: print), _c_(51846, _n_(51844, "unique_values_in_list_of_lists", lambda: unique_values_in_list_of_lists), _n_(51845, "nums", lambda: nums)))
_l_(51848)
_c_(51850, _n_(51849, "print", lambda: print), '\nOriginal list:')
_l_(51851)
_c_(51854, _n_(51852, "print", lambda: print), _n_(51853, "chars", lambda: chars))
_l_(51855)
_c_(51857, _n_(51856, "print", lambda: print), 'Unique values of the said list of lists:')
_l_(51858)
_c_(51863, _n_(51859, "print", lambda: print), _c_(51862, _n_(51860, "unique_values_in_list_of_lists", lambda: unique_values_in_list_of_lists), _n_(51861, "chars", lambda: chars)))
_l_(51864)