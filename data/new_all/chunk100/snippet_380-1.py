# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sort_on_specific_item(lst, n):
    _l_(113723)

    result = _c_(113719, _n_(113715, "sorted", lambda: sorted), _n_(113716, "lst", lambda: lst), key=lambda x: _n_(113717, "x", lambda: x)[_n_(113718, "n", lambda: n)])
    _l_(113720)
    aux = _n_(113721, "result", lambda: result)
    _l_(113722)
    return aux
_c_(113725, _n_(113724, "print", lambda: print), 'Original list of tuples:')
_l_(113726)
_c_(113729, _n_(113727, "print", lambda: print), _n_(113728, "items", lambda: items))
_l_(113730)
_c_(113732, _n_(113731, "print", lambda: print), '\nSort on 1st element of the tuple of the said list:')
_l_(113733)
n = 0
_l_(113734)
_c_(113740, _n_(113735, "print", lambda: print), _c_(113739, _n_(113736, "sort_on_specific_item", lambda: sort_on_specific_item), _n_(113737, "items", lambda: items), _n_(113738, "n", lambda: n)))
_l_(113741)
_c_(113743, _n_(113742, "print", lambda: print), '\nSort on 2nd element of the tuple of the said list:')
_l_(113744)
n = 1
_l_(113745)
_c_(113751, _n_(113746, "print", lambda: print), _c_(113750, _n_(113747, "sort_on_specific_item", lambda: sort_on_specific_item), _n_(113748, "items", lambda: items), _n_(113749, "n", lambda: n)))
_l_(113752)
_c_(113754, _n_(113753, "print", lambda: print), '\nSort on 3rd element of the tuple of the said list:')
_l_(113755)
n = 2
_l_(113756)
_c_(113762, _n_(113757, "print", lambda: print), _c_(113761, _n_(113758, "sort_on_specific_item", lambda: sort_on_specific_item), _n_(113759, "items", lambda: items), _n_(113760, "n", lambda: n)))
_l_(113763)