# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(110418)

except ImportError:
    pass
_c_(110420, _n_(110419, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(110421)
df = _c_(110425, _a_(110423, _n_(110422, "pd", lambda: pd), "DataFrame"), [[1, 2, 3], [3, 4, 5], [5, 6, 7]], columns=_n_(110424, "cols", lambda: cols))
_l_(110426)
_c_(110429, _n_(110427, "print", lambda: print), _n_(110428, "df", lambda: df))
_l_(110430)
_c_(110432, _n_(110431, "print", lambda: print), '\nRemove the top level index:')
_l_(110433)
_n_(110434, "df", lambda: df).columns = _c_(110438, _a_(110437, _a_(110436, _n_(110435, "df", lambda: df), "columns"), "droplevel"), 0)
_l_(110439)
_c_(110442, _n_(110440, "print", lambda: print), _n_(110441, "df", lambda: df))
_l_(110443)
df = _c_(110447, _a_(110445, _n_(110444, "pd", lambda: pd), "DataFrame"), [[1, 2, 3], [3, 4, 5], [5, 6, 7]], columns=_n_(110446, "cols", lambda: cols))
_l_(110448)
_c_(110450, _n_(110449, "print", lambda: print), '\nOriginal dataframe:')
_l_(110451)
_c_(110454, _n_(110452, "print", lambda: print), _n_(110453, "df", lambda: df))
_l_(110455)
_c_(110457, _n_(110456, "print", lambda: print), '\nRemove the index next to top level:')
_l_(110458)
_n_(110459, "df", lambda: df).columns = _c_(110463, _a_(110462, _a_(110461, _n_(110460, "df", lambda: df), "columns"), "droplevel"), 1)
_l_(110464)
_c_(110467, _n_(110465, "print", lambda: print), _n_(110466, "df", lambda: df))
_l_(110468)