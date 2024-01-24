# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67015675/getting-unsupported-operand-type-error-while-trying-to-subtract-two-date-values
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(393737)

except ImportError:
    pass
try:
    import time
    _l_(393739)

except ImportError:
    pass
start =_c_(393746, _a_(393745, _c_(393744, _a_(393743, _c_(393742, _a_(393741, _n_(393740, "datetime", lambda: datetime), "now")), "replace"), microsecond=0), "isoformat"), ' ')
_l_(393747)
end = _c_(393754, _a_(393753, _c_(393752, _a_(393751, _c_(393750, _a_(393749, _n_(393748, "datetime", lambda: datetime), "now")), "replace"), microsecond=0), "isoformat"), ' ')
_l_(393755)
_c_(393759, _n_(393756, "print", lambda: print), f" Total Time taken by check run is {_n_(393757, 'end', lambda: end) - _n_(393758, 'start', lambda: start)}[hh:mm:ss]")
_l_(393760)