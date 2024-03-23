# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sort_matrix(M):
    _l_(84042)

    result = _c_(84038, _n_(84035, "sorted", lambda: sorted), _n_(84036, "M", lambda: M), key=_n_(84037, "sum", lambda: sum))
    _l_(84039)
    aux = _n_(84040, "result", lambda: result)
    _l_(84041)
    return aux
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
_l_(84043)
_c_(84045, _n_(84044, "print", lambda: print), 'Original Matrix:')
_l_(84046)
_c_(84049, _n_(84047, "print", lambda: print), _n_(84048, "matrix1", lambda: matrix1))
_l_(84050)
_c_(84052, _n_(84051, "print", lambda: print), '\nSort the said matrix in ascending order according to the sum of its rows')
_l_(84053)
_c_(84058, _n_(84054, "print", lambda: print), _c_(84057, _n_(84055, "sort_matrix", lambda: sort_matrix), _n_(84056, "matrix1", lambda: matrix1)))
_l_(84059)
_c_(84061, _n_(84060, "print", lambda: print), '\nOriginal Matrix:')
_l_(84062)
_c_(84065, _n_(84063, "print", lambda: print), _n_(84064, "matrix2", lambda: matrix2))
_l_(84066)
_c_(84068, _n_(84067, "print", lambda: print), '\nSort the said matrix in ascending order according to the sum of its rows')
_l_(84069)
_c_(84074, _n_(84070, "print", lambda: print), _c_(84073, _n_(84071, "sort_matrix", lambda: sort_matrix), _n_(84072, "matrix2", lambda: matrix2)))
_l_(84075)