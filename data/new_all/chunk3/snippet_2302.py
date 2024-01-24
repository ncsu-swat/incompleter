# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52749012/python-typeerror-1-is-not-a-string
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(522989)

except ImportError:
    pass
try:
    import matplotlib.pylab as plt
    _l_(522991)

except ImportError:
    pass

data = _c_(522994, _a_(522993, _n_(522992, "pd", lambda: pd), "read_csv"), 'sedimento.csv', encoding ='latin-1', delimiter=';', decimal=',')
_l_(522995)