# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(1548816)

except ImportError:
    pass
try:
    import string
    _l_(1548818)

except ImportError:
    pass

if _n_(1548819, "__name__", lambda: __name__) == '__main__':
    _l_(1548839)

    length = 16
    _l_(1548820)
    a = _c_(1548831, _a_(1548823, _a_(1548822, _n_(1548821, "np", lambda: np), "random"), "choice"), _c_(1548829, _n_(1548824, "list", lambda: list), _a_(1548826, _n_(1548825, "string", lambda: string), "ascii_uppercase") + _a_(1548828, _n_(1548827, "string", lambda: string), "digits")), _n_(1548830, "length", lambda: length))                
    _l_(1548832)                
    _c_(1548837, _n_(1548833, "print", lambda: print), _c_(1548836, _a_(1548834, '', "join"), _n_(1548835, "a", lambda: a)))
    _l_(1548838)

