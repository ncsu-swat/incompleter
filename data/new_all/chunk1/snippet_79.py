# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47027254/typeerror-write-argument-must-be-str-not-bytes-python-3-vs-python-2
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(396444)

except ImportError:
    pass
with _c_(396446, _n_(396445, "open", lambda: open), 'random.bin','w') as f:
    _l_(396454)

    _c_(396452, _a_(396448, _n_(396447, "f", lambda: f), "write"), _c_(396451, _a_(396450, _n_(396449, "os", lambda: os), "urandom"), 10))
    _l_(396453)