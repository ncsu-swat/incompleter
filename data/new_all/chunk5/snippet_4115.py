# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62785773/attributeerror-numpy-ndarray-object-has-no-attribute-assert-compile-was-cal
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
result = _c_(650488, _a_(650487, _c_(650486, _a_(650482, _n_(650481, "np", lambda: np), "apply_along_axis"), _n_(650483, "augment", lambda: augment), axis=1, arr=_n_(650484, "X", lambda: X)[_n_(650485, "C3", lambda: C3)]), "reshape"), -1, 187)
_l_(650489)
classe = _c_(650495, _a_(650491, _n_(650490, "np", lambda: np), "ones"), shape=(_a_(650493, _n_(650492, "result", lambda: result), "shape")[0],), dtype=_n_(650494, "int", lambda: int))*3
_l_(650496)
X = _c_(650501, _a_(650498, _n_(650497, "np", lambda: np), "vstack"), [_n_(650499, "X", lambda: X), _n_(650500, "result", lambda: result)])
_l_(650502)
y = _c_(650507, _a_(650504, _n_(650503, "np", lambda: np), "hstack"), [_n_(650505, "y", lambda: y), _n_(650506, "classe", lambda: classe)])
_l_(650508)
subC0 = _c_(650513, _a_(650511, _a_(650510, _n_(650509, "np", lambda: np), "random"), "choice"), _n_(650512, "C0", lambda: C0), 800)
_l_(650514)
subC1 = _c_(650519, _a_(650517, _a_(650516, _n_(650515, "np", lambda: np), "random"), "choice"), _n_(650518, "C1", lambda: C1), 800)
_l_(650520)
subC2 = _c_(650525, _a_(650523, _a_(650522, _n_(650521, "np", lambda: np), "random"), "choice"), _n_(650524, "C2", lambda: C2), 800)
_l_(650526)
subC3 = _c_(650531, _a_(650529, _a_(650528, _n_(650527, "np", lambda: np), "random"), "choice"), _n_(650530, "C3", lambda: C3), 800)
_l_(650532)
subC4 = _c_(650537, _a_(650535, _a_(650534, _n_(650533, "np", lambda: np), "random"), "choice"), _n_(650536, "C4", lambda: C4), 800)
_l_(650538)
X_test = _c_(650551, _a_(650540, _n_(650539, "np", lambda: np), "vstack"), [_n_(650541, "X", lambda: X)[_n_(650542, "subC0", lambda: subC0)], _n_(650543, "X", lambda: X)[_n_(650544, "subC1", lambda: subC1)], _n_(650545, "X", lambda: X)[_n_(650546, "subC2", lambda: subC2)], _n_(650547, "X", lambda: X)[_n_(650548, "subC3", lambda: subC3)], _n_(650549, "X", lambda: X)[_n_(650550, "subC4", lambda: subC4)]])
_l_(650552)
y_test = _c_(650565, _a_(650554, _n_(650553, "np", lambda: np), "hstack"), [_n_(650555, "y", lambda: y)[_n_(650556, "subC0", lambda: subC0)], _n_(650557, "y", lambda: y)[_n_(650558, "subC1", lambda: subC1)], _n_(650559, "y", lambda: y)[_n_(650560, "subC2", lambda: subC2)], _n_(650561, "y", lambda: y)[_n_(650562, "subC3", lambda: subC3)], _n_(650563, "y", lambda: y)[_n_(650564, "subC4", lambda: subC4)]])
_l_(650566)

X_train = _c_(650575, _a_(650568, _n_(650567, "np", lambda: np), "delete"), _n_(650569, "X", lambda: X), [_n_(650570, "subC0", lambda: subC0), _n_(650571, "subC1", lambda: subC1), _n_(650572, "subC2", lambda: subC2), _n_(650573, "subC3", lambda: subC3), _n_(650574, "subC4", lambda: subC4)], axis=0)
_l_(650576)
y_train = _c_(650585, _a_(650578, _n_(650577, "np", lambda: np), "delete"), _n_(650579, "y", lambda: y), [_n_(650580, "subC0", lambda: subC0), _n_(650581, "subC1", lambda: subC1), _n_(650582, "subC2", lambda: subC2), _n_(650583, "subC3", lambda: subC3), _n_(650584, "subC4", lambda: subC4)], axis=0)
_l_(650586)

X_train, y_train = _c_(650590, _n_(650587, "shuffle", lambda: shuffle), _n_(650588, "X_train", lambda: X_train), _n_(650589, "y_train", lambda: y_train), random_state=0)
_l_(650591)
X_test, y_test = _c_(650595, _n_(650592, "shuffle", lambda: shuffle), _n_(650593, "X_test", lambda: X_test), _n_(650594, "y_test", lambda: y_test), random_state=0)
_l_(650596)

del X
_l_(650597)
del y
_l_(650598)
X_train = _c_(650602, _a_(650600, _n_(650599, "np", lambda: np), "expand_dims"), _n_(650601, "X_train", lambda: X_train), 2)
_l_(650603)
X_test = _c_(650607, _a_(650605, _n_(650604, "np", lambda: np), "expand_dims"), _n_(650606, "X_test", lambda: X_test), 2)
_l_(650608)
history = _c_(650619, _a_(650612, _a_(650611, _a_(650610, _n_(650609, "tensorflow", lambda: tensorflow), "keras"), "Model"), "fit"), _n_(650613, "X_train", lambda: X_train), _n_(650614, "y_train", lambda: y_train), 
                epochs=75, 
                batch_size=_n_(650615, "batch_size", lambda: batch_size), 
                verbose=2, 
                validation_data=(_n_(650616, "X_test", lambda: X_test), _n_(650617, "y_test", lambda: y_test)), 
                callbacks= [_n_(650618, "lrate", lambda: lrate)])
_l_(650620)