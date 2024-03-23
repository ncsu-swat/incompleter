# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sort_matrix(M):
    _l_(97876)

    result = _c_(97872, _n_(97867, "sorted", lambda: sorted), _n_(97868, "M", lambda: M), key=lambda matrix_row: _c_(97871, _n_(97869, "sum", lambda: sum), _n_(97870, "matrix_row", lambda: matrix_row)))
    _l_(97873)
    aux = _n_(97874, "result", lambda: result)
    _l_(97875)
    return aux
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
_l_(97877)
_c_(97879, _n_(97878, "print", lambda: print), 'Original Matrix:')
_l_(97880)
_c_(97883, _n_(97881, "print", lambda: print), _n_(97882, "matrix1", lambda: matrix1))
_l_(97884)
_c_(97886, _n_(97885, "print", lambda: print), '\nSort the said matrix in ascending order according to the sum of its rows')
_l_(97887)
_c_(97892, _n_(97888, "print", lambda: print), _c_(97891, _n_(97889, "sort_matrix", lambda: sort_matrix), _n_(97890, "matrix1", lambda: matrix1)))
_l_(97893)
_c_(97895, _n_(97894, "print", lambda: print), '\nOriginal Matrix:')
_l_(97896)
_c_(97899, _n_(97897, "print", lambda: print), _n_(97898, "matrix2", lambda: matrix2))
_l_(97900)
_c_(97902, _n_(97901, "print", lambda: print), '\nSort the said matrix in ascending order according to the sum of its rows')
_l_(97903)
_c_(97908, _n_(97904, "print", lambda: print), _c_(97907, _n_(97905, "sort_matrix", lambda: sort_matrix), _n_(97906, "matrix2", lambda: matrix2)))
_l_(97909)