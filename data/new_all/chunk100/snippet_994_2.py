# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_column(nums, n):
    _l_(98633)

    for i in _n_(98628, "nums", lambda: nums):
        _l_(98630)

        del i[n]
        _l_(98629)
    aux = _n_(98631, "nums", lambda: nums)
    _l_(98632)
    return aux
list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
_l_(98634)
n = 0
_l_(98635)
_c_(98637, _n_(98636, "print", lambda: print), 'Original Nested list:')
_l_(98638)
_c_(98641, _n_(98639, "print", lambda: print), _n_(98640, "list1", lambda: list1))
_l_(98642)
_c_(98644, _n_(98643, "print", lambda: print), 'After removing 1st column:')
_l_(98645)
_c_(98651, _n_(98646, "print", lambda: print), _c_(98650, _n_(98647, "remove_column", lambda: remove_column), _n_(98648, "list1", lambda: list1), _n_(98649, "n", lambda: n)))
_l_(98652)
n = 2
_l_(98653)
_c_(98655, _n_(98654, "print", lambda: print), '\nOriginal Nested list:')
_l_(98656)
_c_(98659, _n_(98657, "print", lambda: print), _n_(98658, "list2", lambda: list2))
_l_(98660)
_c_(98662, _n_(98661, "print", lambda: print), 'After removing 3rd column:')
_l_(98663)
_c_(98669, _n_(98664, "print", lambda: print), _c_(98668, _n_(98665, "remove_column", lambda: remove_column), _n_(98666, "list2", lambda: list2), _n_(98667, "n", lambda: n)))
_l_(98670)