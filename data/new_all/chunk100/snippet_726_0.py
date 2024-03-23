# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from heapq import nlargest
    _l_(73665)

except ImportError:
    pass
three_largest = _c_(73670, _n_(73666, "nlargest", lambda: nlargest), 3, _n_(73667, "my_dict", lambda: my_dict), key=_a_(73669, _n_(73668, "my_dict", lambda: my_dict), "get"))
_l_(73671)
_c_(73674, _n_(73672, "print", lambda: print), _n_(73673, "three_largest", lambda: three_largest))
_l_(73675)