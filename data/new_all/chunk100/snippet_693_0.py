# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(71640)

except ImportError:
    pass
series1 = _c_(71643, _a_(71642, _n_(71641, "pd", lambda: pd), "Series"), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
_l_(71644)
series2 = _c_(71647, _a_(71646, _n_(71645, "pd", lambda: pd), "Series"), [1, 3, 5, 7, 10])
_l_(71648)
_c_(71650, _n_(71649, "print", lambda: print), 'Original Series:')
_l_(71651)
_c_(71654, _n_(71652, "print", lambda: print), _n_(71653, "series1", lambda: series1))
_l_(71655)
_c_(71658, _n_(71656, "print", lambda: print), _n_(71657, "series2", lambda: series2))
_l_(71659)
_c_(71661, _n_(71660, "print", lambda: print), 'Positions of items of series2 in series1:')
_l_(71662)
_c_(71665, _n_(71663, "print", lambda: print), _n_(71664, "result", lambda: result))
_l_(71666)