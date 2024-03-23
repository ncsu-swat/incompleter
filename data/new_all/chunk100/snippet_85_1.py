# LExecutor: DO NOT INSTRUMENT

from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(84747)

except ImportError:
    pass
payload = {'key1': 'value1', 'key2': 'value2'}
_l_(84748)
_c_(84751, _n_(84749, "print", lambda: print), 'Parameters: ', _n_(84750, "payload", lambda: payload))
_l_(84752)
_c_(84754, _n_(84753, "print", lambda: print), 'Print the url to check the URL has been correctly encoded or not!')
_l_(84755)
_c_(84759, _n_(84756, "print", lambda: print), _a_(84758, _n_(84757, "r", lambda: r), "url"))
_l_(84760)
_c_(84762, _n_(84761, "print", lambda: print), '\nPass a list of items as a value:')
_l_(84763)
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
_l_(84764)
_c_(84767, _n_(84765, "print", lambda: print), 'Parameters: ', _n_(84766, "payload", lambda: payload))
_l_(84768)
r = _c_(84772, _a_(84770, _n_(84769, "requests", lambda: requests), "get"), 'https://httpbin.org/get', params=_n_(84771, "payload", lambda: payload))
_l_(84773)
_c_(84775, _n_(84774, "print", lambda: print), 'Print the url to check the URL has been correctly encoded or not!')
_l_(84776)
_c_(84780, _n_(84777, "print", lambda: print), _a_(84779, _n_(84778, "r", lambda: r), "url"))
_l_(84781)