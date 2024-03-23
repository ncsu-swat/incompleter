# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(30682)

except ImportError:
    pass
cols = _c_(30686, _a_(30685, _a_(30684, _n_(30683, "pd", lambda: pd), "MultiIndex"), "from_tuples"), [('a', 'x'), ('a', 'y'), ('a', 'z')])
_l_(30687)
_c_(30689, _n_(30688, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(30690)
df = _c_(30694, _a_(30692, _n_(30691, "pd", lambda: pd), "DataFrame"), [[1, 2, 3], [3, 4, 5], [5, 6, 7]], columns=_n_(30693, "cols", lambda: cols))
_l_(30695)
_c_(30698, _n_(30696, "print", lambda: print), _n_(30697, "df", lambda: df))
_l_(30699)
_c_(30701, _n_(30700, "print", lambda: print), '\nRemove the top level index:')
_l_(30702)
_n_(30703, "df", lambda: df).columns = _c_(30707, _a_(30706, _a_(30705, _n_(30704, "df", lambda: df), "columns"), "droplevel"), 0)
_l_(30708)
_c_(30711, _n_(30709, "print", lambda: print), _n_(30710, "df", lambda: df))
_l_(30712)
df = _c_(30716, _a_(30714, _n_(30713, "pd", lambda: pd), "DataFrame"), [[1, 2, 3], [3, 4, 5], [5, 6, 7]], columns=_n_(30715, "cols", lambda: cols))
_l_(30717)
_c_(30719, _n_(30718, "print", lambda: print), '\nOriginal dataframe:')
_l_(30720)
_c_(30723, _n_(30721, "print", lambda: print), _n_(30722, "df", lambda: df))
_l_(30724)
_c_(30726, _n_(30725, "print", lambda: print), '\nRemove the index next to top level:')
_l_(30727)
_c_(30730, _n_(30728, "print", lambda: print), _n_(30729, "df", lambda: df))
_l_(30731)