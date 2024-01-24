# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/45569763/attributeerror-list-object-has-no-attribute-create-png
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(376933)

except ImportError:
    pass
try:
    from sklearn import linear_model, datasets, tree
    _l_(376935)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(376937)

except ImportError:
    pass
iris = _c_(376940, _a_(376939, _n_(376938, "datasets", lambda: datasets), "load_iris"))
_l_(376941)
f = _c_(376943, _n_(376942, "open", lambda: open), 'decision_tree_data.txt')
_l_(376944)
x_train = []
_l_(376945)
y_train = []
_l_(376946)
for line in _n_(376947, "f", lambda: f):
    _l_(376967)

    line = _c_(376955, _a_(376949, _n_(376948, "np", lambda: np), "asarray"), _c_(376952, _a_(376951, _n_(376950, "line", lambda: line), "split")),dtype = _a_(376954, _n_(376953, "np", lambda: np), "float32"))
    _l_(376956)
    _c_(376960, _a_(376958, _n_(376957, "x_train", lambda: x_train), "append"), _n_(376959, "line", lambda: line)[:-1])
    _l_(376961)
    _c_(376965, _a_(376963, _n_(376962, "y_train", lambda: y_train), "append"), _n_(376964, "line", lambda: line)[:-1])
    _l_(376966)
x_train = _c_(376971, _a_(376969, _n_(376968, "np", lambda: np), "asmatrix"), _n_(376970, "x_train", lambda: x_train))
_l_(376972)
y_train = _c_(376976, _a_(376974, _n_(376973, "np", lambda: np), "asmatrix"), _n_(376975, "y_train", lambda: y_train))
_l_(376977)
model = _c_(376980, _a_(376979, _n_(376978, "tree", lambda: tree), "DecisionTreeClassifier"))
_l_(376981)
_c_(376986, _a_(376983, _n_(376982, "model", lambda: model), "fit"), _n_(376984, "x_train", lambda: x_train),_n_(376985, "y_train", lambda: y_train))
_l_(376987)
try:
    from sklearn.externals.six import StringIO
    _l_(376989)

except ImportError:
    pass
try:
    import pydot
    _l_(376991)

except ImportError:
    pass
try:
    from IPython.display import Image
    _l_(376993)

except ImportError:
    pass
dot_data = _c_(376995, _n_(376994, "StringIO", lambda: StringIO))
_l_(376996)
_c_(377005, _a_(376998, _n_(376997, "tree", lambda: tree), "export_graphviz"), _n_(376999, "model", lambda: model), out_file=_n_(377000, "dot_data", lambda: dot_data),  
                     feature_names=_a_(377002, _n_(377001, "iris", lambda: iris), "feature_names"),  
                     class_names=_a_(377004, _n_(377003, "iris", lambda: iris), "target_names"),  
                     filled=True, rounded=True,  
                     special_characters=True)  
_l_(377006)  
graph = _c_(377012, _a_(377008, _n_(377007, "pydot", lambda: pydot), "graph_from_dot_data"), _c_(377011, _a_(377010, _n_(377009, "dot_data", lambda: dot_data), "getvalue"))) 
_l_(377013) 
_c_(377018, _n_(377014, "Image", lambda: Image), _c_(377017, _a_(377016, _n_(377015, "graph", lambda: graph), "create_png")))
_l_(377019)