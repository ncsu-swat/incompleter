# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1489599/how-do-i-find-out-my-pythonpath-using-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(1540853)

except ImportError:
    pass
for a in _a_(1540855, _n_(1540854, "sys", lambda: sys), "path"):
    _l_(1540864)

    a = _c_(1540858, _a_(1540857, _n_(1540856, "a", lambda: a), "replace"), '\\\\','\\')
    _l_(1540859)
    _c_(1540862, _n_(1540860, "print", lambda: print), _n_(1540861, "a", lambda: a))
    _l_(1540863)

