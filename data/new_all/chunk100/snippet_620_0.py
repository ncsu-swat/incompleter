# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(64861)

except ImportError:
    pass
a = _c_(64864, _a_(64863, _n_(64862, "np", lambda: np), "array"), [1, 2, 3])
_l_(64865)
b = _c_(64868, _a_(64867, _n_(64866, "np", lambda: np), "array"), [0, 1, 0])
_l_(64869)
_c_(64871, _n_(64870, "print", lambda: print), 'Original 1-d arrays:')
_l_(64872)
_c_(64875, _n_(64873, "print", lambda: print), _n_(64874, "a", lambda: a))
_l_(64876)
_c_(64879, _n_(64877, "print", lambda: print), _n_(64878, "b", lambda: b))
_l_(64880)
result = _c_(64885, _a_(64882, _n_(64881, "np", lambda: np), "einsum"), 'n,n', _n_(64883, "a", lambda: a), _n_(64884, "b", lambda: b))
_l_(64886)
_c_(64888, _n_(64887, "print", lambda: print), 'Einstein’s summation convention of the said arrays:')
_l_(64889)
_c_(64892, _n_(64890, "print", lambda: print), _n_(64891, "result", lambda: result))
_l_(64893)
x = _c_(64898, _a_(64897, _c_(64896, _a_(64895, _n_(64894, "np", lambda: np), "arange"), 9), "reshape"), 3, 3)
_l_(64899)
y = _c_(64904, _a_(64903, _c_(64902, _a_(64901, _n_(64900, "np", lambda: np), "arange"), 3, 12), "reshape"), 3, 3)
_l_(64905)
_c_(64907, _n_(64906, "print", lambda: print), 'Original Higher dimension:')
_l_(64908)
_c_(64911, _n_(64909, "print", lambda: print), _n_(64910, "x", lambda: x))
_l_(64912)
_c_(64915, _n_(64913, "print", lambda: print), _n_(64914, "y", lambda: y))
_l_(64916)
_c_(64918, _n_(64917, "print", lambda: print), 'Einstein’s summation convention of the said arrays:')
_l_(64919)
_c_(64922, _n_(64920, "print", lambda: print), _n_(64921, "result", lambda: result))
_l_(64923)