# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sort_sublists(input_list):
    _l_(18845)

    result = [_c_(18840, _n_(18837, "sorted", lambda: sorted), _n_(18838, "x", lambda: x), key=lambda x: _n_(18839, "x", lambda: x)[0]) for x in _n_(18841, "input_list", lambda: input_list)]
    _l_(18842)
    aux = _n_(18843, "result", lambda: result)
    _l_(18844)
    return aux
_c_(18847, _n_(18846, "print", lambda: print), '\nOriginal list:')
_l_(18848)
_c_(18851, _n_(18849, "print", lambda: print), _n_(18850, "color1", lambda: color1))
_l_(18852)
_c_(18854, _n_(18853, "print", lambda: print), '\nAfter sorting each sublist of the said list of lists:')
_l_(18855)
_c_(18860, _n_(18856, "print", lambda: print), _c_(18859, _n_(18857, "sort_sublists", lambda: sort_sublists), _n_(18858, "color1", lambda: color1)))
_l_(18861)