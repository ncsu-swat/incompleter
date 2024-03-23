# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sum_column(nums, C):
    _l_(69721)

    result = _c_(69717, _n_(69713, "sum", lambda: sum), (_n_(69714, "row", lambda: row)[_n_(69715, "C", lambda: C)] for row in _n_(69716, "nums", lambda: nums)))
    _l_(69718)
    aux = _n_(69719, "result", lambda: result)
    _l_(69720)
    return aux
nums = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
_l_(69722)
_c_(69724, _n_(69723, "print", lambda: print), 'Original list of lists:')
_l_(69725)
_c_(69728, _n_(69726, "print", lambda: print), _n_(69727, "nums", lambda: nums))
_l_(69729)
_c_(69731, _n_(69730, "print", lambda: print), '\nSum: 1st column of the said list of lists:')
_l_(69732)
_c_(69738, _n_(69733, "print", lambda: print), _c_(69737, _n_(69734, "sum_column", lambda: sum_column), _n_(69735, "nums", lambda: nums), _n_(69736, "column", lambda: column)))
_l_(69739)
column = 1
_l_(69740)
_c_(69742, _n_(69741, "print", lambda: print), '\nSum: 2nd column of the said list of lists:')
_l_(69743)
_c_(69749, _n_(69744, "print", lambda: print), _c_(69748, _n_(69745, "sum_column", lambda: sum_column), _n_(69746, "nums", lambda: nums), _n_(69747, "column", lambda: column)))
_l_(69750)
column = 3
_l_(69751)
_c_(69753, _n_(69752, "print", lambda: print), '\nSum: 4th column of the said list of lists:')
_l_(69754)
_c_(69760, _n_(69755, "print", lambda: print), _c_(69759, _n_(69756, "sum_column", lambda: sum_column), _n_(69757, "nums", lambda: nums), _n_(69758, "column", lambda: column)))
_l_(69761)