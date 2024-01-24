# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/67260107/attributeerror-module-matplotlib-cbook-has-no-attribute-check-in-list
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(605150)

except ImportError:
    pass
try:
    import matplotlib.pyplot as plt
    _l_(605152)

except ImportError:
    pass

_n_(605153, "df", lambda: df)['Month'] = _c_(605157, _a_(605155, _n_(605154, "pd", lambda: pd), "to_datetime"), _n_(605156, "df", lambda: df)['Month'], infer_datetime_format = True)
_l_(605158)
df = _c_(605161, _a_(605160, _n_(605159, "df", lambda: df), "set_index"), 'Month',inplace=False)    
_l_(605162)    
# plot graph
_c_(605165, _a_(605164, _n_(605163, "plt", lambda: plt), "xlabel"), 'date')
_l_(605166)
_c_(605169, _a_(605168, _n_(605167, "plt", lambda: plt), "ylabel"), 'trafic flow count')
_l_(605170)
_c_(605174, _a_(605172, _n_(605171, "plt", lambda: plt), "plot"), _n_(605173, "df", lambda: df))
_l_(605175)