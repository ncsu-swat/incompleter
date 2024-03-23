# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
list2 = [[2, 4], [6, 8], [10, 12, 14]]
_l_(65471)
_c_(65473, _n_(65472, "print", lambda: print), 'Original lists:')
_l_(65474)
_c_(65477, _n_(65475, "print", lambda: print), _n_(65476, "list1", lambda: list1))
_l_(65478)
_c_(65481, _n_(65479, "print", lambda: print), _n_(65480, "list2", lambda: list2))
_l_(65482)
result = _c_(65490, _n_(65483, "list", lambda: list), _c_(65489, _n_(65484, "map", lambda: map), _a_(65486, _n_(65485, "list", lambda: list), "__add__"), _n_(65487, "list1", lambda: list1), _n_(65488, "list2", lambda: list2)))
_l_(65491)
_c_(65496, _n_(65492, "print", lambda: print), '\nZipped list:\n' + _c_(65495, _n_(65493, "str", lambda: str), _n_(65494, "result", lambda: result)))
_l_(65497)