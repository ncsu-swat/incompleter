# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67106239/attributeerror-nonetype-object-has-no-attribute-encode-binance
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(408607)

except ImportError:
    pass
try:
    from binance.client import Client
    _l_(408609)

except ImportError:
    pass
try:
    from binance.websockets import BinanceSocketManager
    _l_(408611)

except ImportError:
    pass
try:
    from twisted.internet import reactor
    _l_(408613)

except ImportError:
    pass

# Get keys
api_key = _c_(408617, _a_(408616, _a_(408615, _n_(408614, "os", lambda: os), "environ"), "get"), 'binance_api')
_l_(408618)
api_secret = _c_(408622, _a_(408621, _a_(408620, _n_(408619, "os", lambda: os), "environ"), "get"), 'binance_secret')
_l_(408623)

# Connect to Binance
client = _c_(408627, _n_(408624, "Client", lambda: Client), _n_(408625, "api_key", lambda: api_key), _n_(408626, "api_secret", lambda: api_secret))
_l_(408628)
_c_(408633, _n_(408629, "print", lambda: print), _c_(408632, _a_(408631, _n_(408630, "client", lambda: client), "get_account")))
_l_(408634)