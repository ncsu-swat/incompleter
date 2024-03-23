# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def sort_matrix(M):
    _l_(84120)

    result = _c_(84116, _n_(84113, "sorted", lambda: sorted), _n_(84114, "M", lambda: M), key=_n_(84115, "sum", lambda: sum))
    _l_(84117)
    aux = _n_(84118, "result", lambda: result)
    _l_(84119)
    return aux
matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
_l_(84121)
_c_(84123, _n_(84122, "print", lambda: print), 'Original Matrix:')
_l_(84124)
_c_(84127, _n_(84125, "print", lambda: print), _n_(84126, "matrix1", lambda: matrix1))
_l_(84128)
_c_(84130, _n_(84129, "print", lambda: print), '\nSort the said matrix in ascending order according to the sum of its rows')
_l_(84131)
_c_(84136, _n_(84132, "print", lambda: print), _c_(84135, _n_(84133, "sort_matrix", lambda: sort_matrix), _n_(84134, "matrix1", lambda: matrix1)))
_l_(84137)
_c_(84139, _n_(84138, "print", lambda: print), '\nOriginal Matrix:')
_l_(84140)
_c_(84143, _n_(84141, "print", lambda: print), _n_(84142, "matrix2", lambda: matrix2))
_l_(84144)
_c_(84146, _n_(84145, "print", lambda: print), '\nSort the said matrix in ascending order according to the sum of its rows')
_l_(84147)
_c_(84152, _n_(84148, "print", lambda: print), _c_(84151, _n_(84149, "sort_matrix", lambda: sort_matrix), _n_(84150, "matrix2", lambda: matrix2)))
_l_(84153)