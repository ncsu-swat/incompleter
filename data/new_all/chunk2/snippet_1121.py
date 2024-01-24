# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/72341946/typeerror-not-supported-between-instances-of-str-and-float
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import requests
    _l_(447584)

except ImportError:
    pass

def get_ids():
    _l_(447613)

    url = "https://retro.umoiq.com/service/publicJSONFeed?command=vehicleLocations&a=sf-muni&t=0"
    _l_(447585)
    response = _c_(447591, _a_(447590, _c_(447589, _a_(447587, _n_(447586, "requests", lambda: requests), "get"), _n_(447588, "url", lambda: url)), "json"))
    _l_(447592)

    id_list = []
    _l_(447593)

    for id in _n_(447594, "response", lambda: response)['vehicle']:
        _l_(447610)

        lat = _n_(447595, "id", lambda: id)['lat']
        _l_(447596)
        lon = _n_(447597, "id", lambda: id)['lon'] 
        _l_(447598) 
        
        if (_n_(447599, "lat", lambda: lat) <= 37.769754 and _n_(447600, "lat", lambda: lat) >= 37.748554):
            _l_(447609)

            if (_n_(447601, "lon", lambda: lon) >= -122.427050 and _n_(447602, "lon", lambda: lon) <= -122.404535):
                _l_(447608)

                _c_(447606, _a_(447604, _n_(447603, "id_list", lambda: id_list), "append"), _n_(447605, "id", lambda: id)['id'])
                _l_(447607)
    aux = _n_(447611, "id_list", lambda: id_list)
    _l_(447612)
    
    return aux

def main():
    _l_(447619)

    _c_(447617, _n_(447614, "print", lambda: print), _c_(447616, _n_(447615, "get_ids", lambda: get_ids)))
    _l_(447618)

if _n_(447620, "__name__", lambda: __name__) == "__main__":
    _l_(447624)

    _c_(447622, _n_(447621, "main", lambda: main))
    _l_(447623)