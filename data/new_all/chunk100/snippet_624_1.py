# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
list1 = [[1, 3], [5, 7], [9, 11]]
_l_(65444)
_c_(65446, _n_(65445, "print", lambda: print), 'Original lists:')
_l_(65447)
_c_(65450, _n_(65448, "print", lambda: print), _n_(65449, "list1", lambda: list1))
_l_(65451)
_c_(65454, _n_(65452, "print", lambda: print), _n_(65453, "list2", lambda: list2))
_l_(65455)
result = _c_(65463, _n_(65456, "list", lambda: list), _c_(65462, _n_(65457, "map", lambda: map), _a_(65459, _n_(65458, "list", lambda: list), "__add__"), _n_(65460, "list1", lambda: list1), _n_(65461, "list2", lambda: list2)))
_l_(65464)
_c_(65469, _n_(65465, "print", lambda: print), '\nZipped list:\n' + _c_(65468, _n_(65466, "str", lambda: str), _n_(65467, "result", lambda: result)))
_l_(65470)