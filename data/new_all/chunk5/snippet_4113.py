# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62785773/attributeerror-numpy-ndarray-object-has-no-attribute-assert-compile-was-cal
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
result = _c_(700212, _a_(700211, _c_(700210, _a_(700206, _n_(700205, "np", lambda: np), "apply_along_axis"), _n_(700207, "augment", lambda: augment), axis=1, arr=_n_(700208, "X", lambda: X)[_n_(700209, "C3", lambda: C3)]), "reshape"), -1, 187)
_l_(700213)
classe = _c_(700219, _a_(700215, _n_(700214, "np", lambda: np), "ones"), shape=(_a_(700217, _n_(700216, "result", lambda: result), "shape")[0],), dtype=_n_(700218, "int", lambda: int))*3
_l_(700220)
X = _c_(700225, _a_(700222, _n_(700221, "np", lambda: np), "vstack"), [_n_(700223, "X", lambda: X), _n_(700224, "result", lambda: result)])
_l_(700226)
y = _c_(700231, _a_(700228, _n_(700227, "np", lambda: np), "hstack"), [_n_(700229, "y", lambda: y), _n_(700230, "classe", lambda: classe)])
_l_(700232)
subC0 = _c_(700237, _a_(700235, _a_(700234, _n_(700233, "np", lambda: np), "random"), "choice"), _n_(700236, "C0", lambda: C0), 800)
_l_(700238)
subC1 = _c_(700243, _a_(700241, _a_(700240, _n_(700239, "np", lambda: np), "random"), "choice"), _n_(700242, "C1", lambda: C1), 800)
_l_(700244)
subC2 = _c_(700249, _a_(700247, _a_(700246, _n_(700245, "np", lambda: np), "random"), "choice"), _n_(700248, "C2", lambda: C2), 800)
_l_(700250)
subC3 = _c_(700255, _a_(700253, _a_(700252, _n_(700251, "np", lambda: np), "random"), "choice"), _n_(700254, "C3", lambda: C3), 800)
_l_(700256)
subC4 = _c_(700261, _a_(700259, _a_(700258, _n_(700257, "np", lambda: np), "random"), "choice"), _n_(700260, "C4", lambda: C4), 800)
_l_(700262)
X_test = _c_(700275, _a_(700264, _n_(700263, "np", lambda: np), "vstack"), [_n_(700265, "X", lambda: X)[_n_(700266, "subC0", lambda: subC0)], _n_(700267, "X", lambda: X)[_n_(700268, "subC1", lambda: subC1)], _n_(700269, "X", lambda: X)[_n_(700270, "subC2", lambda: subC2)], _n_(700271, "X", lambda: X)[_n_(700272, "subC3", lambda: subC3)], _n_(700273, "X", lambda: X)[_n_(700274, "subC4", lambda: subC4)]])
_l_(700276)
y_test = _c_(700289, _a_(700278, _n_(700277, "np", lambda: np), "hstack"), [_n_(700279, "y", lambda: y)[_n_(700280, "subC0", lambda: subC0)], _n_(700281, "y", lambda: y)[_n_(700282, "subC1", lambda: subC1)], _n_(700283, "y", lambda: y)[_n_(700284, "subC2", lambda: subC2)], _n_(700285, "y", lambda: y)[_n_(700286, "subC3", lambda: subC3)], _n_(700287, "y", lambda: y)[_n_(700288, "subC4", lambda: subC4)]])
_l_(700290)

X_train = _c_(700299, _a_(700292, _n_(700291, "np", lambda: np), "delete"), _n_(700293, "X", lambda: X), [_n_(700294, "subC0", lambda: subC0), _n_(700295, "subC1", lambda: subC1), _n_(700296, "subC2", lambda: subC2), _n_(700297, "subC3", lambda: subC3), _n_(700298, "subC4", lambda: subC4)], axis=0)
_l_(700300)
y_train = _c_(700309, _a_(700302, _n_(700301, "np", lambda: np), "delete"), _n_(700303, "y", lambda: y), [_n_(700304, "subC0", lambda: subC0), _n_(700305, "subC1", lambda: subC1), _n_(700306, "subC2", lambda: subC2), _n_(700307, "subC3", lambda: subC3), _n_(700308, "subC4", lambda: subC4)], axis=0)
_l_(700310)

X_train, y_train = _c_(700314, _n_(700311, "shuffle", lambda: shuffle), _n_(700312, "X_train", lambda: X_train), _n_(700313, "y_train", lambda: y_train), random_state=0)
_l_(700315)
X_test, y_test = _c_(700319, _n_(700316, "shuffle", lambda: shuffle), _n_(700317, "X_test", lambda: X_test), _n_(700318, "y_test", lambda: y_test), random_state=0)
_l_(700320)

del X
_l_(700321)
del y
_l_(700322)
X_train = _c_(700326, _a_(700324, _n_(700323, "np", lambda: np), "expand_dims"), _n_(700325, "X_train", lambda: X_train), 2)
_l_(700327)
X_test = _c_(700331, _a_(700329, _n_(700328, "np", lambda: np), "expand_dims"), _n_(700330, "X_test", lambda: X_test), 2)
_l_(700332)
history = _c_(700343, _a_(700336, _a_(700335, _a_(700334, _n_(700333, "tensorflow", lambda: tensorflow), "keras"), "Model"), "fit"), _n_(700337, "X_train", lambda: X_train), _n_(700338, "y_train", lambda: y_train), 
                epochs=75, 
                batch_size=_n_(700339, "batch_size", lambda: batch_size), 
                verbose=2, 
                validation_data=(_n_(700340, "X_test", lambda: X_test), _n_(700341, "y_test", lambda: y_test)), 
                callbacks= [_n_(700342, "lrate", lambda: lrate)])
_l_(700344)