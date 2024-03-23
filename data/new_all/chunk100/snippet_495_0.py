# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unique_values_in_list_of_lists(lst):
    _l_(51787)

    result = _c_(51781, _n_(51777, "set", lambda: set), (_n_(51778, "x", lambda: x) for l in _n_(51779, "lst", lambda: lst) for x in _n_(51780, "l", lambda: l)))
    _l_(51782)
    aux = _c_(51785, _n_(51783, "list", lambda: list), _n_(51784, "result", lambda: result))
    _l_(51786)
    return aux
_c_(51789, _n_(51788, "print", lambda: print), 'Original list:')
_l_(51790)
_c_(51793, _n_(51791, "print", lambda: print), _n_(51792, "nums", lambda: nums))
_l_(51794)
_c_(51796, _n_(51795, "print", lambda: print), 'Unique values of the said list of lists:')
_l_(51797)
_c_(51802, _n_(51798, "print", lambda: print), _c_(51801, _n_(51799, "unique_values_in_list_of_lists", lambda: unique_values_in_list_of_lists), _n_(51800, "nums", lambda: nums)))
_l_(51803)
chars = [['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]
_l_(51804)
_c_(51806, _n_(51805, "print", lambda: print), '\nOriginal list:')
_l_(51807)
_c_(51810, _n_(51808, "print", lambda: print), _n_(51809, "chars", lambda: chars))
_l_(51811)
_c_(51813, _n_(51812, "print", lambda: print), 'Unique values of the said list of lists:')
_l_(51814)
_c_(51819, _n_(51815, "print", lambda: print), _c_(51818, _n_(51816, "unique_values_in_list_of_lists", lambda: unique_values_in_list_of_lists), _n_(51817, "chars", lambda: chars)))
_l_(51820)