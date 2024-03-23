# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sort_matrix(M):
    _l_(97956)

    result = _c_(97952, _n_(97947, "sorted", lambda: sorted), _n_(97948, "M", lambda: M), key=lambda matrix_row: _c_(97951, _n_(97949, "sum", lambda: sum), _n_(97950, "matrix_row", lambda: matrix_row)))
    _l_(97953)
    aux = _n_(97954, "result", lambda: result)
    _l_(97955)
    return aux
matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
_l_(97957)
_c_(97959, _n_(97958, "print", lambda: print), 'Original Matrix:')
_l_(97960)
_c_(97963, _n_(97961, "print", lambda: print), _n_(97962, "matrix1", lambda: matrix1))
_l_(97964)
_c_(97966, _n_(97965, "print", lambda: print), '\nSort the said matrix in ascending order according to the sum of its rows')
_l_(97967)
_c_(97972, _n_(97968, "print", lambda: print), _c_(97971, _n_(97969, "sort_matrix", lambda: sort_matrix), _n_(97970, "matrix1", lambda: matrix1)))
_l_(97973)
_c_(97975, _n_(97974, "print", lambda: print), '\nOriginal Matrix:')
_l_(97976)
_c_(97979, _n_(97977, "print", lambda: print), _n_(97978, "matrix2", lambda: matrix2))
_l_(97980)
_c_(97982, _n_(97981, "print", lambda: print), '\nSort the said matrix in ascending order according to the sum of its rows')
_l_(97983)
_c_(97988, _n_(97984, "print", lambda: print), _c_(97987, _n_(97985, "sort_matrix", lambda: sort_matrix), _n_(97986, "matrix2", lambda: matrix2)))
_l_(97989)