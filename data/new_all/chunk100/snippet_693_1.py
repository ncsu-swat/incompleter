# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(71668)

except ImportError:
    pass
series2 = _c_(71671, _a_(71670, _n_(71669, "pd", lambda: pd), "Series"), [1, 3, 5, 7, 10])
_l_(71672)
_c_(71674, _n_(71673, "print", lambda: print), 'Original Series:')
_l_(71675)
_c_(71678, _n_(71676, "print", lambda: print), _n_(71677, "series1", lambda: series1))
_l_(71679)
_c_(71682, _n_(71680, "print", lambda: print), _n_(71681, "series2", lambda: series2))
_l_(71683)
result = [_c_(71690, _a_(71688, _c_(71687, _a_(71685, _n_(71684, "pd", lambda: pd), "Index"), _n_(71686, "series1", lambda: series1)), "get_loc"), _n_(71689, "i", lambda: i)) for i in _n_(71691, "series2", lambda: series2)]
_l_(71692)
_c_(71694, _n_(71693, "print", lambda: print), 'Positions of items of series2 in series1:')
_l_(71695)
_c_(71698, _n_(71696, "print", lambda: print), _n_(71697, "result", lambda: result))
_l_(71699)