# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75897778/attributeerror-module-networkx-has-no-attribute-info
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import networkx as nx
    _l_(421849)

except ImportError:
    pass
G = _c_(421855, _a_(421851, _n_(421850, "nx", lambda: nx), "read_edgelist"), 'webpages.txt', create_using=_c_(421854, _a_(421853, _n_(421852, "nx", lambda: nx), "DiGraph")))
_l_(421856)
_c_(421862, _n_(421857, "print", lambda: print), _c_(421861, _a_(421859, _n_(421858, "nx", lambda: nx), "info"), _n_(421860, "G", lambda: G)))
_l_(421863)