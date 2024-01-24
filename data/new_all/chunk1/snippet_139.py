# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53017174/attributeerror-module-networkx-algorithms-community-has-no-attribute-best-pa
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import networkx as nx
    _l_(387283)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(387285)

except ImportError:
    pass
try:
    from networkx.algorithms import community
    _l_(387287)

except ImportError:
    pass
try:
    from networkx.algorithms.community.centrality import girvan_newman
    _l_(387289)

except ImportError:
    pass

G_fb = _c_(387296, _a_(387291, _n_(387290, "nx", lambda: nx), "read_edgelist"), "./facebook_combined.txt",create_using = _c_(387294, _a_(387293, _n_(387292, "nx", lambda: nx), "Graph")), nodetype=_n_(387295, "int", lambda: int))
_l_(387297)

parts = _c_(387301, _a_(387299, _n_(387298, "community", lambda: community), "best_partition"), _n_(387300, "G_fb", lambda: G_fb))
_l_(387302)
values = [_c_(387306, _a_(387304, _n_(387303, "parts", lambda: parts), "get"), _n_(387305, "node", lambda: node)) for node in _c_(387309, _a_(387308, _n_(387307, "G_fb", lambda: G_fb), "nodes"))]
_l_(387310)