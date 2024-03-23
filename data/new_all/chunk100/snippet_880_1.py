# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(86479)

except ImportError:
    pass
y = _c_(86488, _a_(86481, _n_(86480, "np", lambda: np), "array"), [[1, 2, 3], [_a_(86483, _n_(86482, "np", lambda: np), "nan"), 0, _a_(86485, _n_(86484, "np", lambda: np), "nan")], [6, 7, _a_(86487, _n_(86486, "np", lambda: np), "nan")]])
_l_(86489)
_c_(86491, _n_(86490, "print", lambda: print), 'Original array:')
_l_(86492)
_c_(86495, _n_(86493, "print", lambda: print), _n_(86494, "x", lambda: x))
_l_(86496)
_c_(86498, _n_(86497, "print", lambda: print), 'After removing nan values:')
_l_(86499)
result = _n_(86500, "x", lambda: x)[_c_(86507, _a_(86502, _n_(86501, "np", lambda: np), "logical_not"), _c_(86506, _a_(86504, _n_(86503, "np", lambda: np), "isnan"), _n_(86505, "x", lambda: x)))]
_l_(86508)
_c_(86511, _n_(86509, "print", lambda: print), _n_(86510, "result", lambda: result))
_l_(86512)
_c_(86514, _n_(86513, "print", lambda: print), '\nOriginal array:')
_l_(86515)
_c_(86518, _n_(86516, "print", lambda: print), _n_(86517, "y", lambda: y))
_l_(86519)
_c_(86521, _n_(86520, "print", lambda: print), 'After removing nan values:')
_l_(86522)
result = _n_(86523, "y", lambda: y)[_c_(86530, _a_(86525, _n_(86524, "np", lambda: np), "logical_not"), _c_(86529, _a_(86527, _n_(86526, "np", lambda: np), "isnan"), _n_(86528, "y", lambda: y)))]
_l_(86531)
_c_(86534, _n_(86532, "print", lambda: print), _n_(86533, "result", lambda: result))
_l_(86535)