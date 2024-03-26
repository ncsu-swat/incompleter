# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(112973)

except ImportError:
    pass
x = _c_(112978, _a_(112975, _n_(112974, "np", lambda: np), "array"), [1.0, 2.0, 3.0, 4.0], _a_(112977, _n_(112976, "np", lambda: np), "float32"))
_l_(112979)
_c_(112981, _n_(112980, "print", lambda: print), 'Original array: ')
_l_(112982)
_c_(112985, _n_(112983, "print", lambda: print), _n_(112984, "x", lambda: x))
_l_(112986)
_c_(112988, _n_(112987, "print", lambda: print), '\n2^p for all the elements of the said array:')
_l_(112989)
r1 = _c_(112993, _a_(112991, _n_(112990, "np", lambda: np), "exp2"), _n_(112992, "x", lambda: x))
_l_(112994)
assert _c_(112999, _a_(112996, _n_(112995, "np", lambda: np), "allclose"), _n_(112997, "r1", lambda: r1), _n_(112998, "r2", lambda: r2))
_l_(113000)
_c_(113003, _n_(113001, "print", lambda: print), _n_(113002, "r1", lambda: r1))
_l_(113004)