# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import *
    _l_(104620)

except ImportError:
    pass
num_list = [1, 2, 6, -8]
_l_(104621)
_c_(104626, _n_(104622, "print", lambda: print), 'Items in the list: ' + _c_(104625, _n_(104623, "str", lambda: str), _n_(104624, "num_list", lambda: num_list)))
_l_(104627)
_c_(104629, _n_(104628, "print", lambda: print), 'Append items from the list: ')
_l_(104630)
_c_(104634, _a_(104632, _n_(104631, "array_num", lambda: array_num), "fromlist"), _n_(104633, "num_list", lambda: num_list))
_l_(104635)
_c_(104640, _n_(104636, "print", lambda: print), 'Items in the array: ' + _c_(104639, _n_(104637, "str", lambda: str), _n_(104638, "array_num", lambda: array_num)))
_l_(104641)