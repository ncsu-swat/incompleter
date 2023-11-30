# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13703720/converting-between-datetime-timestamp-and-datetime64
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(1543043)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(1543045)

except ImportError:
    pass

class NumpyConverter(_n_(1543046, "object", lambda: object)):
    _l_(1543087)

    @_n_(1543047, "classmethod", lambda: classmethod)
    def to_datetime(cls, dt64, tzinfo=None):
        _l_(1543086)

        """
        Converts a Numpy datetime64 to a Python datetime.
        :param dt64: A Numpy datetime64 variable
        :type dt64: numpy.datetime64
        :param tzinfo: The timezone the date / time value is in
        :type tzinfo: pytz.timezone
        :return: A Python datetime variable
        :rtype: datetime
        """
        ts = _c_(1543051, _a_(1543049, _n_(1543048, "pd", lambda: pd), "to_datetime"), _n_(1543050, "dt64", lambda: dt64))
        _l_(1543052)
        if _n_(1543053, "tzinfo", lambda: tzinfo) is not None:
            _l_(1543070)

            aux = _c_(1543068, _n_(1543054, "datetime", lambda: datetime), _a_(1543056, _n_(1543055, "ts", lambda: ts), "year"), _a_(1543058, _n_(1543057, "ts", lambda: ts), "month"), _a_(1543060, _n_(1543059, "ts", lambda: ts), "day"), _a_(1543062, _n_(1543061, "ts", lambda: ts), "hour"), _a_(1543064, _n_(1543063, "ts", lambda: ts), "minute"), _a_(1543066, _n_(1543065, "ts", lambda: ts), "second"), tzinfo=_n_(1543067, "tzinfo", lambda: tzinfo))
            _l_(1543069)
            return aux
        aux = _c_(1543084, _n_(1543071, "datetime", lambda: datetime), _a_(1543073, _n_(1543072, "ts", lambda: ts), "year"), _a_(1543075, _n_(1543074, "ts", lambda: ts), "month"), _a_(1543077, _n_(1543076, "ts", lambda: ts), "day"), _a_(1543079, _n_(1543078, "ts", lambda: ts), "hour"), _a_(1543081, _n_(1543080, "ts", lambda: ts), "minute"), _a_(1543083, _n_(1543082, "ts", lambda: ts), "second"))
        _l_(1543085)
        return aux

