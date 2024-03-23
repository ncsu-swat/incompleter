# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def count_range_in_list(li, min, max):
    _l_(65282)

    ctr = 0
    _l_(65272)
    for x in _n_(65273, "li", lambda: li):
        _l_(65279)

        if _n_(65274, "min", lambda: min) <= _n_(65275, "x", lambda: x) <= _n_(65276, "max", lambda: max):
            _l_(65278)

            ctr += 1
            _l_(65277)
    aux = _n_(65280, "ctr", lambda: ctr)
    _l_(65281)
    return aux
list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]
_l_(65283)
_c_(65288, _n_(65284, "print", lambda: print), _c_(65287, _n_(65285, "count_range_in_list", lambda: count_range_in_list), _n_(65286, "list1", lambda: list1), 40, 100))
_l_(65289)
_c_(65294, _n_(65290, "print", lambda: print), _c_(65293, _n_(65291, "count_range_in_list", lambda: count_range_in_list), _n_(65292, "list2", lambda: list2), 'a', 'e'))
_l_(65295)