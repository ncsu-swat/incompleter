# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60029383/typeerror-not-supported-between-instances-of-dict-and-dict-python-3-co
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nodes=_c_(375039, _a_(375038, _n_(375037, "random", lambda: random), "randint"), 47,52)
_l_(375040)
p=_c_(375043, _a_(375042, _n_(375041, "random", lambda: random), "uniform"), 0.05,0.08)
_l_(375044)
name="Erdos-Renyi random weighted graph"
_l_(375045)
G=_c_(375050, _a_(375047, _n_(375046, "nx", lambda: nx), "erdos_renyi_graph"), _n_(375048, "nodes", lambda: nodes),_n_(375049, "p", lambda: p))
_l_(375051)
maxw=_c_(375054, _a_(375053, _n_(375052, "random", lambda: random), "randint"), 7,12)
_l_(375055)
weight=_c_(375059, _n_(375056, "weight_attr", lambda: weight_attr), _n_(375057, "G", lambda: G),_n_(375058, "maxw", lambda: maxw))
_l_(375060)
w_edges=[(_n_(375061, "x", lambda: x),_n_(375062, "y", lambda: y),_n_(375063, "z", lambda: z)) for (x,y),z in _c_(375066, _a_(375065, _n_(375064, "weight", lambda: weight), "items"))]
_l_(375067)
_c_(375071, _a_(375069, _n_(375068, "G", lambda: G), "add_weighted_edges_from"), _n_(375070, "w_edges", lambda: w_edges))
_l_(375072)
G=_c_(375077, _a_(375074, _n_(375073, "nx", lambda: nx), "Graph"), _n_(375075, "G", lambda: G),name=_n_(375076, "name", lambda: name))
_l_(375078)
_c_(375094, _n_(375079, "print", lambda: print), "Graph G is a %s with %i nodes, p=%.3f and %i edges\n" %(_c_(375082, _n_(375080, "str", lambda: str), _n_(375081, "G", lambda: G)),_c_(375087, _n_(375083, "len", lambda: len), _c_(375086, _a_(375085, _n_(375084, "G", lambda: G), "nodes"))),_n_(375088, "p", lambda: p),_c_(375093, _n_(375089, "len", lambda: len), _c_(375092, _a_(375091, _n_(375090, "G", lambda: G), "edges")))))
_l_(375095)

res = _c_(375110, _n_(375096, "list", lambda: list), _c_(375109, _n_(375097, "sorted", lambda: sorted), _c_(375102, _n_(375098, "Counter", lambda: Counter), _c_(375101, _a_(375100, _n_(375099, "G", lambda: G), "edges"))), key=_a_(375108, _c_(375107, _n_(375103, "Counter", lambda: Counter), _c_(375106, _a_(375105, _n_(375104, "G", lambda: G), "edges"))), "__getitem__"), reverse=True))
_l_(375111)
for i in _n_(375112, "res", lambda: res):
    _l_(375123)

    _c_(375121, _n_(375113, "print", lambda: print), "Edge", _n_(375114, "i", lambda: i), "has weight", _c_(375119, _n_(375115, "Counter", lambda: Counter), _c_(375118, _a_(375117, _n_(375116, "G", lambda: G), "edges")))[_n_(375120, "i", lambda: i)]['weight'])
    _l_(375122)