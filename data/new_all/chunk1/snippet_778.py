# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55661668/attributeerror-get-numeric-data-iris-dataset
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(378643)

except ImportError:
    pass
try:
    import numpy
    _l_(378645)

except ImportError:
    pass
try:
    import mglearn
    _l_(378647)

except ImportError:
    pass
try:
    from sklearn.datasets import load_iris
    _l_(378649)

except ImportError:
    pass
try:
    from sklearn.model_selection import train_test_split
    _l_(378651)

except ImportError:
    pass
iri = _c_(378653, _n_(378652, "load_iris", lambda: load_iris))
_l_(378654)

xTrain, xTest, yTrain, yTest = _c_(378658, _n_(378655, "train_test_split", lambda: train_test_split), _n_(378656, "iri", lambda: iri)['data'], _n_(378657, "iri", lambda: iri)['target'], random_state=0)
_l_(378659)

_c_(378663, _n_(378660, "print", lambda: print), _a_(378662, _n_(378661, "xTrain", lambda: xTrain), "shape"))
_l_(378664)

iriFrame = _c_(378670, _a_(378666, _n_(378665, "pd", lambda: pd), "DataFrame"), _n_(378667, "xTrain", lambda: xTrain), columns=_a_(378669, _n_(378668, "iri", lambda: iri), "feature_names"))
_l_(378671)
_c_(378679, _a_(378674, _a_(378673, _n_(378672, "pd", lambda: pd), "plotting"), "scatter_matrix"), _n_(378675, "iri", lambda: iri), c=_n_(378676, "yTrain", lambda: yTrain), figsize=(15, 15), marker='o', hist_kwds={'bins':20}, s=60, alpha=.8, cmap=_a_(378678, _n_(378677, "mglearn", lambda: mglearn), "cm3"))
_l_(378680)
#print('Keys: \n{}'.format(iri.keys()))
#print(iri['data'])
#print(iri['feature_names'])