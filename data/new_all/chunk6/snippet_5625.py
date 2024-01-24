# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60029383/typeerror-not-supported-between-instances-of-dict-and-dict-python-3-co
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nodes=_c_(345632, _a_(345631, _n_(345630, "random", lambda: random), "randint"), 47,52)
_l_(345633)
p=_c_(345636, _a_(345635, _n_(345634, "random", lambda: random), "uniform"), 0.05,0.08)
_l_(345637)
name="Erdos-Renyi random weighted graph"
_l_(345638)
G=_c_(345643, _a_(345640, _n_(345639, "nx", lambda: nx), "erdos_renyi_graph"), _n_(345641, "nodes", lambda: nodes),_n_(345642, "p", lambda: p))
_l_(345644)
maxw=_c_(345647, _a_(345646, _n_(345645, "random", lambda: random), "randint"), 7,12)
_l_(345648)
weight=_c_(345652, _n_(345649, "weight_attr", lambda: weight_attr), _n_(345650, "G", lambda: G),_n_(345651, "maxw", lambda: maxw))
_l_(345653)
w_edges=[(_n_(345654, "x", lambda: x),_n_(345655, "y", lambda: y),_n_(345656, "z", lambda: z)) for (x,y),z in _c_(345659, _a_(345658, _n_(345657, "weight", lambda: weight), "items"))]
_l_(345660)
_c_(345664, _a_(345662, _n_(345661, "G", lambda: G), "add_weighted_edges_from"), _n_(345663, "w_edges", lambda: w_edges))
_l_(345665)
G=_c_(345670, _a_(345667, _n_(345666, "nx", lambda: nx), "Graph"), _n_(345668, "G", lambda: G),name=_n_(345669, "name", lambda: name))
_l_(345671)
_c_(345687, _n_(345672, "print", lambda: print), "Graph G is a %s with %i nodes, p=%.3f and %i edges\n" %(_c_(345675, _n_(345673, "str", lambda: str), _n_(345674, "G", lambda: G)),_c_(345680, _n_(345676, "len", lambda: len), _c_(345679, _a_(345678, _n_(345677, "G", lambda: G), "nodes"))),_n_(345681, "p", lambda: p),_c_(345686, _n_(345682, "len", lambda: len), _c_(345685, _a_(345684, _n_(345683, "G", lambda: G), "edges")))))
_l_(345688)

res = _c_(345703, _n_(345689, "list", lambda: list), _c_(345702, _n_(345690, "sorted", lambda: sorted), _c_(345695, _n_(345691, "Counter", lambda: Counter), _c_(345694, _a_(345693, _n_(345692, "G", lambda: G), "edges"))), key=_a_(345701, _c_(345700, _n_(345696, "Counter", lambda: Counter), _c_(345699, _a_(345698, _n_(345697, "G", lambda: G), "edges"))), "__getitem__"), reverse=True))
_l_(345704)
for i in _n_(345705, "res", lambda: res):
    _l_(345716)

    _c_(345714, _n_(345706, "print", lambda: print), "Edge", _n_(345707, "i", lambda: i), "has weight", _c_(345712, _n_(345708, "Counter", lambda: Counter), _c_(345711, _a_(345710, _n_(345709, "G", lambda: G), "edges")))[_n_(345713, "i", lambda: i)]['weight'])
    _l_(345715)