# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59414732/typeerror-can-only-concatenate-list-not-tuple-to-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
fde = _n_(654534, "fde", lambda: fde)[_n_(654535, "features", lambda: features)]
_l_(654536)
locations = []
_l_(654537)
for row in _c_(654540, _a_(654539, _n_(654538, "fde", lambda: fde), "iterrows")):
    _l_(654569)

    temp_elite = _n_(654541, "fne", lambda: fne)[_n_(654542, "features", lambda: features)]
    _l_(654543)
    temp_elite = _c_(654547, _a_(654545, _n_(654544, "temp_elite", lambda: temp_elite), "append"), _n_(654546, "row", lambda: row))
    _l_(654548)
    tree = _c_(654551, _n_(654549, "KDTree", lambda: KDTree), _n_(654550, "temp_elite", lambda: temp_elite), metric='euclidean')
    _l_(654552)
    dist, ind = _c_(654556, _a_(654554, _n_(654553, "tree", lambda: tree), "query"), _n_(654555, "temp_elite", lambda: temp_elite), k=4)
    _l_(654557)
    _c_(654560, _n_(654558, "print", lambda: print), _n_(654559, "ind", lambda: ind))
    _l_(654561)
    _c_(654567, _a_(654563, _n_(654562, "locations", lambda: locations), "append"), _c_(654566, _a_(654565, _n_(654564, "ind", lambda: ind), "tail"), 1))
    _l_(654568)
_c_(654572, _n_(654570, "print", lambda: print), _n_(654571, "locations", lambda: locations))
_l_(654573)