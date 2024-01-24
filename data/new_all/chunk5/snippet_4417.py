# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58044715/attributeerror-nonetype-object-has-no-attribute-get-balance
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from upstox_api.api import *
    _l_(669599)

except ImportError:
    pass
def get_balance():
    _l_(669605)

    global u, s
    _l_(669600)
    aux = _c_(669603, _a_(669602, _n_(669601, "u", lambda: u), "get_balance"))
    _l_(669604)
    return aux