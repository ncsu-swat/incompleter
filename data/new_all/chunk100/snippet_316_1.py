# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def interleave_multiple_lists(list1, list2, list3):
    _l_(30297)

    result = [_n_(30287, "el", lambda: el) for pair in _c_(30292, _n_(30288, "zip", lambda: zip), _n_(30289, "list1", lambda: list1), _n_(30290, "list2", lambda: list2), _n_(30291, "list3", lambda: list3)) for el in _n_(30293, "pair", lambda: pair)]
    _l_(30294)
    aux = _n_(30295, "result", lambda: result)
    _l_(30296)
    return aux
list2 = [10, 20, 30, 40, 50, 60, 70]
_l_(30298)
list3 = [100, 200, 300, 400, 500, 600, 700]
_l_(30299)
_c_(30301, _n_(30300, "print", lambda: print), 'Original list:')
_l_(30302)
_c_(30305, _n_(30303, "print", lambda: print), 'list1:', _n_(30304, "list1", lambda: list1))
_l_(30306)
_c_(30309, _n_(30307, "print", lambda: print), 'list2:', _n_(30308, "list2", lambda: list2))
_l_(30310)
_c_(30313, _n_(30311, "print", lambda: print), 'list3:', _n_(30312, "list3", lambda: list3))
_l_(30314)
_c_(30316, _n_(30315, "print", lambda: print), '\nInterleave multiple lists:')
_l_(30317)
_c_(30324, _n_(30318, "print", lambda: print), _c_(30323, _n_(30319, "interleave_multiple_lists", lambda: interleave_multiple_lists), _n_(30320, "list1", lambda: list1), _n_(30321, "list2", lambda: list2), _n_(30322, "list3", lambda: list3)))
_l_(30325)