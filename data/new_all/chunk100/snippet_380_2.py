# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sort_on_specific_item(lst, n):
    _l_(38066)

    result = _c_(38062, _n_(38058, "sorted", lambda: sorted), _n_(38059, "lst", lambda: lst), key=lambda x: _n_(38060, "x", lambda: x)[_n_(38061, "n", lambda: n)])
    _l_(38063)
    aux = _n_(38064, "result", lambda: result)
    _l_(38065)
    return aux
items = [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
_l_(38067)
_c_(38069, _n_(38068, "print", lambda: print), 'Original list of tuples:')
_l_(38070)
_c_(38073, _n_(38071, "print", lambda: print), _n_(38072, "items", lambda: items))
_l_(38074)
_c_(38076, _n_(38075, "print", lambda: print), '\nSort on 1st element of the tuple of the said list:')
_l_(38077)
n = 0
_l_(38078)
_c_(38084, _n_(38079, "print", lambda: print), _c_(38083, _n_(38080, "sort_on_specific_item", lambda: sort_on_specific_item), _n_(38081, "items", lambda: items), _n_(38082, "n", lambda: n)))
_l_(38085)
_c_(38087, _n_(38086, "print", lambda: print), '\nSort on 2nd element of the tuple of the said list:')
_l_(38088)
_c_(38094, _n_(38089, "print", lambda: print), _c_(38093, _n_(38090, "sort_on_specific_item", lambda: sort_on_specific_item), _n_(38091, "items", lambda: items), _n_(38092, "n", lambda: n)))
_l_(38095)
_c_(38097, _n_(38096, "print", lambda: print), '\nSort on 3rd element of the tuple of the said list:')
_l_(38098)
n = 2
_l_(38099)
_c_(38105, _n_(38100, "print", lambda: print), _c_(38104, _n_(38101, "sort_on_specific_item", lambda: sort_on_specific_item), _n_(38102, "items", lambda: items), _n_(38103, "n", lambda: n)))
_l_(38106)