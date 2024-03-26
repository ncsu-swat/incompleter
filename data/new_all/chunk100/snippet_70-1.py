# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(119860)

except ImportError:
    pass
str = 'abcd'
_l_(119861)
_c_(119863, _n_(119862, "print", lambda: print), 'Orginal list of strings:')
_l_(119864)
_c_(119867, _n_(119865, "print", lambda: print), _n_(119866, "texts", lambda: texts))
_l_(119868)
result = _c_(119879, _n_(119869, "list", lambda: list), _c_(119878, _n_(119870, "filter", lambda: filter), lambda x: _c_(119873, _n_(119871, "Counter", lambda: Counter), _n_(119872, "str", lambda: str)) == _c_(119876, _n_(119874, "Counter", lambda: Counter), _n_(119875, "x", lambda: x)), _n_(119877, "texts", lambda: texts)))
_l_(119880)
_c_(119882, _n_(119881, "print", lambda: print), "\nAnagrams of 'abcd' in the above string: ")
_l_(119883)
_c_(119886, _n_(119884, "print", lambda: print), _n_(119885, "result", lambda: result))
_l_(119887)