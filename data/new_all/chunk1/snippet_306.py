# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/32670223/profiling-numba-in-spyder-results-in-nameerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from numpy import array
    _l_(418496)

except ImportError:
    pass
try:
    from numba import jit
    _l_(418498)

except ImportError:
    pass

@_n_(418499, "jit", lambda: jit)
def test():
    _l_(418505)

    a = _c_(418501, _n_(418500, "array", lambda: array), [0,0])
    _l_(418502)
    aux = _n_(418503, "a", lambda: a)
    _l_(418504)
    return aux

blah = _c_(418507, _n_(418506, "test", lambda: test))
_l_(418508)