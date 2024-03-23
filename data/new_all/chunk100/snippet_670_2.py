# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sum_column(nums, C):
    _l_(69628)

    result = _c_(69624, _n_(69620, "sum", lambda: sum), (_n_(69621, "row", lambda: row)[_n_(69622, "C", lambda: C)] for row in _n_(69623, "nums", lambda: nums)))
    _l_(69625)
    aux = _n_(69626, "result", lambda: result)
    _l_(69627)
    return aux
nums = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
_l_(69629)
_c_(69631, _n_(69630, "print", lambda: print), 'Original list of lists:')
_l_(69632)
_c_(69635, _n_(69633, "print", lambda: print), _n_(69634, "nums", lambda: nums))
_l_(69636)
column = 0
_l_(69637)
_c_(69639, _n_(69638, "print", lambda: print), '\nSum: 1st column of the said list of lists:')
_l_(69640)
_c_(69646, _n_(69641, "print", lambda: print), _c_(69645, _n_(69642, "sum_column", lambda: sum_column), _n_(69643, "nums", lambda: nums), _n_(69644, "column", lambda: column)))
_l_(69647)
_c_(69649, _n_(69648, "print", lambda: print), '\nSum: 2nd column of the said list of lists:')
_l_(69650)
_c_(69656, _n_(69651, "print", lambda: print), _c_(69655, _n_(69652, "sum_column", lambda: sum_column), _n_(69653, "nums", lambda: nums), _n_(69654, "column", lambda: column)))
_l_(69657)
column = 3
_l_(69658)
_c_(69660, _n_(69659, "print", lambda: print), '\nSum: 4th column of the said list of lists:')
_l_(69661)
_c_(69667, _n_(69662, "print", lambda: print), _c_(69666, _n_(69663, "sum_column", lambda: sum_column), _n_(69664, "nums", lambda: nums), _n_(69665, "column", lambda: column)))
_l_(69668)