# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(30527)

except ImportError:
    pass
_c_(30529, _n_(30528, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(30530)
df = _c_(30534, _a_(30532, _n_(30531, "pd", lambda: pd), "DataFrame"), [[1, 2, 3], [3, 4, 5], [5, 6, 7]], columns=_n_(30533, "cols", lambda: cols))
_l_(30535)
_c_(30538, _n_(30536, "print", lambda: print), _n_(30537, "df", lambda: df))
_l_(30539)
_c_(30541, _n_(30540, "print", lambda: print), '\nRemove the top level index:')
_l_(30542)
_n_(30543, "df", lambda: df).columns = _c_(30547, _a_(30546, _a_(30545, _n_(30544, "df", lambda: df), "columns"), "droplevel"), 0)
_l_(30548)
_c_(30551, _n_(30549, "print", lambda: print), _n_(30550, "df", lambda: df))
_l_(30552)
df = _c_(30556, _a_(30554, _n_(30553, "pd", lambda: pd), "DataFrame"), [[1, 2, 3], [3, 4, 5], [5, 6, 7]], columns=_n_(30555, "cols", lambda: cols))
_l_(30557)
_c_(30559, _n_(30558, "print", lambda: print), '\nOriginal dataframe:')
_l_(30560)
_c_(30563, _n_(30561, "print", lambda: print), _n_(30562, "df", lambda: df))
_l_(30564)
_c_(30566, _n_(30565, "print", lambda: print), '\nRemove the index next to top level:')
_l_(30567)
_n_(30568, "df", lambda: df).columns = _c_(30572, _a_(30571, _a_(30570, _n_(30569, "df", lambda: df), "columns"), "droplevel"), 1)
_l_(30573)
_c_(30576, _n_(30574, "print", lambda: print), _n_(30575, "df", lambda: df))
_l_(30577)