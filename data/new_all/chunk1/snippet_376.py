# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/47242694/attributeerror-module-sklearn-datasets-has-no-attribute-load-titanic
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from sklearn import datasets
    _l_(414313)

except ImportError:
    pass
titanic = _c_(414316, _a_(414315, _n_(414314, "datasets", lambda: datasets), "load_titanic"))
_l_(414317)