# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def interleave_multiple_lists(list1, list2, list3):
    _l_(110300)

    result = [_n_(110290, "el", lambda: el) for pair in _c_(110295, _n_(110291, "zip", lambda: zip), _n_(110292, "list1", lambda: list1), _n_(110293, "list2", lambda: list2), _n_(110294, "list3", lambda: list3)) for el in _n_(110296, "pair", lambda: pair)]
    _l_(110297)
    aux = _n_(110298, "result", lambda: result)
    _l_(110299)
    return aux
list2 = [10, 20, 30, 40, 50, 60, 70]
_l_(110301)
list3 = [100, 200, 300, 400, 500, 600, 700]
_l_(110302)
_c_(110304, _n_(110303, "print", lambda: print), 'Original list:')
_l_(110305)
_c_(110308, _n_(110306, "print", lambda: print), 'list1:', _n_(110307, "list1", lambda: list1))
_l_(110309)
_c_(110312, _n_(110310, "print", lambda: print), 'list2:', _n_(110311, "list2", lambda: list2))
_l_(110313)
_c_(110316, _n_(110314, "print", lambda: print), 'list3:', _n_(110315, "list3", lambda: list3))
_l_(110317)
_c_(110319, _n_(110318, "print", lambda: print), '\nInterleave multiple lists:')
_l_(110320)
_c_(110327, _n_(110321, "print", lambda: print), _c_(110326, _n_(110322, "interleave_multiple_lists", lambda: interleave_multiple_lists), _n_(110323, "list1", lambda: list1), _n_(110324, "list2", lambda: list2), _n_(110325, "list3", lambda: list3)))
_l_(110328)