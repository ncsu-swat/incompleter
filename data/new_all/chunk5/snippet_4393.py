# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58590443/pkgutil-get-data-attributeerror-nonetype-object-has-no-attribute-decode
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pkgutil import get_data
    _l_(700346)

except ImportError:
    pass

@_c_(700348, _n_(700347, "fixture", lambda: fixture), scope='session')
def ref_o_full():
    _l_(700359)

    aux = _c_(700357, _a_(700350, _n_(700349, "pd", lambda: pd), "read_csv"), _c_(700356, _n_(700351, "StringIO", lambda: StringIO), _c_(700355, _a_(700354, _c_(700353, _n_(700352, "get_data", lambda: get_data), 'test_data', 'ref_o.csv'), "decode"))))
    _l_(700358)
    return aux