# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(84783)

except ImportError:
    pass
payload = {'key1': 'value1', 'key2': 'value2'}
_l_(84784)
_c_(84787, _n_(84785, "print", lambda: print), 'Parameters: ', _n_(84786, "payload", lambda: payload))
_l_(84788)
r = _c_(84792, _a_(84790, _n_(84789, "requests", lambda: requests), "get"), 'https://httpbin.org/get', params=_n_(84791, "payload", lambda: payload))
_l_(84793)
_c_(84795, _n_(84794, "print", lambda: print), 'Print the url to check the URL has been correctly encoded or not!')
_l_(84796)
_c_(84800, _n_(84797, "print", lambda: print), _a_(84799, _n_(84798, "r", lambda: r), "url"))
_l_(84801)
_c_(84803, _n_(84802, "print", lambda: print), '\nPass a list of items as a value:')
_l_(84804)
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
_l_(84805)
_c_(84808, _n_(84806, "print", lambda: print), 'Parameters: ', _n_(84807, "payload", lambda: payload))
_l_(84809)
_c_(84811, _n_(84810, "print", lambda: print), 'Print the url to check the URL has been correctly encoded or not!')
_l_(84812)
_c_(84816, _n_(84813, "print", lambda: print), _a_(84815, _n_(84814, "r", lambda: r), "url"))
_l_(84817)