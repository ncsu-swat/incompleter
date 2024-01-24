# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64760543/filenotfounderror-when-i-read-a-file
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import tensorflow
    _l_(591133)

except ImportError:
    pass
try:
    import keras
    _l_(591135)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(591137)

except ImportError:
    pass
try:
    import numpy as np
    _l_(591139)

except ImportError:
    pass
try:
    import sklearn
    _l_(591141)

except ImportError:
    pass
try:
    from sklearn import linear_model
    _l_(591143)

except ImportError:
    pass
try:
    from sklearn.utils import shuffle
    _l_(591145)

except ImportError:
    pass


data = _c_(591148, _a_(591147, _n_(591146, "pd", lambda: pd), "read_csv"), "student-mat.csv", sep=";")
_l_(591149)

data = _n_(591150, "data", lambda: data)[["G1","G2","G3","studytime","failures","absences"]]
_l_(591151)

_c_(591156, _n_(591152, "print", lambda: print), _c_(591155, _a_(591154, _n_(591153, "data", lambda: data), "head")))
_l_(591157)