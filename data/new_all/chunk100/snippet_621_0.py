# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_range_in_list(li, min, max):
    _l_(65257)

    for x in _n_(65248, "li", lambda: li):
        _l_(65254)

        if _n_(65249, "min", lambda: min) <= _n_(65250, "x", lambda: x) <= _n_(65251, "max", lambda: max):
            _l_(65253)

            ctr += 1
            _l_(65252)
    aux = _n_(65255, "ctr", lambda: ctr)
    _l_(65256)
    return aux
list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
_l_(65258)
_c_(65263, _n_(65259, "print", lambda: print), _c_(65262, _n_(65260, "count_range_in_list", lambda: count_range_in_list), _n_(65261, "list1", lambda: list1), 40, 100))
_l_(65264)
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
_l_(65265)
_c_(65270, _n_(65266, "print", lambda: print), _c_(65269, _n_(65267, "count_range_in_list", lambda: count_range_in_list), _n_(65268, "list2", lambda: list2), 'a', 'e'))
_l_(65271)