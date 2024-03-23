# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_column(nums, n):
    _l_(98590)

    for i in _n_(98585, "nums", lambda: nums):
        _l_(98587)

        del i[n]
        _l_(98586)
    aux = _n_(98588, "nums", lambda: nums)
    _l_(98589)
    return aux
n = 0
_l_(98591)
_c_(98593, _n_(98592, "print", lambda: print), 'Original Nested list:')
_l_(98594)
_c_(98597, _n_(98595, "print", lambda: print), _n_(98596, "list1", lambda: list1))
_l_(98598)
_c_(98600, _n_(98599, "print", lambda: print), 'After removing 1st column:')
_l_(98601)
_c_(98607, _n_(98602, "print", lambda: print), _c_(98606, _n_(98603, "remove_column", lambda: remove_column), _n_(98604, "list1", lambda: list1), _n_(98605, "n", lambda: n)))
_l_(98608)
list2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
_l_(98609)
n = 2
_l_(98610)
_c_(98612, _n_(98611, "print", lambda: print), '\nOriginal Nested list:')
_l_(98613)
_c_(98616, _n_(98614, "print", lambda: print), _n_(98615, "list2", lambda: list2))
_l_(98617)
_c_(98619, _n_(98618, "print", lambda: print), 'After removing 3rd column:')
_l_(98620)
_c_(98626, _n_(98621, "print", lambda: print), _c_(98625, _n_(98622, "remove_column", lambda: remove_column), _n_(98623, "list2", lambda: list2), _n_(98624, "n", lambda: n)))
_l_(98627)