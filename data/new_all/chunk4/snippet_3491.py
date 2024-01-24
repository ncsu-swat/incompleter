# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73448351/datetime-typeerror-strptime-argument-1-must-be-str-not-timestamp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(588161)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(588163)

except ImportError:
    pass
dataset = _c_(588166, _a_(588165, _n_(588164, "pd", lambda: pd), "read_excel"), "D:\\DataSciencePython/retail_raw_reduced.xltx")
_l_(588167)
_n_(588168, "dataset", lambda: dataset)['order_month'] = _c_(588178, _a_(588170, _n_(588169, "dataset", lambda: dataset)['order_date'], "apply"), lambda x: _c_(588177, _a_(588176, _c_(588175, _a_(588173, _a_(588172, _n_(588171, "datetime", lambda: datetime), "datetime"), "strptime"), _n_(588174, "x", lambda: x), "%Y-%m-%d"), "strftime"), '%Y-%m'))
_l_(588179)
_c_(588184, _n_(588180, "print", lambda: print), _c_(588183, _a_(588182, _n_(588181, "dataset", lambda: dataset), "head")))
_l_(588185)