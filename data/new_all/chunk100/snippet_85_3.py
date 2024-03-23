# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(84819)

except ImportError:
    pass
_c_(84822, _n_(84820, "print", lambda: print), 'Parameters: ', _n_(84821, "payload", lambda: payload))
_l_(84823)
r = _c_(84827, _a_(84825, _n_(84824, "requests", lambda: requests), "get"), 'https://httpbin.org/get', params=_n_(84826, "payload", lambda: payload))
_l_(84828)
_c_(84830, _n_(84829, "print", lambda: print), 'Print the url to check the URL has been correctly encoded or not!')
_l_(84831)
_c_(84835, _n_(84832, "print", lambda: print), _a_(84834, _n_(84833, "r", lambda: r), "url"))
_l_(84836)
_c_(84838, _n_(84837, "print", lambda: print), '\nPass a list of items as a value:')
_l_(84839)
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
_l_(84840)
_c_(84843, _n_(84841, "print", lambda: print), 'Parameters: ', _n_(84842, "payload", lambda: payload))
_l_(84844)
r = _c_(84848, _a_(84846, _n_(84845, "requests", lambda: requests), "get"), 'https://httpbin.org/get', params=_n_(84847, "payload", lambda: payload))
_l_(84849)
_c_(84851, _n_(84850, "print", lambda: print), 'Print the url to check the URL has been correctly encoded or not!')
_l_(84852)
_c_(84856, _n_(84853, "print", lambda: print), _a_(84855, _n_(84854, "r", lambda: r), "url"))
_l_(84857)