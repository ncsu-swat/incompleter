# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def remove_column(nums, n):
    _l_(98547)

    for i in _n_(98542, "nums", lambda: nums):
        _l_(98544)

        del i[n]
        _l_(98543)
    aux = _n_(98545, "nums", lambda: nums)
    _l_(98546)
    return aux
list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
_l_(98548)
n = 0
_l_(98549)
_c_(98551, _n_(98550, "print", lambda: print), 'Original Nested list:')
_l_(98552)
_c_(98555, _n_(98553, "print", lambda: print), _n_(98554, "list1", lambda: list1))
_l_(98556)
_c_(98558, _n_(98557, "print", lambda: print), 'After removing 1st column:')
_l_(98559)
_c_(98565, _n_(98560, "print", lambda: print), _c_(98564, _n_(98561, "remove_column", lambda: remove_column), _n_(98562, "list1", lambda: list1), _n_(98563, "n", lambda: n)))
_l_(98566)
list2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
_l_(98567)
_c_(98569, _n_(98568, "print", lambda: print), '\nOriginal Nested list:')
_l_(98570)
_c_(98573, _n_(98571, "print", lambda: print), _n_(98572, "list2", lambda: list2))
_l_(98574)
_c_(98576, _n_(98575, "print", lambda: print), 'After removing 3rd column:')
_l_(98577)
_c_(98583, _n_(98578, "print", lambda: print), _c_(98582, _n_(98579, "remove_column", lambda: remove_column), _n_(98580, "list2", lambda: list2), _n_(98581, "n", lambda: n)))
_l_(98584)