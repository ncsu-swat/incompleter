# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67142181/attributeerror-bytes-object-has-no-attribute-hexdigest
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(467746)

except ImportError:
    pass
try:
    import hashlib
    _l_(467748)

except ImportError:
    pass

def request_api_data (query_char):
    _l_(467764)

    url = 'https://api.pwnedpasswords.com/range/'+ _n_(467749, "query_char", lambda: query_char)
    _l_(467750)
    res = _c_(467754, _a_(467752, _n_(467751, "requests", lambda: requests), "get"), _n_(467753, "url", lambda: url))
    _l_(467755)
    if _a_(467757, _n_(467756, "res", lambda: res), "status_code") != 200:
        _l_(467763)

        _c_(467759, _n_(467758, "print", lambda: print), 'it is an error')
        _l_(467760)
        aux = _n_(467761, "res", lambda: res)
        _l_(467762)
        #raise RuntimeError(f'Error fetching: {res.status_code}, check api and try again')
        return aux
_c_(467766, _n_(467765, "request_api_data", lambda: request_api_data), '123')
_l_(467767)

def pwned_api_check(password):
    _l_(467783)

    sha1password= _c_(467777, _a_(467769, _n_(467768, "hashlib", lambda: hashlib), "sha1"), _c_(467776, _a_(467775, _c_(467774, _a_(467773, _c_(467772, _a_(467771, _n_(467770, "password", lambda: password), "encode"), 'utf-8'), "hexdigest")), "upper")))
    _l_(467778)
    
    _c_(467781, _n_(467779, "print", lambda: print), _n_(467780, "sha1password", lambda: sha1password))
    _l_(467782)

_c_(467785, _n_(467784, "pwned_api_check", lambda: pwned_api_check), '123')  
_l_(467786)  