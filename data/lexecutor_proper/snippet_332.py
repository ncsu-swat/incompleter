# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/29576430/shuffle-dataframe-rows
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(62374, _a_(62371, _a_(62370, _n_(62369, "np", lambda: np), "random"), "shuffle"), _a_(62373, _n_(62372, "DataFrame", lambda: DataFrame), "values"))
_l_(62375)

nd = _c_(62380, _a_(62378, _a_(62377, _n_(62376, "sklearn", lambda: sklearn), "utils"), "shuffle"), _n_(62379, "nd", lambda: nd))
_l_(62381)

_c_(62386, _a_(62384, _a_(62383, _n_(62382, "np", lambda: np), "random"), "shuffle"), _n_(62385, "nd", lambda: nd))
_l_(62387)

df = _c_(62392, _a_(62390, _a_(62389, _n_(62388, "sklearn", lambda: sklearn), "utils"), "shuffle"), _n_(62391, "df", lambda: df))
_l_(62393)

_c_(62399, _a_(62396, _a_(62395, _n_(62394, "np", lambda: np), "random"), "shuffle"), _a_(62398, _n_(62397, "df", lambda: df), "values"))
_l_(62400)
try:
    import timeit
    _l_(62402)

except ImportError:
    pass
setup = '''
import numpy as np
import pandas as pd
import sklearn
nd = np.random.random((1000, 100))
df = pd.DataFrame(nd)
'''
_l_(62403)

_c_(62407, _a_(62405, _n_(62404, "timeit", lambda: timeit), "timeit"), 'nd = sklearn.utils.shuffle(nd)', setup=_n_(62406, "setup", lambda: setup), number=1000)
_l_(62408)
_c_(62412, _a_(62410, _n_(62409, "timeit", lambda: timeit), "timeit"), 'np.random.shuffle(nd)', setup=_n_(62411, "setup", lambda: setup), number=1000)
_l_(62413)
_c_(62417, _a_(62415, _n_(62414, "timeit", lambda: timeit), "timeit"), 'df = sklearn.utils.shuffle(df)', setup=_n_(62416, "setup", lambda: setup), number=1000)
_l_(62418)
_c_(62422, _a_(62420, _n_(62419, "timeit", lambda: timeit), "timeit"), 'np.random.shuffle(df.values)', setup=_n_(62421, "setup", lambda: setup), number=1000)
_l_(62423)

