# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(120862)

except ImportError:
    pass
_c_(120865, _n_(120863, "print", lambda: print), 'Parameters: ', _n_(120864, "payload", lambda: payload))
_l_(120866)
r = _c_(120870, _a_(120868, _n_(120867, "requests", lambda: requests), "get"), 'https://httpbin.org/get', params=_n_(120869, "payload", lambda: payload))
_l_(120871)
_c_(120873, _n_(120872, "print", lambda: print), 'Print the url to check the URL has been correctly encoded or not!')
_l_(120874)
_c_(120878, _n_(120875, "print", lambda: print), _a_(120877, _n_(120876, "r", lambda: r), "url"))
_l_(120879)
_c_(120881, _n_(120880, "print", lambda: print), '\nPass a list of items as a value:')
_l_(120882)
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
_l_(120883)
_c_(120886, _n_(120884, "print", lambda: print), 'Parameters: ', _n_(120885, "payload", lambda: payload))
_l_(120887)
r = _c_(120891, _a_(120889, _n_(120888, "requests", lambda: requests), "get"), 'https://httpbin.org/get', params=_n_(120890, "payload", lambda: payload))
_l_(120892)
_c_(120894, _n_(120893, "print", lambda: print), 'Print the url to check the URL has been correctly encoded or not!')
_l_(120895)
_c_(120899, _n_(120896, "print", lambda: print), _a_(120898, _n_(120897, "r", lambda: r), "url"))
_l_(120900)