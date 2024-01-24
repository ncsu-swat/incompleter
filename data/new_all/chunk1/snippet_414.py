# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45583691/typeerror-expected-string-or-bytes-like-object-tensorflow
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow as tf
    _l_(385221)

except ImportError:
    pass
with _c_(385224, _a_(385223, _n_(385222, "tf", lambda: tf), "Session")) as ses:
    _l_(385238)

    c = _c_(385227, _a_(385226, _n_(385225, "tf", lambda: tf), "add"), 1, 2)
    _l_(385228)
    d = _c_(385232, _a_(385230, _n_(385229, "ses", lambda: ses), "run"), _n_(385231, "c", lambda: c))
    _l_(385233)
    _c_(385236, _n_(385234, "print", lambda: print), _n_(385235, "d", lambda: d))
    _l_(385237)