# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from collections import defaultdict, Counter
    _l_(61637)

except ImportError:
    pass
my_dict = {}
_l_(61638)
for letter in _n_(61639, "str1", lambda: str1):
    _l_(61647)

    _n_(61640, "my_dict", lambda: my_dict)[_n_(61641, "letter", lambda: letter)] = _c_(61645, _a_(61643, _n_(61642, "my_dict", lambda: my_dict), "get"), _n_(61644, "letter", lambda: letter), 0) + 1
    _l_(61646)
_c_(61650, _n_(61648, "print", lambda: print), _n_(61649, "my_dict", lambda: my_dict))
_l_(61651)