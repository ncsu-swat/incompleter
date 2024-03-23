# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sort_on_specific_item(lst, n):
    _l_(38164)

    result = _c_(38160, _n_(38156, "sorted", lambda: sorted), _n_(38157, "lst", lambda: lst), key=lambda x: _n_(38158, "x", lambda: x)[_n_(38159, "n", lambda: n)])
    _l_(38161)
    aux = _n_(38162, "result", lambda: result)
    _l_(38163)
    return aux
_c_(38166, _n_(38165, "print", lambda: print), 'Original list of tuples:')
_l_(38167)
_c_(38170, _n_(38168, "print", lambda: print), _n_(38169, "items", lambda: items))
_l_(38171)
_c_(38173, _n_(38172, "print", lambda: print), '\nSort on 1st element of the tuple of the said list:')
_l_(38174)
n = 0
_l_(38175)
_c_(38181, _n_(38176, "print", lambda: print), _c_(38180, _n_(38177, "sort_on_specific_item", lambda: sort_on_specific_item), _n_(38178, "items", lambda: items), _n_(38179, "n", lambda: n)))
_l_(38182)
_c_(38184, _n_(38183, "print", lambda: print), '\nSort on 2nd element of the tuple of the said list:')
_l_(38185)
n = 1
_l_(38186)
_c_(38192, _n_(38187, "print", lambda: print), _c_(38191, _n_(38188, "sort_on_specific_item", lambda: sort_on_specific_item), _n_(38189, "items", lambda: items), _n_(38190, "n", lambda: n)))
_l_(38193)
_c_(38195, _n_(38194, "print", lambda: print), '\nSort on 3rd element of the tuple of the said list:')
_l_(38196)
n = 2
_l_(38197)
_c_(38203, _n_(38198, "print", lambda: print), _c_(38202, _n_(38199, "sort_on_specific_item", lambda: sort_on_specific_item), _n_(38200, "items", lambda: items), _n_(38201, "n", lambda: n)))
_l_(38204)