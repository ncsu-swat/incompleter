# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import types
    _l_(1546870)

except ImportError:
    pass

def func(_static=_c_(1546873, _a_(1546872, _n_(1546871, "types", lambda: types), "SimpleNamespace"), counter=0)):
    _l_(1546881)

    _n_(1546874, "_static", lambda: _static).counter += 1
    _l_(1546875)
    _c_(1546879, _n_(1546876, "print", lambda: print), _a_(1546878, _n_(1546877, "_static", lambda: _static), "counter"))
    _l_(1546880)

