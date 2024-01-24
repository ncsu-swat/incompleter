# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/73471240/typeerror-unsupported-operand-types-for-str-and-datetime-timedelta
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def date_return():
    _l_(542902)

    aux = _n_(542900, "date", lambda: date)
    _l_(542901)
    return aux


_c_(542904, _n_(542903, "date_return", lambda: date_return)) + _c_(542907, _a_(542906, _n_(542905, "datetime", lambda: datetime), "timedelta"), days=10) 
_l_(542908) 