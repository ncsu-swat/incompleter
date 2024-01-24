# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75126511/sklearn-with-joblib-raises-attributeerror-nonetype-object-has-no-attribute
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(406324)

except ImportError:
    pass
try:
    from joblib import Parallel, delayed, parallel_backend
    _l_(406326)

except ImportError:
    pass
try:
    from sklearn.neighbors import NearestNeighbors
    _l_(406328)

except ImportError:
    pass


def it():
    _l_(406346)

    df = _c_(406334, _a_(406333, _c_(406332, _a_(406331, _a_(406330, _n_(406329, "np", lambda: np), "random"), "randn"), 1000), "reshape"), -1,1)
    _l_(406335)
    _c_(406343, _a_(406341, _c_(406340, _a_(406338, _c_(406337, _n_(406336, "NearestNeighbors", lambda: NearestNeighbors), n_neighbors=2, p=2), "fit"), _n_(406339, "df", lambda: df)), "kneighbors"), _n_(406342, "df", lambda: df))
    _l_(406344)
    yield 1
    _l_(406345)

f = lambda x: 1
_l_(406347)
with _c_(406349, _n_(406348, "parallel_backend", lambda: parallel_backend), "loky", inner_max_num_threads=1):
    _l_(406361)

    res = _c_(406359, _c_(406351, _n_(406350, "Parallel", lambda: Parallel), n_jobs=2), (_c_(406356, _c_(406354, _n_(406352, "delayed", lambda: delayed), _n_(406353, "f", lambda: f)), _n_(406355, "p", lambda: p)) for p in  _c_(406358, _n_(406357, "it", lambda: it))))
    _l_(406360)