# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/7023052/configure-flask-dev-server-to-be-visible-across-the-network
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(63022)

except ImportError:
    pass

if _n_(63023, "__name__", lambda: __name__) == "__main__":
    _l_(63036)

    port = _c_(63029, _n_(63024, "int", lambda: int), _c_(63028, _a_(63027, _a_(63026, _n_(63025, "os", lambda: os), "environ"), "get"), "PORT", 5000))
    _l_(63030)
    _c_(63034, _a_(63032, _n_(63031, "app", lambda: app), "run"), host='0.0.0.0', port=_n_(63033, "port", lambda: port))
    _l_(63035)

