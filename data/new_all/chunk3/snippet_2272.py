# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/53956264/typeerror-while-looping-through-dictionary-key-and-items
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
BDT_param_grid1 ={"learning_rate": _c_(525660, _a_(525659, _n_(525658, "np", lambda: np), "arange"), 0.1,1.0,0.1),
                  "n_estimators": _c_(525663, _a_(525662, _n_(525661, "np", lambda: np), "arange"), 1, 1000, 10),
                  "base_estimator__min_samples_split": _c_(525666, _a_(525665, _n_(525664, "np", lambda: np), "arange"), 0.1,1.0,0.1),
                  "base_estimator__min_samples_leaf": _c_(525669, _a_(525668, _n_(525667, "np", lambda: np), "arange"), 1,60,1),
                  "base_estimator__max_leaf_nodes": _c_(525672, _a_(525671, _n_(525670, "np", lambda: np), "arange"), 2,60,1),
                  "base_estimator__min_weight_fraction_leaf": _c_(525675, _a_(525674, _n_(525673, "np", lambda: np), "arange"), 0.1, 0.4, 0.1),
                  "base_estimator__max_features": _c_(525678, _a_(525677, _n_(525676, "np", lambda: np), "arange"), 0.1,1,0.1),
                  "base_estimator__max_depth": _c_(525681, _a_(525680, _n_(525679, "np", lambda: np), "arange"), 1, 28, 1)}
_l_(525682)

for key,items in _c_(525686, _a_(525684, _n_(525683, "dict", lambda: dict), "items"), _n_(525685, "BDT_param_grid1", lambda: BDT_param_grid1)):
    _l_(525692)

    _c_(525690, _n_(525687, "print", lambda: print), _n_(525688, "key", lambda: key),_n_(525689, "items", lambda: items))
    _l_(525691)