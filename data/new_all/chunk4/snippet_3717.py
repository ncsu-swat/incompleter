# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69343020/cython-attribute-error-classes-vec-object-has-no-attribute-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pyximport; 
    _l_(638995)

except ImportError:
    pass
try:
    from Classes import line, Vec
    _l_(638997)

except ImportError:
    pass

L = _c_(639003, _n_(638998, "line", lambda: line), _c_(639000, _n_(638999, "Vec", lambda: Vec), 0,0,4), _c_(639002, _n_(639001, "Vec", lambda: Vec), 5,6,6))
_l_(639004)