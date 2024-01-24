# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73448351/datetime-typeerror-strptime-argument-1-must-be-str-not-timestamp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(645987)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(645989)

except ImportError:
    pass
dataset = _c_(645992, _a_(645991, _n_(645990, "pd", lambda: pd), "read_excel"), "D:\\DataSciencePython/retail_raw_reduced.xltx")
_l_(645993)
_n_(645994, "dataset", lambda: dataset)['order_month'] = _c_(646004, _a_(645996, _n_(645995, "dataset", lambda: dataset)['order_date'], "apply"), lambda x: _c_(646003, _a_(646002, _c_(646001, _a_(645999, _a_(645998, _n_(645997, "datetime", lambda: datetime), "datetime"), "strptime"), _n_(646000, "x", lambda: x), "%Y-%m-%d"), "strftime"), '%Y-%m'))
_l_(646005)
_c_(646010, _n_(646006, "print", lambda: print), _c_(646009, _a_(646008, _n_(646007, "dataset", lambda: dataset), "head")))
_l_(646011)