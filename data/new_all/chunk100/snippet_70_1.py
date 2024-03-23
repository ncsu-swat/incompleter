# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(72450)

except ImportError:
    pass
str = 'abcd'
_l_(72451)
_c_(72453, _n_(72452, "print", lambda: print), 'Orginal list of strings:')
_l_(72454)
_c_(72457, _n_(72455, "print", lambda: print), _n_(72456, "texts", lambda: texts))
_l_(72458)
result = _c_(72469, _n_(72459, "list", lambda: list), _c_(72468, _n_(72460, "filter", lambda: filter), lambda x: _c_(72463, _n_(72461, "Counter", lambda: Counter), _n_(72462, "str", lambda: str)) == _c_(72466, _n_(72464, "Counter", lambda: Counter), _n_(72465, "x", lambda: x)), _n_(72467, "texts", lambda: texts)))
_l_(72470)
_c_(72472, _n_(72471, "print", lambda: print), "\nAnagrams of 'abcd' in the above string: ")
_l_(72473)
_c_(72476, _n_(72474, "print", lambda: print), _n_(72475, "result", lambda: result))
_l_(72477)