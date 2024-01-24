# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59063220/typeerror-expected-string-or-bytes-like-object-while-trying-to-plot-data-from-a
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
path = '/Users/pradeepallath/Documents/000_Edureka_Training/001_PredictiveAnalysis/Weather_WWII'
_l_(556073)
try:
    import pandas as pd
    _l_(556075)

except ImportError:
    pass
dataset = _c_(556079, _a_(556077, _n_(556076, "pd", lambda: pd), "read_csv"), _n_(556078, "path", lambda: path)+'/Weather.csv',low_memory=False,nrows=1000)
_l_(556080)
_c_(556083, _a_(556082, _n_(556081, "dataset", lambda: dataset), "plot"), x='MinTemp',y='MaxTemp',style=0)
_l_(556084)
_c_(556087, _a_(556086, _n_(556085, "plt", lambda: plt), "plot"))
_l_(556088)