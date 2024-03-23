# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import Counter
    _l_(72479)

except ImportError:
    pass
texts = ['bcda', 'abce', 'cbda', 'cbea', 'adcb']
_l_(72480)
_c_(72482, _n_(72481, "print", lambda: print), 'Orginal list of strings:')
_l_(72483)
_c_(72486, _n_(72484, "print", lambda: print), _n_(72485, "texts", lambda: texts))
_l_(72487)
result = _c_(72498, _n_(72488, "list", lambda: list), _c_(72497, _n_(72489, "filter", lambda: filter), lambda x: _c_(72492, _n_(72490, "Counter", lambda: Counter), _n_(72491, "str", lambda: str)) == _c_(72495, _n_(72493, "Counter", lambda: Counter), _n_(72494, "x", lambda: x)), _n_(72496, "texts", lambda: texts)))
_l_(72499)
_c_(72501, _n_(72500, "print", lambda: print), "\nAnagrams of 'abcd' in the above string: ")
_l_(72502)
_c_(72505, _n_(72503, "print", lambda: print), _n_(72504, "result", lambda: result))
_l_(72506)