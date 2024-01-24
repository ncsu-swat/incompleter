# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54564583/how-to-fix-typeerror-must-be-real-number-not-numpy-str-occurred-at-inde
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
radius_in_miles = 0.5
_l_(394173)

def get_complaint_count(r):
    _l_(394194)

    xy = _n_(394174, "r", lambda: r)['latitude'], _n_(394175, "r", lambda: r)['longitude']
    _l_(394176)
    distances, indices = _c_(394182, _a_(394178, _n_(394177, "trees_tree", lambda: trees_tree), "query"), _n_(394179, "xy", lambda: xy), k=_n_(394180, "trees_count", lambda: trees_count), distance_upper_bound=_n_(394181, "radius_in_miles", lambda: radius_in_miles))
    _l_(394183)
    indices = _n_(394184, "indices", lambda: indices)[~_c_(394188, _a_(394186, _n_(394185, "np", lambda: np), "isnan"), _n_(394187, "indices", lambda: indices))]
    _l_(394189)
    aux = _c_(394192, _n_(394190, "len", lambda: len), _n_(394191, "indices", lambda: indices))
    _l_(394193)
    return aux

_n_(394195, "treeLocations", lambda: treeLocations)['# of Complaints within 0.5 miles'] = _c_(394199, _a_(394197, _n_(394196, "treeLocations", lambda: treeLocations), "apply"), _n_(394198, "get_complaint_count", lambda: get_complaint_count),axis=1)
_l_(394200)

_n_(394201, "treeLocations", lambda: treeLocations)
_l_(394202)