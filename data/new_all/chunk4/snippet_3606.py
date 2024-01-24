# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71395086/typeerror-expected-string-or-bytes-like-object-when-setting-cookies-gotten-fr
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
cookies = _c_(639262, _a_(639259, _n_(639258, "pickle", lambda: pickle), "load"), _c_(639261, _n_(639260, "open", lambda: open), "cookies.pkl", "rb"))
_l_(639263)

r = _c_(639266, _a_(639265, _n_(639264, "requests", lambda: requests), "Session"))
_l_(639267)
for cookie in _n_(639268, "cookies", lambda: cookies):
    _l_(639276)

    _c_(639274, _a_(639271, _a_(639270, _n_(639269, "r", lambda: r), "cookies"), "set"), _n_(639272, "cookie", lambda: cookie)['name'], _n_(639273, "cookie", lambda: cookie)['value'])
    _l_(639275)