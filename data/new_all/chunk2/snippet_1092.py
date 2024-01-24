# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64236575/file-not-found-error-in-jupyter-lab-using-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(447677)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(447679)

except ImportError:
    pass
try:
    from collections import Counter
    _l_(447681)

except ImportError:
    pass
try:
    import seaborn as sns
    _l_(447683)

except ImportError:
    pass

df = _c_(447686, _a_(447685, _n_(447684, "pd", lambda: pd), "read_csv"), 'demo/big.csv')
_l_(447687)

_c_(447690, _n_(447688, "print", lambda: print), _n_(447689, "df", lambda: df))
_l_(447691)