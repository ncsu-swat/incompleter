# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/10580676/comparing-two-numpy-arrays-for-equality-element-wise
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(64884)

except ImportError:
    pass
a = _c_(64887, _a_(64886, _n_(64885, "np", lambda: np), "arange"), 0.0, 10.2, 0.12)
_l_(64888)
b = _c_(64891, _a_(64890, _n_(64889, "np", lambda: np), "arange"), 0.0, 10.2, 0.12)
_l_(64892)
ap = _c_(64896, _a_(64894, _n_(64893, "pd", lambda: pd), "DataFrame"), _n_(64895, "a", lambda: a))
_l_(64897)
bp = _c_(64901, _a_(64899, _n_(64898, "pd", lambda: pd), "DataFrame"), _n_(64900, "b", lambda: b))
_l_(64902)

_c_(64906, _a_(64904, _n_(64903, "ap", lambda: ap), "equals"), _n_(64905, "bp", lambda: bp))
_l_(64907)
True
_l_(64908)

_c_(64912, _n_(64909, "identical", lambda: identical), _n_(64910, "iris1", lambda: iris1), _n_(64911, "iris2", lambda: iris2))
_l_(64913)
#[1] TRUE
_c_(64918, _a_(64915, _n_(64914, "all", lambda: all), "equal"), _n_(64916, "array1", lambda: array1), _n_(64917, "array2", lambda: array2))
_l_(64919)
#> [1] TRUE 

