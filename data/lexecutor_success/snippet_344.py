# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1006289/how-to-find-out-the-number-of-cpus-using-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(1543489)

except ImportError:
    pass
workers = _c_(1543492, _a_(1543491, _n_(1543490, "os", lambda: os), "cpu_count"))
_l_(1543493)
if 'sched_getaffinity' in _c_(1543496, _n_(1543494, "dir", lambda: dir), _n_(1543495, "os", lambda: os)):
    _l_(1543503)

    workers = _c_(1543501, _n_(1543497, "len", lambda: len), _c_(1543500, _a_(1543499, _n_(1543498, "os", lambda: os), "sched_getaffinity"), 0))
    _l_(1543502)

