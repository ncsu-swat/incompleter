# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(84707)

except ImportError:
    pass
payload = {'key1': 'value1', 'key2': 'value2'}
_l_(84708)
_c_(84711, _n_(84709, "print", lambda: print), 'Parameters: ', _n_(84710, "payload", lambda: payload))
_l_(84712)
r = _c_(84716, _a_(84714, _n_(84713, "requests", lambda: requests), "get"), 'https://httpbin.org/get', params=_n_(84715, "payload", lambda: payload))
_l_(84717)
_c_(84719, _n_(84718, "print", lambda: print), 'Print the url to check the URL has been correctly encoded or not!')
_l_(84720)
_c_(84724, _n_(84721, "print", lambda: print), _a_(84723, _n_(84722, "r", lambda: r), "url"))
_l_(84725)
_c_(84727, _n_(84726, "print", lambda: print), '\nPass a list of items as a value:')
_l_(84728)
_c_(84731, _n_(84729, "print", lambda: print), 'Parameters: ', _n_(84730, "payload", lambda: payload))
_l_(84732)
r = _c_(84736, _a_(84734, _n_(84733, "requests", lambda: requests), "get"), 'https://httpbin.org/get', params=_n_(84735, "payload", lambda: payload))
_l_(84737)
_c_(84739, _n_(84738, "print", lambda: print), 'Print the url to check the URL has been correctly encoded or not!')
_l_(84740)
_c_(84744, _n_(84741, "print", lambda: print), _a_(84743, _n_(84742, "r", lambda: r), "url"))
_l_(84745)