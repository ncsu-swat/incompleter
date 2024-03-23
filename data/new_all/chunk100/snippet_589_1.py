# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict, Counter
    _l_(61653)

except ImportError:
    pass
str1 = 'w3resource'
_l_(61654)
for letter in _n_(61655, "str1", lambda: str1):
    _l_(61663)

    _n_(61656, "my_dict", lambda: my_dict)[_n_(61657, "letter", lambda: letter)] = _c_(61661, _a_(61659, _n_(61658, "my_dict", lambda: my_dict), "get"), _n_(61660, "letter", lambda: letter), 0) + 1
    _l_(61662)
_c_(61666, _n_(61664, "print", lambda: print), _n_(61665, "my_dict", lambda: my_dict))
_l_(61667)