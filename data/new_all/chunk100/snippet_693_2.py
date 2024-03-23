# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(71701)

except ImportError:
    pass
series1 = _c_(71704, _a_(71703, _n_(71702, "pd", lambda: pd), "Series"), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
_l_(71705)
_c_(71707, _n_(71706, "print", lambda: print), 'Original Series:')
_l_(71708)
_c_(71711, _n_(71709, "print", lambda: print), _n_(71710, "series1", lambda: series1))
_l_(71712)
_c_(71715, _n_(71713, "print", lambda: print), _n_(71714, "series2", lambda: series2))
_l_(71716)
result = [_c_(71723, _a_(71721, _c_(71720, _a_(71718, _n_(71717, "pd", lambda: pd), "Index"), _n_(71719, "series1", lambda: series1)), "get_loc"), _n_(71722, "i", lambda: i)) for i in _n_(71724, "series2", lambda: series2)]
_l_(71725)
_c_(71727, _n_(71726, "print", lambda: print), 'Positions of items of series2 in series1:')
_l_(71728)
_c_(71731, _n_(71729, "print", lambda: print), _n_(71730, "result", lambda: result))
_l_(71732)