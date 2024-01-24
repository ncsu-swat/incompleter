# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/58672758/typeerror-data-type-not-understood-while-parsing-csv-with-pandas
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pandas as pd
    _l_(406118)

except ImportError:
    pass
try:
    import datetime as datetime
    _l_(406120)

except ImportError:
    pass

data = _c_(406123, _a_(406122, _n_(406121, "pd", lambda: pd), "read_csv"), "scans.csv")
_l_(406124)

# dtypes = {
#     'date': datetime,
#     'muscle': str,
#     'side': str,
#     'MQ(0-100)': float,
#     'MQ(raw)': int,
#     'fat': float
# }
# data = pd.read_csv("scans.csv", dtype=dtypes)

_c_(406129, _n_(406125, "print", lambda: print), _c_(406128, _a_(406127, _n_(406126, "data", lambda: data), "head")))
_l_(406130)
_c_(406134, _n_(406131, "print", lambda: print), _a_(406133, _n_(406132, "data", lambda: data), "dtypes"))
_l_(406135)