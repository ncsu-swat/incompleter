# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from array import *
    _l_(15714)

except ImportError:
    pass
array_num = _c_(15716, _n_(15715, "array", lambda: array), 'i', [])
_l_(15717)
_c_(15722, _n_(15718, "print", lambda: print), 'Items in the list: ' + _c_(15721, _n_(15719, "str", lambda: str), _n_(15720, "num_list", lambda: num_list)))
_l_(15723)
_c_(15725, _n_(15724, "print", lambda: print), 'Append items from the list: ')
_l_(15726)
_c_(15730, _a_(15728, _n_(15727, "array_num", lambda: array_num), "fromlist"), _n_(15729, "num_list", lambda: num_list))
_l_(15731)
_c_(15736, _n_(15732, "print", lambda: print), 'Items in the array: ' + _c_(15735, _n_(15733, "str", lambda: str), _n_(15734, "array_num", lambda: array_num)))
_l_(15737)