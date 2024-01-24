# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61555925/typeerror-string-indices-must-be-integers-error-while-iterating-through-neste
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
api_request = _c_(697770, _a_(697769, _n_(697768, "requests", lambda: requests), "get"), 'https://api.thevirustracker.com/free-api?countryTotals=ALL')
_l_(697771)

api = _c_(697776, _a_(697773, _n_(697772, "json", lambda: json), "loads"), _a_(697775, _n_(697774, "api_request", lambda: api_request), "content"))
_l_(697777)

dict = _n_(697778, "api", lambda: api)['countryitems'][0]
_l_(697779)

for key in _n_(697780, "dict", lambda: dict):
    _l_(697788)


    country = _n_(697781, "api", lambda: api)['countryitems'][0][_n_(697782, "key", lambda: key)]['title']
    _l_(697783)
    _c_(697786, _n_(697784, "print", lambda: print), _n_(697785, "country", lambda: country))
    _l_(697787)