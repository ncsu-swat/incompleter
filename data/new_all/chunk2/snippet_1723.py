# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60702740/attributeerror-module-networkx-has-no-attribute-generate-graph6
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import networkx as nx
    _l_(475128)

except ImportError:
    pass
G=_c_(475131, _a_(475130, _n_(475129, "nx", lambda: nx), "Graph"))
_l_(475132)
_c_(475135, _a_(475134, _n_(475133, "G", lambda: G), "add_edges_from"), [(2, 3),(4, 5), (1, 3), (1, 2), (1, 5), (1, 4), (2, 4), (3, 5), (2, 5), (3, 4)])
_l_(475136)
_c_(475140, _a_(475138, _n_(475137, "nx", lambda: nx), "generate_graph6"), _n_(475139, "G", lambda: G))
_l_(475141)