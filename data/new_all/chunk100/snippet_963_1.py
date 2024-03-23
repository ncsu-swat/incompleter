# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(96969)

except ImportError:
    pass

def sum_matrix_Elements(m):
    _l_(97007)

    arra = _c_(96973, _a_(96971, _n_(96970, "np", lambda: np), "array"), _n_(96972, "m", lambda: m))
    _l_(96974)
    element_sum = 0
    _l_(96975)
    for p in _c_(96980, _n_(96976, "range", lambda: range), _c_(96979, _n_(96977, "len", lambda: len), _n_(96978, "arra", lambda: arra))):
        _l_(97004)

        for q in _c_(96986, _n_(96981, "range", lambda: range), _c_(96985, _n_(96982, "len", lambda: len), _n_(96983, "arra", lambda: arra)[_n_(96984, "p", lambda: p)])):
            _l_(97003)

            if _n_(96987, "arra", lambda: arra)[_n_(96988, "p", lambda: p)][_n_(96989, "q", lambda: q)] == 0 and _n_(96990, "p", lambda: p) < _c_(96993, _n_(96991, "len", lambda: len), _n_(96992, "arra", lambda: arra)) - 1:
                _l_(96998)

                _n_(96994, "arra", lambda: arra)[_n_(96995, "p", lambda: p) + 1][_n_(96996, "q", lambda: q)] = 0
                _l_(96997)
            element_sum += _n_(96999, "arra", lambda: arra)[_n_(97000, "p", lambda: p)][_n_(97001, "q", lambda: q)]
            _l_(97002)
    aux = _n_(97005, "element_sum", lambda: element_sum)
    _l_(97006)
    return aux
_c_(97009, _n_(97008, "print", lambda: print), 'Original matrix:')
_l_(97010)
_c_(97013, _n_(97011, "print", lambda: print), _n_(97012, "m", lambda: m))
_l_(97014)
_c_(97016, _n_(97015, "print", lambda: print), 'Sum:')
_l_(97017)
_c_(97022, _n_(97018, "print", lambda: print), _c_(97021, _n_(97019, "sum_matrix_Elements", lambda: sum_matrix_Elements), _n_(97020, "m", lambda: m)))
_l_(97023)