# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61555925/typeerror-string-indices-must-be-integers-error-while-iterating-through-neste
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
api_request = _c_(594849, _a_(594848, _n_(594847, "requests", lambda: requests), "get"), 'https://api.thevirustracker.com/free-api?countryTotals=ALL')
_l_(594850)

api = _c_(594855, _a_(594852, _n_(594851, "json", lambda: json), "loads"), _a_(594854, _n_(594853, "api_request", lambda: api_request), "content"))
_l_(594856)

dict = _n_(594857, "api", lambda: api)['countryitems'][0]
_l_(594858)

for key in _n_(594859, "dict", lambda: dict):
    _l_(594867)


    country = _n_(594860, "api", lambda: api)['countryitems'][0][_n_(594861, "key", lambda: key)]['title']
    _l_(594862)
    _c_(594865, _n_(594863, "print", lambda: print), _n_(594864, "country", lambda: country))
    _l_(594866)