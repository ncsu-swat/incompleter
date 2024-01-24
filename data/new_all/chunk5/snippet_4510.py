# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/56447938/typeerror-get-token-missing-1-required-positional-argument-bs4
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(691523)

except ImportError:
    pass
try:
    from bs4 import BeautifulSoup
    _l_(691525)

except ImportError:
    pass

class checker_start(_n_(691526, "object", lambda: object)):
    _l_(691544)

    def get_token(self, bs4):
        _l_(691543)

        data = _c_(691529, _a_(691528, _n_(691527, "requests", lambda: requests), "get"), "https://login.live.com")
        _l_(691530)
        soup = _c_(691535, _a_(691532, _n_(691531, "bs4", lambda: bs4), "BeautifulSoup"), _a_(691534, _n_(691533, "data", lambda: data), "text"), 'lxml')
        _l_(691536)

        token_1 = _c_(691539, _a_(691538, _n_(691537, "soup", lambda: soup), "find"), "input", {"value": "flowToken"})["value"]
        _l_(691540)
        aux = _n_(691541, "token_1", lambda: token_1)
        _l_(691542)
        return aux


_c_(691550, _n_(691545, "print", lambda: print), _c_(691549, _a_(691548, _c_(691547, _n_(691546, "checker_start", lambda: checker_start)), "get_token")))
_l_(691551)