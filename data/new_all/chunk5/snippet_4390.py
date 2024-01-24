# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58590443/pkgutil-get-data-attributeerror-nonetype-object-has-no-attribute-decode
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pkg_resources import resource_filename
    _l_(656346)

except ImportError:
    pass
try:
    from os.path import join as join_path
    _l_(656348)

except ImportError:
    pass

@_c_(656350, _n_(656349, "fixture", lambda: fixture), scope='session')
def ref_o_full():
    _l_(656362)

    dir = _c_(656353, _n_(656351, "resource_filename", lambda: resource_filename), _n_(656352, "__name__", lambda: __name__), 'test_data')
    _l_(656354)
    aux = _c_(656360, _a_(656356, _n_(656355, "pd", lambda: pd), "read_csv"), _c_(656359, _n_(656357, "join_path", lambda: join_path), _n_(656358, "dir", lambda: dir), 'ref_o.csv'))
    _l_(656361)
    return aux