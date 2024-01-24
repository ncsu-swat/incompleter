# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56261606/how-to-fix-typeerror-a-bytes-like-object-is-required-not-str-error-in-pyth
# mainTest.py module
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from config import logger
    _l_(415496)

except ImportError:
    pass
log = _c_(415500, _a_(415498, _n_(415497, "logger", lambda: logger), "getLogger"), _n_(415499, "__file__", lambda: __file__))
_l_(415501)

def function():
    _l_(415508)

    message = "testing"
    _l_(415502)
    _c_(415506, _a_(415504, _n_(415503, "log", lambda: log), "info"), _n_(415505, "message", lambda: message))
    _l_(415507)