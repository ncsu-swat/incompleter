# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/43663206/typeerror-unsupported-operand-types-for-dict-values-and-int
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(413791)

except ImportError:
    pass
# Summarize the data about minutes spent in the classroom
total_minutes = _c_(413794, _a_(413793, _n_(413792, "total_minutes_by_account", lambda: total_minutes_by_account), "values"))
_l_(413795)
total_minutes = _c_(413799, _a_(413797, _n_(413796, "np", lambda: np), "array"), _n_(413798, "total_minutes", lambda: total_minutes))
_l_(413800)
_c_(413806, _n_(413801, "print", lambda: print), 'Mean:', _c_(413805, _a_(413803, _n_(413802, "np", lambda: np), "mean"), _n_(413804, "total_minutes", lambda: total_minutes)))
_l_(413807)
_c_(413813, _n_(413808, "print", lambda: print), 'Standard deviation:', _c_(413812, _a_(413810, _n_(413809, "np", lambda: np), "std"), _n_(413811, "total_minutes", lambda: total_minutes)))
_l_(413814)
_c_(413820, _n_(413815, "print", lambda: print), 'Minimum:', _c_(413819, _a_(413817, _n_(413816, "np", lambda: np), "min"), _n_(413818, "total_minutes", lambda: total_minutes)))
_l_(413821)
_c_(413827, _n_(413822, "print", lambda: print), 'Maximum:', _c_(413826, _a_(413824, _n_(413823, "np", lambda: np), "max"), _n_(413825, "total_minutes", lambda: total_minutes)))
_l_(413828)