# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(79425)

except ImportError:
    pass
_c_(79428, _a_(79427, _n_(79426, "pd", lambda: pd), "set_option"), 'display.max_rows', None)
_l_(79429)
_c_(79431, _n_(79430, "print", lambda: print), 'Original Orders DataFrame:')
_l_(79432)
_c_(79435, _n_(79433, "print", lambda: print), _n_(79434, "df", lambda: df))
_l_(79436)
_c_(79438, _n_(79437, "print", lambda: print), "\nSplit the said data on 'salesman_id', 'customer_id' wise:")
_l_(79439)
result = _c_(79442, _a_(79441, _n_(79440, "df", lambda: df), "groupby"), ['salesman_id', 'customer_id'])
_l_(79443)
for (name, group) in _n_(79444, "result", lambda: result):
    _l_(79456)

    _c_(79446, _n_(79445, "print", lambda: print), '\nGroup:')
    _l_(79447)
    _c_(79450, _n_(79448, "print", lambda: print), _n_(79449, "name", lambda: name))
    _l_(79451)
    _c_(79454, _n_(79452, "print", lambda: print), _n_(79453, "group", lambda: group))
    _l_(79455)
n = 2
_l_(79457)
_c_(79459, _n_(79458, "print", lambda: print), '\nDroping last two records:')
_l_(79460)
result1 = _c_(79470, _a_(79462, _n_(79461, "df", lambda: df), "drop"), _a_(79469, _c_(79468, _a_(79466, _c_(79465, _a_(79464, _n_(79463, "df", lambda: df), "groupby"), ['salesman_id', 'customer_id']), "tail"), _n_(79467, "n", lambda: n)), "index"), axis=0)
_l_(79471)
_c_(79474, _n_(79472, "print", lambda: print), _n_(79473, "result1", lambda: result1))
_l_(79475)