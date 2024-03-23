# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sort_on_specific_item(lst, n):
    _l_(38115)

    result = _c_(38111, _n_(38107, "sorted", lambda: sorted), _n_(38108, "lst", lambda: lst), key=lambda x: _n_(38109, "x", lambda: x)[_n_(38110, "n", lambda: n)])
    _l_(38112)
    aux = _n_(38113, "result", lambda: result)
    _l_(38114)
    return aux
items = [('item2', 10, 10.12), ('item3', 15, 25.1), ('item1', 11, 24.5), ('item4', 12, 22.5)]
_l_(38116)
_c_(38118, _n_(38117, "print", lambda: print), 'Original list of tuples:')
_l_(38119)
_c_(38122, _n_(38120, "print", lambda: print), _n_(38121, "items", lambda: items))
_l_(38123)
_c_(38125, _n_(38124, "print", lambda: print), '\nSort on 1st element of the tuple of the said list:')
_l_(38126)
_c_(38132, _n_(38127, "print", lambda: print), _c_(38131, _n_(38128, "sort_on_specific_item", lambda: sort_on_specific_item), _n_(38129, "items", lambda: items), _n_(38130, "n", lambda: n)))
_l_(38133)
_c_(38135, _n_(38134, "print", lambda: print), '\nSort on 2nd element of the tuple of the said list:')
_l_(38136)
n = 1
_l_(38137)
_c_(38143, _n_(38138, "print", lambda: print), _c_(38142, _n_(38139, "sort_on_specific_item", lambda: sort_on_specific_item), _n_(38140, "items", lambda: items), _n_(38141, "n", lambda: n)))
_l_(38144)
_c_(38146, _n_(38145, "print", lambda: print), '\nSort on 3rd element of the tuple of the said list:')
_l_(38147)
n = 2
_l_(38148)
_c_(38154, _n_(38149, "print", lambda: print), _c_(38153, _n_(38150, "sort_on_specific_item", lambda: sort_on_specific_item), _n_(38151, "items", lambda: items), _n_(38152, "n", lambda: n)))
_l_(38155)