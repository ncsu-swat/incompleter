# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/46586419/python-attributeerror-nonetype-object-has-no-attribute-fileno
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime as dt
    _l_(437821)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(437823)

except ImportError:
    pass
try:
    from matplotlib import style
    _l_(437825)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(437827)

except ImportError:
    pass
try:
    import pandas_datareader.data as web
    _l_(437829)

except ImportError:
    pass
try:
    import numpy as np
    _l_(437831)

except ImportError:
    pass
_c_(437834, _a_(437833, _n_(437832, "style", lambda: style), "use"), 'ggplot')
_l_(437835)
start=_c_(437838, _a_(437837, _n_(437836, "dt", lambda: dt), "datetime"), 2000,1,1)
_l_(437839)
end=_c_(437842, _a_(437841, _n_(437840, "dt", lambda: dt), "datetime"), 2016,12,31)
_l_(437843)
df= _c_(437848, _a_(437845, _n_(437844, "web", lambda: web), "DataReader"), 'ERIE', 'google', _n_(437846, "start", lambda: start), _n_(437847, "end", lambda: end))
_l_(437849)
_c_(437854, _n_(437850, "print", lambda: print), _c_(437853, _a_(437852, _n_(437851, "df", lambda: df), "head")))
_l_(437855)