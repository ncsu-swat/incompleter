# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/70348607/typeerror-unsupported-operand-types-for-str-and-str-pandas-reindex
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(632418)

except ImportError:
    pass
s1=_c_(632423, _a_(632420, _n_(632419, "pd", lambda: pd), "Series"), [1,2,3,4],index=_c_(632422, _n_(632421, "list", lambda: list), 'aceg'))
_l_(632424)
_c_(632434, _n_(632425, "print", lambda: print), _c_(632433, _a_(632427, _n_(632426, "s1", lambda: s1), "reindex"), _c_(632432, _a_(632429, _n_(632428, "pd", lambda: pd), "Index"), _c_(632431, _n_(632430, "list", lambda: list), 'abdg')),method='nearest'))
_l_(632435)