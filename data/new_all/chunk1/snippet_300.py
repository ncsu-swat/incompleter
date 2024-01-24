# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54546868/how-to-fix-typeerror-must-be-real-number-not-str-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pysal.cg.kdtree import KDTree
    _l_(383166)

except ImportError:
    pass
try:
    from pysal.cg import RADIUS_EARTH_MILES
    _l_(383168)

except ImportError:
    pass

trees_xys = _a_(383170, _n_(383169, "results_df", lambda: results_df)[['latitude', 'longitude']], "values")
_l_(383171)
trees_tree = _c_(383175, _n_(383172, "KDTree", lambda: KDTree), _n_(383173, "trees_xys", lambda: trees_xys), distance_metric='Arc', radius=_n_(383174, "RADIUS_EARTH_MILES", lambda: RADIUS_EARTH_MILES))
_l_(383176)