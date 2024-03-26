# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def unique_values_in_list_of_lists(lst):
    _l_(118843)

    result = _c_(118837, _n_(118833, "set", lambda: set), (_n_(118834, "x", lambda: x) for l in _n_(118835, "lst", lambda: lst) for x in _n_(118836, "l", lambda: l)))
    _l_(118838)
    aux = _c_(118841, _n_(118839, "list", lambda: list), _n_(118840, "result", lambda: result))
    _l_(118842)
    return aux
nums = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]
_l_(118844)
_c_(118846, _n_(118845, "print", lambda: print), 'Original list:')
_l_(118847)
_c_(118850, _n_(118848, "print", lambda: print), _n_(118849, "nums", lambda: nums))
_l_(118851)
_c_(118853, _n_(118852, "print", lambda: print), 'Unique values of the said list of lists:')
_l_(118854)
_c_(118859, _n_(118855, "print", lambda: print), _c_(118858, _n_(118856, "unique_values_in_list_of_lists", lambda: unique_values_in_list_of_lists), _n_(118857, "nums", lambda: nums)))
_l_(118860)
_c_(118862, _n_(118861, "print", lambda: print), '\nOriginal list:')
_l_(118863)
_c_(118866, _n_(118864, "print", lambda: print), _n_(118865, "chars", lambda: chars))
_l_(118867)
_c_(118869, _n_(118868, "print", lambda: print), 'Unique values of the said list of lists:')
_l_(118870)
_c_(118875, _n_(118871, "print", lambda: print), _c_(118874, _n_(118872, "unique_values_in_list_of_lists", lambda: unique_values_in_list_of_lists), _n_(118873, "chars", lambda: chars)))
_l_(118876)