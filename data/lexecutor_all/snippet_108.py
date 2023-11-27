# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(1548718)

except ImportError:
    pass
start_time = _c_(1548721, _a_(1548720, _n_(1548719, "time", lambda: time), "perf_counter"))
_l_(1548722)
for x in _c_(1548724, _n_(1548723, "range", lambda: range), 1, 100):
    _l_(1548729)

    _c_(1548727, _n_(1548725, "print", lambda: print), _n_(1548726, "x", lambda: x))
    _l_(1548728)
end_time = _c_(1548732, _a_(1548731, _n_(1548730, "time", lambda: time), "perf_counter"))
_l_(1548733)
_c_(1548737, _n_(1548734, "print", lambda: print), _n_(1548735, "end_time", lambda: end_time) - _n_(1548736, "start_time", lambda: start_time), "seconds")
_l_(1548738)

