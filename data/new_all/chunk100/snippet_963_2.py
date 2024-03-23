# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(97025)

except ImportError:
    pass

def sum_matrix_Elements(m):
    _l_(97062)

    arra = _c_(97029, _a_(97027, _n_(97026, "np", lambda: np), "array"), _n_(97028, "m", lambda: m))
    _l_(97030)
    for p in _c_(97035, _n_(97031, "range", lambda: range), _c_(97034, _n_(97032, "len", lambda: len), _n_(97033, "arra", lambda: arra))):
        _l_(97059)

        for q in _c_(97041, _n_(97036, "range", lambda: range), _c_(97040, _n_(97037, "len", lambda: len), _n_(97038, "arra", lambda: arra)[_n_(97039, "p", lambda: p)])):
            _l_(97058)

            if _n_(97042, "arra", lambda: arra)[_n_(97043, "p", lambda: p)][_n_(97044, "q", lambda: q)] == 0 and _n_(97045, "p", lambda: p) < _c_(97048, _n_(97046, "len", lambda: len), _n_(97047, "arra", lambda: arra)) - 1:
                _l_(97053)

                _n_(97049, "arra", lambda: arra)[_n_(97050, "p", lambda: p) + 1][_n_(97051, "q", lambda: q)] = 0
                _l_(97052)
            element_sum += _n_(97054, "arra", lambda: arra)[_n_(97055, "p", lambda: p)][_n_(97056, "q", lambda: q)]
            _l_(97057)
    aux = _n_(97060, "element_sum", lambda: element_sum)
    _l_(97061)
    return aux
m = [[1, 1, 0, 2], [0, 3, 0, 3], [1, 0, 4, 4]]
_l_(97063)
_c_(97065, _n_(97064, "print", lambda: print), 'Original matrix:')
_l_(97066)
_c_(97069, _n_(97067, "print", lambda: print), _n_(97068, "m", lambda: m))
_l_(97070)
_c_(97072, _n_(97071, "print", lambda: print), 'Sum:')
_l_(97073)
_c_(97078, _n_(97074, "print", lambda: print), _c_(97077, _n_(97075, "sum_matrix_Elements", lambda: sum_matrix_Elements), _n_(97076, "m", lambda: m)))
_l_(97079)