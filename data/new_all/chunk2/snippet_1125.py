# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/66701388/typeerror-unsupported-operand-types-for-float-and-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import math
    _l_(445309)

except ImportError:
    pass
phi = _c_(445312, _a_(445311, _n_(445310, "math", lambda: math), "sqrt"), 5) / 2
_l_(445313)
pi = (802 * _n_(445314, "phi", lambda: phi) - 801) / (602 * _n_(445315, "phi", lambda: phi) - 601)
_l_(445316)
pi = _c_(445319, _n_(445317, "round", lambda: round), _n_(445318, "pi", lambda: pi) ^ 4)
_l_(445320)
_c_(445323, _n_(445321, "print", lambda: print), "Pi is equivalent to", _n_(445322, "pi", lambda: pi))
_l_(445324)