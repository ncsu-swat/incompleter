# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/34506536/attributeerror-str-object-has-no-attribute-sleep
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time, datetime
    _l_(449766)

except ImportError:
    pass

Year = 2020
_l_(449767)
Month = 12
_l_(449768)
Day = 24
_l_(449769)
Hour = 23
_l_(449770)
Minute = 18
_l_(449771)
Second = 50
_l_(449772)

while True:
    _l_(449807)

    Datetime = _c_(449781, _a_(449774, _n_(449773, "datetime", lambda: datetime), "datetime"), _n_(449775, "Year", lambda: Year), _n_(449776, "Month", lambda: Month), _n_(449777, "Day", lambda: Day), _n_(449778, "Hour", lambda: Hour), _n_(449779, "Minute", lambda: Minute), _n_(449780, "Second", lambda: Second))
    _l_(449782)
    diff = _n_(449783, "Datetime", lambda: Datetime) - _c_(449787, _a_(449786, _a_(449785, _n_(449784, "datetime", lambda: datetime), "datetime"), "now"))
    _l_(449788)
    diff = _c_(449791, _n_(449789, "str", lambda: str), _n_(449790, "diff", lambda: diff))
    _l_(449792)

    days, not_useful, time = _c_(449795, _a_(449794, _n_(449793, "diff", lambda: diff), "split"))
    _l_(449796)

    Day1 = _n_(449797, "days", lambda: days) + " " + "Day" # Day
    _l_(449798) # Day

    _c_(449801, _n_(449799, "print", lambda: print), _n_(449800, "Day1", lambda: Day1))
    _l_(449802)

    _c_(449805, _a_(449804, _n_(449803, "time", lambda: time), "sleep"), 1)
    _l_(449806)