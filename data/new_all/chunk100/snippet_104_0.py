# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(4882)

except ImportError:
    pass
now = _c_(4886, _a_(4885, _a_(4884, _n_(4883, "datetime", lambda: datetime), "datetime"), "now"))
_l_(4887)
_c_(4890, _n_(4888, "print", lambda: print), _n_(4889, "now", lambda: now))
_l_(4891)
year = lambda x: _a_(4893, _n_(4892, "x", lambda: x), "year")
_l_(4894)
day = lambda x: _a_(4896, _n_(4895, "x", lambda: x), "day")
_l_(4897)
t = lambda x: _c_(4900, _a_(4899, _n_(4898, "x", lambda: x), "time"))
_l_(4901)
_c_(4906, _n_(4902, "print", lambda: print), _c_(4905, _n_(4903, "year", lambda: year), _n_(4904, "now", lambda: now)))
_l_(4907)
_c_(4912, _n_(4908, "print", lambda: print), _c_(4911, _n_(4909, "month", lambda: month), _n_(4910, "now", lambda: now)))
_l_(4913)
_c_(4918, _n_(4914, "print", lambda: print), _c_(4917, _n_(4915, "day", lambda: day), _n_(4916, "now", lambda: now)))
_l_(4919)
_c_(4924, _n_(4920, "print", lambda: print), _c_(4923, _n_(4921, "t", lambda: t), _n_(4922, "now", lambda: now)))
_l_(4925)