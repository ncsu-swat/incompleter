# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sum_column(nums, C):
    _l_(69530)

    result = _c_(69526, _n_(69522, "sum", lambda: sum), (_n_(69523, "row", lambda: row)[_n_(69524, "C", lambda: C)] for row in _n_(69525, "nums", lambda: nums)))
    _l_(69527)
    aux = _n_(69528, "result", lambda: result)
    _l_(69529)
    return aux
nums = [[1, 2, 3, 2], [4, 5, 6, 2], [7, 8, 9, 5]]
_l_(69531)
_c_(69533, _n_(69532, "print", lambda: print), 'Original list of lists:')
_l_(69534)
_c_(69537, _n_(69535, "print", lambda: print), _n_(69536, "nums", lambda: nums))
_l_(69538)
column = 0
_l_(69539)
_c_(69541, _n_(69540, "print", lambda: print), '\nSum: 1st column of the said list of lists:')
_l_(69542)
_c_(69548, _n_(69543, "print", lambda: print), _c_(69547, _n_(69544, "sum_column", lambda: sum_column), _n_(69545, "nums", lambda: nums), _n_(69546, "column", lambda: column)))
_l_(69549)
column = 1
_l_(69550)
_c_(69552, _n_(69551, "print", lambda: print), '\nSum: 2nd column of the said list of lists:')
_l_(69553)
_c_(69559, _n_(69554, "print", lambda: print), _c_(69558, _n_(69555, "sum_column", lambda: sum_column), _n_(69556, "nums", lambda: nums), _n_(69557, "column", lambda: column)))
_l_(69560)
_c_(69562, _n_(69561, "print", lambda: print), '\nSum: 4th column of the said list of lists:')
_l_(69563)
_c_(69569, _n_(69564, "print", lambda: print), _c_(69568, _n_(69565, "sum_column", lambda: sum_column), _n_(69566, "nums", lambda: nums), _n_(69567, "column", lambda: column)))
_l_(69570)