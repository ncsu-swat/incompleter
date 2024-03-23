# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
list1 = [[1, 3], [5, 7], [9, 11]]
_l_(65425)
list2 = [[2, 4], [6, 8], [10, 12, 14]]
_l_(65426)
_c_(65428, _n_(65427, "print", lambda: print), 'Original lists:')
_l_(65429)
_c_(65432, _n_(65430, "print", lambda: print), _n_(65431, "list1", lambda: list1))
_l_(65433)
_c_(65436, _n_(65434, "print", lambda: print), _n_(65435, "list2", lambda: list2))
_l_(65437)
_c_(65442, _n_(65438, "print", lambda: print), '\nZipped list:\n' + _c_(65441, _n_(65439, "str", lambda: str), _n_(65440, "result", lambda: result)))
_l_(65443)