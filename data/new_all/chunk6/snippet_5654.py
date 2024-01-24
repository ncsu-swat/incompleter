# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47733532/python-getting-typeerror-during-checking-whether-a-json-key-exist-or-not
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
json = _c_(342093, _a_(342091, _n_(342090, "json", lambda: json), "dumps"), _n_(342092, "results", lambda: results))
_l_(342094)
for profile in _c_(342096, _n_(342095, "range", lambda: range), 0, 10):
    _l_(342104)

    if 'person' not in _n_(342097, "json", lambda: json)['items'][_n_(342098, "profile", lambda: profile)]['pagemap']:
        _l_(342103)

        org="null"
        _l_(342099)
    else:
        org= _n_(342100, "results", lambda: results)['items'][_n_(342101, "profile", lambda: profile)]['pagemap']['person'][0]['org']
        _l_(342102)
        #results stores the json response.