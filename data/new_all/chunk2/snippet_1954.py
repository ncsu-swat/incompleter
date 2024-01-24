# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/75893246/python-prefect-2-9-0-typeerror-fn-must-be-callable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
@_n_(475603, "task", lambda: task)
def print_values():
    _l_(475612)

    _c_(475610, _n_(475604, "print", lambda: print), "Test 1: "+ _c_(475609, _a_(475608, _c_(475607, _a_(475606, _n_(475605, "datetime", lambda: datetime), "now")), "strftime"), "%H:%M:%S"))
    _l_(475611)

with _c_(475614, _n_(475613, "Flow", lambda: Flow), "my-flow") as flow:
    _l_(475618)

    _c_(475616, _n_(475615, "print_values", lambda: print_values))
    _l_(475617)

_c_(475625, _a_(475620, _n_(475619, "flow", lambda: flow), "run_config"), {"scheduler": _c_(475624, _n_(475621, "IntervalSchedule", lambda: IntervalSchedule), interval=_c_(475623, _n_(475622, "timedelta", lambda: timedelta), seconds=10))}
)
_l_(475626)