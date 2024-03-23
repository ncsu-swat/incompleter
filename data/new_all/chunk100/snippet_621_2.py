# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_range_in_list(li, min, max):
    _l_(65306)

    ctr = 0
    _l_(65296)
    for x in _n_(65297, "li", lambda: li):
        _l_(65303)

        if _n_(65298, "min", lambda: min) <= _n_(65299, "x", lambda: x) <= _n_(65300, "max", lambda: max):
            _l_(65302)

            ctr += 1
            _l_(65301)
    aux = _n_(65304, "ctr", lambda: ctr)
    _l_(65305)
    return aux
_c_(65311, _n_(65307, "print", lambda: print), _c_(65310, _n_(65308, "count_range_in_list", lambda: count_range_in_list), _n_(65309, "list1", lambda: list1), 40, 100))
_l_(65312)
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
_l_(65313)
_c_(65318, _n_(65314, "print", lambda: print), _c_(65317, _n_(65315, "count_range_in_list", lambda: count_range_in_list), _n_(65316, "list2", lambda: list2), 'a', 'e'))
_l_(65319)