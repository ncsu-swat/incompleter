# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50625975/typeerror-ufunc-true-divide-output-typecode-d-could-not-be-coerced-to-pro
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import numpy as np
    _l_(378899)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(378901)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(378903)

except ImportError:
    pass
try:
    import gower_function as gf
    _l_(378905)

except ImportError:
    pass

# Importing the dataset with pandas
dataset = _c_(378908, _a_(378907, _n_(378906, "pd", lambda: pd), "read_excel"), 'input_partial.xlsx')
_l_(378909)
X = _a_(378912, _a_(378911, _n_(378910, "dataset", lambda: dataset), "iloc")[:, 1:], "values")
_l_(378913)
df = _c_(378917, _a_(378915, _n_(378914, "pd", lambda: pd), "DataFrame"), _n_(378916, "X", lambda: X))
_l_(378918)
#obtaining gower distances of instances
Gower = _c_(378922, _a_(378920, _n_(378919, "gf", lambda: gf), "gower_distances"), _n_(378921, "X", lambda: X))
_l_(378923)