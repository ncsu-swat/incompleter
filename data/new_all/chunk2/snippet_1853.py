# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50435311/program-is-not-working-typeerror-fit-missing-1-required-positional-argument
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn import tree
    _l_(434864)

except ImportError:
    pass
try:
    from sklearn.datasets import load_iris
    _l_(434866)

except ImportError:
    pass
iris=_c_(434868, _n_(434867, "load_iris", lambda: load_iris))
_l_(434869)
_c_(434872, _n_(434870, "dir", lambda: dir), _n_(434871, "iris", lambda: iris))
_l_(434873)
#output data to traixn setosa,versicolor and virginica
x=_a_(434875, _n_(434874, "iris", lambda: iris), "data")
_l_(434876)
#fetching data
x=_c_(434882, _a_(434878, _n_(434877, "np", lambda: np), "delete"), _n_(434879, "x", lambda: x), _a_(434881, _n_(434880, "np", lambda: np), "s_")[::50], 0)
_l_(434883)
#print(x)
y=_a_(434885, _n_(434884, "iris", lambda: iris), "target")
_l_(434886)
#featching output
y=_c_(434892, _a_(434888, _n_(434887, "np", lambda: np), "delete"), _n_(434889, "y", lambda: y), _a_(434891, _n_(434890, "np", lambda: np), "s_")[::50], 0)
_l_(434893)
algo=_a_(434895, _n_(434894, "tree", lambda: tree), "DecisionTreeClassifier")
_l_(434896)