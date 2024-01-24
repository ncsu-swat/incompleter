# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60029383/typeerror-not-supported-between-instances-of-dict-and-dict-python-3-co
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
nodes=_c_(365349, _a_(365348, _n_(365347, "random", lambda: random), "randint"), 47,52)
_l_(365350)
p=_c_(365353, _a_(365352, _n_(365351, "random", lambda: random), "uniform"), 0.05,0.08)
_l_(365354)
name="Erdos-Renyi random weighted graph"
_l_(365355)
G=_c_(365360, _a_(365357, _n_(365356, "nx", lambda: nx), "erdos_renyi_graph"), _n_(365358, "nodes", lambda: nodes),_n_(365359, "p", lambda: p))
_l_(365361)
maxw=_c_(365364, _a_(365363, _n_(365362, "random", lambda: random), "randint"), 7,12)
_l_(365365)
weight=_c_(365369, _n_(365366, "weight_attr", lambda: weight_attr), _n_(365367, "G", lambda: G),_n_(365368, "maxw", lambda: maxw))
_l_(365370)
w_edges=[(_n_(365371, "x", lambda: x),_n_(365372, "y", lambda: y),_n_(365373, "z", lambda: z)) for (x,y),z in _c_(365376, _a_(365375, _n_(365374, "weight", lambda: weight), "items"))]
_l_(365377)
_c_(365381, _a_(365379, _n_(365378, "G", lambda: G), "add_weighted_edges_from"), _n_(365380, "w_edges", lambda: w_edges))
_l_(365382)
G=_c_(365387, _a_(365384, _n_(365383, "nx", lambda: nx), "Graph"), _n_(365385, "G", lambda: G),name=_n_(365386, "name", lambda: name))
_l_(365388)
_c_(365404, _n_(365389, "print", lambda: print), "Graph G is a %s with %i nodes, p=%.3f and %i edges\n" %(_c_(365392, _n_(365390, "str", lambda: str), _n_(365391, "G", lambda: G)),_c_(365397, _n_(365393, "len", lambda: len), _c_(365396, _a_(365395, _n_(365394, "G", lambda: G), "nodes"))),_n_(365398, "p", lambda: p),_c_(365403, _n_(365399, "len", lambda: len), _c_(365402, _a_(365401, _n_(365400, "G", lambda: G), "edges")))))
_l_(365405)

res = _c_(365420, _n_(365406, "list", lambda: list), _c_(365419, _n_(365407, "sorted", lambda: sorted), _c_(365412, _n_(365408, "Counter", lambda: Counter), _c_(365411, _a_(365410, _n_(365409, "G", lambda: G), "edges"))), key=_a_(365418, _c_(365417, _n_(365413, "Counter", lambda: Counter), _c_(365416, _a_(365415, _n_(365414, "G", lambda: G), "edges"))), "__getitem__"), reverse=True))
_l_(365421)
for i in _n_(365422, "res", lambda: res):
    _l_(365433)

    _c_(365431, _n_(365423, "print", lambda: print), "Edge", _n_(365424, "i", lambda: i), "has weight", _c_(365429, _n_(365425, "Counter", lambda: Counter), _c_(365428, _a_(365427, _n_(365426, "G", lambda: G), "edges")))[_n_(365430, "i", lambda: i)]['weight'])
    _l_(365432)