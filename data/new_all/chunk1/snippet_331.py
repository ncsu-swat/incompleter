# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/51876460/getting-tensorflow-s-is-not-valid-scope-name-error-while-i-am-trying-to-creat
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(379109)

except ImportError:
    pass
try:
    import tensorflow as tf
    _l_(379111)

except ImportError:
    pass
try:
    import numpy as np
    _l_(379113)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(379115)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(379117)

except ImportError:
    pass
try:
    from sklearn import metrics
    _l_(379119)

except ImportError:
    pass
try:
    from IPython import display
    _l_(379121)

except ImportError:
    pass
try:
    from tensorflow.python.data import Dataset
    _l_(379123)

except ImportError:
    pass
_c_(379130, _a_(379126, _a_(379125, _n_(379124, "tf", lambda: tf), "logging"), "set_verbosity"), _a_(379129, _a_(379128, _n_(379127, "tf", lambda: tf), "logging"), "ERROR"))
_l_(379131)
_a_(379134, _a_(379133, _n_(379132, "pd", lambda: pd), "options"), "display").max_rows = 5
_l_(379135)
_a_(379138, _a_(379137, _n_(379136, "pd", lambda: pd), "options"), "display").float_format = _a_(379139, '{:.1f}', "format")
_l_(379140)

housing_data = _c_(379143, _a_(379142, _n_(379141, "pd", lambda: pd), "read_csv"), "train.csv")
_l_(379144)
housing_data = _c_(379153, _a_(379146, _n_(379145, "housing_data", lambda: housing_data), "reindex"), _c_(379152, _a_(379149, _a_(379148, _n_(379147, "np", lambda: np), "random"), "permutation"), _a_(379151, _n_(379150, "housing_data", lambda: housing_data), "index")))
_l_(379154)
housing_data = _c_(379160, _a_(379159, _c_(379158, _a_(379156, _n_(379155, "pd", lambda: pd), "get_dummies"), _n_(379157, "housing_data", lambda: housing_data)), "dropna"))
_l_(379161)