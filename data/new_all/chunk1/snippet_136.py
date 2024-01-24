# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/40069585/how-can-i-fix-attributeerror-dict-values-object-has-no-attribute-count
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import networkx as nx
    _l_(381835)

except ImportError:
    pass
try:
    import pylab as plt
    _l_(381837)

except ImportError:
    pass

webg = _c_(381844, _a_(381839, _n_(381838, "nx", lambda: nx), "read_edgelist"), 'web-graph.txt',create_using=_c_(381842, _a_(381841, _n_(381840, "nx", lambda: nx), "DiGraph")),nodetype=_n_(381843, "int", lambda: int))
_l_(381845)
in_degrees = _c_(381848, _a_(381847, _n_(381846, "webg", lambda: webg), "in_degree"))
_l_(381849)
in_values = _c_(381856, _n_(381850, "sorted", lambda: sorted), _c_(381855, _n_(381851, "set", lambda: set), _c_(381854, _a_(381853, _n_(381852, "in_degrees", lambda: in_degrees), "values"))))
_l_(381857)
in_hist = [_c_(381863, _a_(381861, _c_(381860, _a_(381859, _n_(381858, "in_degrees", lambda: in_degrees), "values")), "count"), _n_(381862, "x", lambda: x))for x in _n_(381864, "in_values", lambda: in_values)]
_l_(381865)