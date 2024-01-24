# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58590443/pkgutil-get-data-attributeerror-nonetype-object-has-no-attribute-decode
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pkgutil import get_data
    _l_(687615)

except ImportError:
    pass

@_c_(687617, _n_(687616, "fixture", lambda: fixture), scope='session')
def ref_o_full():
    _l_(687628)

    aux = _c_(687626, _a_(687619, _n_(687618, "pd", lambda: pd), "read_csv"), _c_(687625, _n_(687620, "StringIO", lambda: StringIO), _c_(687624, _a_(687623, _c_(687622, _n_(687621, "get_data", lambda: get_data), 'test_data', 'ref_o.csv'), "decode"))))
    _l_(687627)
    return aux