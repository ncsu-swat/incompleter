# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_column(nums, n):
    _l_(98676)

    for i in _n_(98671, "nums", lambda: nums):
        _l_(98673)

        del i[n]
        _l_(98672)
    aux = _n_(98674, "nums", lambda: nums)
    _l_(98675)
    return aux
list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
_l_(98677)
_c_(98679, _n_(98678, "print", lambda: print), 'Original Nested list:')
_l_(98680)
_c_(98683, _n_(98681, "print", lambda: print), _n_(98682, "list1", lambda: list1))
_l_(98684)
_c_(98686, _n_(98685, "print", lambda: print), 'After removing 1st column:')
_l_(98687)
_c_(98693, _n_(98688, "print", lambda: print), _c_(98692, _n_(98689, "remove_column", lambda: remove_column), _n_(98690, "list1", lambda: list1), _n_(98691, "n", lambda: n)))
_l_(98694)
list2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
_l_(98695)
n = 2
_l_(98696)
_c_(98698, _n_(98697, "print", lambda: print), '\nOriginal Nested list:')
_l_(98699)
_c_(98702, _n_(98700, "print", lambda: print), _n_(98701, "list2", lambda: list2))
_l_(98703)
_c_(98705, _n_(98704, "print", lambda: print), 'After removing 3rd column:')
_l_(98706)
_c_(98712, _n_(98707, "print", lambda: print), _c_(98711, _n_(98708, "remove_column", lambda: remove_column), _n_(98709, "list2", lambda: list2), _n_(98710, "n", lambda: n)))
_l_(98713)