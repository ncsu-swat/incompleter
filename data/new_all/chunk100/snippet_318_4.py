# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(30733)

except ImportError:
    pass
cols = _c_(30737, _a_(30736, _a_(30735, _n_(30734, "pd", lambda: pd), "MultiIndex"), "from_tuples"), [('a', 'x'), ('a', 'y'), ('a', 'z')])
_l_(30738)
_c_(30740, _n_(30739, "print", lambda: print), '\nConstruct a Dataframe using the said MultiIndex levels: ')
_l_(30741)
df = _c_(30745, _a_(30743, _n_(30742, "pd", lambda: pd), "DataFrame"), [[1, 2, 3], [3, 4, 5], [5, 6, 7]], columns=_n_(30744, "cols", lambda: cols))
_l_(30746)
_c_(30749, _n_(30747, "print", lambda: print), _n_(30748, "df", lambda: df))
_l_(30750)
_c_(30752, _n_(30751, "print", lambda: print), '\nRemove the top level index:')
_l_(30753)
_n_(30754, "df", lambda: df).columns = _c_(30758, _a_(30757, _a_(30756, _n_(30755, "df", lambda: df), "columns"), "droplevel"), 0)
_l_(30759)
_c_(30762, _n_(30760, "print", lambda: print), _n_(30761, "df", lambda: df))
_l_(30763)
_c_(30765, _n_(30764, "print", lambda: print), '\nOriginal dataframe:')
_l_(30766)
_c_(30769, _n_(30767, "print", lambda: print), _n_(30768, "df", lambda: df))
_l_(30770)
_c_(30772, _n_(30771, "print", lambda: print), '\nRemove the index next to top level:')
_l_(30773)
_n_(30774, "df", lambda: df).columns = _c_(30778, _a_(30777, _a_(30776, _n_(30775, "df", lambda: df), "columns"), "droplevel"), 1)
_l_(30779)
_c_(30782, _n_(30780, "print", lambda: print), _n_(30781, "df", lambda: df))
_l_(30783)