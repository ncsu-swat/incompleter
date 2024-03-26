# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import *
    _l_(104643)

except ImportError:
    pass
array_num = _c_(104645, _n_(104644, "array", lambda: array), 'i', [])
_l_(104646)
_c_(104651, _n_(104647, "print", lambda: print), 'Items in the list: ' + _c_(104650, _n_(104648, "str", lambda: str), _n_(104649, "num_list", lambda: num_list)))
_l_(104652)
_c_(104654, _n_(104653, "print", lambda: print), 'Append items from the list: ')
_l_(104655)
_c_(104659, _a_(104657, _n_(104656, "array_num", lambda: array_num), "fromlist"), _n_(104658, "num_list", lambda: num_list))
_l_(104660)
_c_(104665, _n_(104661, "print", lambda: print), 'Items in the array: ' + _c_(104664, _n_(104662, "str", lambda: str), _n_(104663, "array_num", lambda: array_num)))
_l_(104666)