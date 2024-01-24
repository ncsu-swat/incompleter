# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60345611/dont-understand-cause-of-this-typeerror-exception
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pygal.maps.world import COUNTRIES
    _l_(700193)

except ImportError:
    pass
def get_country_code(country_name):
    _l_(700204)

    """Return the pygal 2-digit country code for given country."""
    for code,name in _c_(700196, _a_(700195, _n_(700194, "COUNTRIES", lambda: COUNTRIES), "items")):
        _l_(700202)

        if _n_(700197, "name", lambda: name) == _n_(700198, "country_name", lambda: country_name):
            _l_(700201)

            aux = _n_(700199, "code", lambda: code)
            _l_(700200)
            return aux
    aux = None
    _l_(700203)
    #if the country wasnt found,return none.
    return aux