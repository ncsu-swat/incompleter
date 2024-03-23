# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(30631)

except ImportError:
    pass
cols = _c_(30635, _a_(30634, _a_(30633, _n_(30632, "pd", lambda: pd), "MultiIndex"), "from_tuples"), [('a', 'x'), ('a', 'y'), ('a', 'z')])
_l_(30636)
_c_(30638, _n_(30637, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(30639)
df = _c_(30643, _a_(30641, _n_(30640, "pd", lambda: pd), "DataFrame"), [[1, 2, 3], [3, 4, 5], [5, 6, 7]], columns=_n_(30642, "cols", lambda: cols))
_l_(30644)
_c_(30647, _n_(30645, "print", lambda: print), _n_(30646, "df", lambda: df))
_l_(30648)
_c_(30650, _n_(30649, "print", lambda: print), '\nRemove the top level index:')
_l_(30651)
_c_(30654, _n_(30652, "print", lambda: print), _n_(30653, "df", lambda: df))
_l_(30655)
df = _c_(30659, _a_(30657, _n_(30656, "pd", lambda: pd), "DataFrame"), [[1, 2, 3], [3, 4, 5], [5, 6, 7]], columns=_n_(30658, "cols", lambda: cols))
_l_(30660)
_c_(30662, _n_(30661, "print", lambda: print), '\nOriginal dataframe:')
_l_(30663)
_c_(30666, _n_(30664, "print", lambda: print), _n_(30665, "df", lambda: df))
_l_(30667)
_c_(30669, _n_(30668, "print", lambda: print), '\nRemove the index next to top level:')
_l_(30670)
_n_(30671, "df", lambda: df).columns = _c_(30675, _a_(30674, _a_(30673, _n_(30672, "df", lambda: df), "columns"), "droplevel"), 1)
_l_(30676)
_c_(30679, _n_(30677, "print", lambda: print), _n_(30678, "df", lambda: df))
_l_(30680)