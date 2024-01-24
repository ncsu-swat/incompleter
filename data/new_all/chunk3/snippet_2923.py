# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58225629/typeerror-in-python-3
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class TSP:
    _l_(545275)

    def __init__(self, initial_node, adjacency_matrix):
        _l_(545241)

        _n_(545235, "self", lambda: self).initial_node = _n_(545236, "initial_node", lambda: initial_node)
        _l_(545237)
        _n_(545238, "self", lambda: self).adjacency_matrix = _n_(545239, "adjacency_matrix", lambda: adjacency_matrix)
        _l_(545240)

    stack = {"cost": {}, "distances": {}}
    _l_(545242)

    def distance(self, start_node, end_node):
        _l_(545253)

        _a_(545244, _n_(545243, "self", lambda: self), "stack")["distances"]["dist%s-%s" %(_n_(545245, "start_node", lambda: start_node), _n_(545246, "end_node", lambda: end_node))] = _a_(545248, _n_(545247, "self", lambda: self), "adjacency")-_n_(545249, "matrix", lambda: matrix)[_n_(545250, "start_node", lambda: start_node)][_n_(545251, "end_node", lambda: end_node)]
        _l_(545252)

    def cost(self, visit_nodes, end_node_cost):
        _l_(545274)

        if _c_(545256, _n_(545254, "len", lambda: len), _n_(545255, "visit_nodes", lambda: visit_nodes)) == 2:
            _l_(545268)

            node_set = _c_(545260, _a_(545258, _n_(545257, "visit_nodes", lambda: visit_nodes), "remove"), _n_(545259, "end_node_cost", lambda: end_node_cost))
            _l_(545261)
            _c_(545266, _a_(545263, _n_(545262, "self", lambda: self), "distance"), _n_(545264, "node_set", lambda: node_set)[0], _n_(545265, "end_node_cost", lambda: end_node_cost))
            _l_(545267)
        _c_(545272, _n_(545269, "print", lambda: print), _a_(545271, _n_(545270, "self", lambda: self), "stack"))
        _l_(545273)


test = _c_(545277, _n_(545276, "TSP", lambda: TSP), 1, [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]])
_l_(545278)

_c_(545283, _n_(545279, "print", lambda: print), _c_(545282, _a_(545281, _n_(545280, "test", lambda: test), "cost"), [1, 2], 2))
_l_(545284)