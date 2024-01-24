# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/71022019/attributeerror-partially-initialized-module-x-has-no-attribute-y-most-likely-d
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(411880)

except ImportError:
    pass


df = _c_(411883, _a_(411882, _n_(411881, "pd", lambda: pd), "read_csv"), 'latex.csv')
_l_(411884)