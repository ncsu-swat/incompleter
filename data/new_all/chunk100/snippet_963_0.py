# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(96917)

except ImportError:
    pass

def sum_matrix_Elements(m):
    _l_(96950)

    element_sum = 0
    _l_(96918)
    for p in _c_(96923, _n_(96919, "range", lambda: range), _c_(96922, _n_(96920, "len", lambda: len), _n_(96921, "arra", lambda: arra))):
        _l_(96947)

        for q in _c_(96929, _n_(96924, "range", lambda: range), _c_(96928, _n_(96925, "len", lambda: len), _n_(96926, "arra", lambda: arra)[_n_(96927, "p", lambda: p)])):
            _l_(96946)

            if _n_(96930, "arra", lambda: arra)[_n_(96931, "p", lambda: p)][_n_(96932, "q", lambda: q)] == 0 and _n_(96933, "p", lambda: p) < _c_(96936, _n_(96934, "len", lambda: len), _n_(96935, "arra", lambda: arra)) - 1:
                _l_(96941)

                _n_(96937, "arra", lambda: arra)[_n_(96938, "p", lambda: p) + 1][_n_(96939, "q", lambda: q)] = 0
                _l_(96940)
            element_sum += _n_(96942, "arra", lambda: arra)[_n_(96943, "p", lambda: p)][_n_(96944, "q", lambda: q)]
            _l_(96945)
    aux = _n_(96948, "element_sum", lambda: element_sum)
    _l_(96949)
    return aux
m = [[1, 1, 0, 2], [0, 3, 0, 3], [1, 0, 4, 4]]
_l_(96951)
_c_(96953, _n_(96952, "print", lambda: print), 'Original matrix:')
_l_(96954)
_c_(96957, _n_(96955, "print", lambda: print), _n_(96956, "m", lambda: m))
_l_(96958)
_c_(96960, _n_(96959, "print", lambda: print), 'Sum:')
_l_(96961)
_c_(96966, _n_(96962, "print", lambda: print), _c_(96965, _n_(96963, "sum_matrix_Elements", lambda: sum_matrix_Elements), _n_(96964, "m", lambda: m)))
_l_(96967)