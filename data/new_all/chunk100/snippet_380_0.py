# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sort_on_specific_item(lst, n):
    _l_(37973)

    result = _c_(37969, _n_(37965, "sorted", lambda: sorted), _n_(37966, "lst", lambda: lst), key=lambda x: _n_(37967, "x", lambda: x)[_n_(37968, "n", lambda: n)])
    _l_(37970)
    aux = _n_(37971, "result", lambda: result)
    _l_(37972)
    return aux
items = [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
_l_(37974)
_c_(37976, _n_(37975, "print", lambda: print), 'Original list of tuples:')
_l_(37977)
_c_(37980, _n_(37978, "print", lambda: print), _n_(37979, "items", lambda: items))
_l_(37981)
_c_(37983, _n_(37982, "print", lambda: print), '\nSort on 1st element of the tuple of the said list:')
_l_(37984)
n = 0
_l_(37985)
_c_(37991, _n_(37986, "print", lambda: print), _c_(37990, _n_(37987, "sort_on_specific_item", lambda: sort_on_specific_item), _n_(37988, "items", lambda: items), _n_(37989, "n", lambda: n)))
_l_(37992)
_c_(37994, _n_(37993, "print", lambda: print), '\nSort on 2nd element of the tuple of the said list:')
_l_(37995)
n = 1
_l_(37996)
_c_(38002, _n_(37997, "print", lambda: print), _c_(38001, _n_(37998, "sort_on_specific_item", lambda: sort_on_specific_item), _n_(37999, "items", lambda: items), _n_(38000, "n", lambda: n)))
_l_(38003)
_c_(38005, _n_(38004, "print", lambda: print), '\nSort on 3rd element of the tuple of the said list:')
_l_(38006)
_c_(38012, _n_(38007, "print", lambda: print), _c_(38011, _n_(38008, "sort_on_specific_item", lambda: sort_on_specific_item), _n_(38009, "items", lambda: items), _n_(38010, "n", lambda: n)))
_l_(38013)