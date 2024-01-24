# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60288895/lambda-and-typeerror-module-object-is-not-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import random
    _l_(400733)

except ImportError:
    pass
try:
    from string import ascii_letters
    _l_(400735)

except ImportError:
    pass

choice = lambda x: _n_(400736, "x", lambda: x)[_c_(400743, _n_(400737, "int", lambda: int), _c_(400739, _n_(400738, "random", lambda: random))* _c_(400742, _n_(400740, "len", lambda: len), _n_(400741, "x", lambda: x)))]
_l_(400744)

_c_(400748, _n_(400745, "print", lambda: print), _c_(400747, _n_(400746, "choice", lambda: choice), "azerty"))
_l_(400749)