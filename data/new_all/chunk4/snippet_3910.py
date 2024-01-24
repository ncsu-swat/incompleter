# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/65459802/typeerror-on-pandas-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(631509)

except ImportError:
    pass
try:
    from datetime import datetime,timedelta
    _l_(631511)

except ImportError:
    pass

data=_c_(631514, _a_(631513, _n_(631512, "pd", lambda: pd), "read_csv"), "Dataset.csv",low_memory=False)
_l_(631515)
_n_(631516, "data", lambda: data).Date = _c_(631524, _a_(631519, _a_(631518, _n_(631517, "data", lambda: data), "Date"), "apply"), lambda x:_c_(631523, _a_(631521, _n_(631520, "datetime", lambda: datetime), "strptime"), _n_(631522, "x", lambda: x), '%Y-%m-%d'))
_l_(631525)