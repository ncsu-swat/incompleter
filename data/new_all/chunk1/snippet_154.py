# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/37530891/python-pandas-nameerror-stringio-is-not-defined
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(414131)

except ImportError:
    pass

data = 'a,b,c\n1,2,3\n4,5,6'
_l_(414132)

_c_(414138, _a_(414134, _n_(414133, "pd", lambda: pd), "read_csv"), _c_(414137, _n_(414135, "StringIO", lambda: StringIO), _n_(414136, "data", lambda: data)),skipinitialspace=True)
_l_(414139)