# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import *
    _l_(15691)

except ImportError:
    pass
num_list = [1, 2, 6, -8]
_l_(15692)
_c_(15697, _n_(15693, "print", lambda: print), 'Items in the list: ' + _c_(15696, _n_(15694, "str", lambda: str), _n_(15695, "num_list", lambda: num_list)))
_l_(15698)
_c_(15700, _n_(15699, "print", lambda: print), 'Append items from the list: ')
_l_(15701)
_c_(15705, _a_(15703, _n_(15702, "array_num", lambda: array_num), "fromlist"), _n_(15704, "num_list", lambda: num_list))
_l_(15706)
_c_(15711, _n_(15707, "print", lambda: print), 'Items in the array: ' + _c_(15710, _n_(15708, "str", lambda: str), _n_(15709, "array_num", lambda: array_num)))
_l_(15712)