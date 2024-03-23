# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(30579)

except ImportError:
    pass
cols = _c_(30583, _a_(30582, _a_(30581, _n_(30580, "pd", lambda: pd), "MultiIndex"), "from_tuples"), [('a', 'x'), ('a', 'y'), ('a', 'z')])
_l_(30584)
_c_(30586, _n_(30585, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(30587)
_c_(30590, _n_(30588, "print", lambda: print), _n_(30589, "df", lambda: df))
_l_(30591)
_c_(30593, _n_(30592, "print", lambda: print), '\nRemove the top level index:')
_l_(30594)
_n_(30595, "df", lambda: df).columns = _c_(30599, _a_(30598, _a_(30597, _n_(30596, "df", lambda: df), "columns"), "droplevel"), 0)
_l_(30600)
_c_(30603, _n_(30601, "print", lambda: print), _n_(30602, "df", lambda: df))
_l_(30604)
df = _c_(30608, _a_(30606, _n_(30605, "pd", lambda: pd), "DataFrame"), [[1, 2, 3], [3, 4, 5], [5, 6, 7]], columns=_n_(30607, "cols", lambda: cols))
_l_(30609)
_c_(30611, _n_(30610, "print", lambda: print), '\nOriginal dataframe:')
_l_(30612)
_c_(30615, _n_(30613, "print", lambda: print), _n_(30614, "df", lambda: df))
_l_(30616)
_c_(30618, _n_(30617, "print", lambda: print), '\nRemove the index next to top level:')
_l_(30619)
_n_(30620, "df", lambda: df).columns = _c_(30624, _a_(30623, _a_(30622, _n_(30621, "df", lambda: df), "columns"), "droplevel"), 1)
_l_(30625)
_c_(30628, _n_(30626, "print", lambda: print), _n_(30627, "df", lambda: df))
_l_(30629)