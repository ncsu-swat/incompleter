# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61555925/typeerror-string-indices-must-be-integers-error-while-iterating-through-neste
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
api_request = _c_(703218, _a_(703217, _n_(703216, "requests", lambda: requests), "get"), 'https://api.thevirustracker.com/free-api?countryTotals=ALL')
_l_(703219)

api = _c_(703224, _a_(703221, _n_(703220, "json", lambda: json), "loads"), _a_(703223, _n_(703222, "api_request", lambda: api_request), "content"))
_l_(703225)

dict = _n_(703226, "api", lambda: api)['countryitems'][0]
_l_(703227)

for key in _n_(703228, "dict", lambda: dict):
    _l_(703236)


    country = _n_(703229, "api", lambda: api)['countryitems'][0][_n_(703230, "key", lambda: key)]['title']
    _l_(703231)
    _c_(703234, _n_(703232, "print", lambda: print), _n_(703233, "country", lambda: country))
    _l_(703235)