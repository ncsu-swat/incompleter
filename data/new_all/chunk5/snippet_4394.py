# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58590443/pkgutil-get-data-attributeerror-nonetype-object-has-no-attribute-decode
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pkg_resources import resource_filename
    _l_(654146)

except ImportError:
    pass
try:
    from os.path import join as join_path
    _l_(654148)

except ImportError:
    pass

@_c_(654150, _n_(654149, "fixture", lambda: fixture), scope='session')
def ref_o_full():
    _l_(654162)

    dir = _c_(654153, _n_(654151, "resource_filename", lambda: resource_filename), _n_(654152, "__name__", lambda: __name__), 'test_data')
    _l_(654154)
    aux = _c_(654160, _a_(654156, _n_(654155, "pd", lambda: pd), "read_csv"), _c_(654159, _n_(654157, "join_path", lambda: join_path), _n_(654158, "dir", lambda: dir), 'ref_o.csv'))
    _l_(654161)
    return aux