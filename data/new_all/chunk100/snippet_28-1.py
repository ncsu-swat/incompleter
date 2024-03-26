# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def first_index(l1):
    _l_(108301)

    aux = _c_(108299, _n_(108295, "sum", lambda: sum), (1 for i in _n_(108296, "l1", lambda: l1) if _n_(108297, "i", lambda: i) > 45 and _n_(108298, "i", lambda: i) % 2 == 0))
    _l_(108300)
    return aux
nums = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
_l_(108302)
_c_(108304, _n_(108303, "print", lambda: print), 'Original list:')
_l_(108305)
_c_(108308, _n_(108306, "print", lambda: print), _n_(108307, "nums", lambda: nums))
_l_(108309)
_c_(108312, _n_(108310, "print", lambda: print), '\nNumber of Items of the said list which are even and greater than', _n_(108311, "n", lambda: n))
_l_(108313)
_c_(108318, _n_(108314, "print", lambda: print), _c_(108317, _n_(108315, "first_index", lambda: first_index), _n_(108316, "nums", lambda: nums)))
_l_(108319)