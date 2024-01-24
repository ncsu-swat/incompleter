# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/31685788/calling-sys-stderr-fileno-after-checking-it-is-a-python-callable-raises-an
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _c_(446549, _n_(446546, "hasattr", lambda: hasattr), _a_(446548, _n_(446547, "sys", lambda: sys), "stderr"), 'fileno'):
    _l_(446561)

    if _c_(446554, _n_(446550, "callable", lambda: callable), _a_(446553, _a_(446552, _n_(446551, "sys", lambda: sys), "stderr"), "fileno")):
        _l_(446560)

        i = _c_(446558, _a_(446557, _a_(446556, _n_(446555, "sys", lambda: sys), "stderr"), "fileno"))
        _l_(446559)