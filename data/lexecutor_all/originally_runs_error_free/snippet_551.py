# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/993358/creating-a-range-of-dates-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
        import datetime as dt
        _l_(1544534)

except ImportError:
        pass
try:
        from dateutil.relativedelta import relativedelta
        _l_(1544536)

except ImportError:
        pass

def month_range(start_date, n_months):
        _l_(1544546)

        for m in _c_(1544539, _n_(1544537, "range", lambda: range), _n_(1544538, "n_months", lambda: n_months)):
                _l_(1544545)

                yield _n_(1544540, "start_date", lambda: start_date) + _c_(1544543, _n_(1544541, "relativedelta", lambda: relativedelta), months=+_n_(1544542, "m", lambda: m))
                _l_(1544544)

