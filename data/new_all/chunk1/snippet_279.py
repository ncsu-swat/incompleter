# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51852502/error-message-when-using-pydot-to-save-image-attributeerror-module-os-has-no
# Import tools needed for visualization
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn.tree import export_graphviz
    _l_(396456)

except ImportError:
    pass
try:
    import pydot
    _l_(396458)

except ImportError:
    pass
# Pull out one tree from the forest
tree = _a_(396460, _n_(396459, "rf", lambda: rf), "estimators_")[5]
_l_(396461)
# Export the image to a dot file
_c_(396465, _n_(396462, "export_graphviz", lambda: export_graphviz), _n_(396463, "tree", lambda: tree), out_file = 'tree.dot', feature_names = _n_(396464, "feature_list", lambda: feature_list), rounded = True, precision = 1)
_l_(396466)
# Use dot file to create a graph
(graph, ) = _c_(396469, _a_(396468, _n_(396467, "pydot", lambda: pydot), "graph_from_dot_file"), 'tree.dot')
_l_(396470)
_c_(396473, _a_(396472, _n_(396471, "graph", lambda: graph), "write_png"), 'tree.png')
_l_(396474)