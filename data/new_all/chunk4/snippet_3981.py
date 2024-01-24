# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64749731/cant-subtract-hours-from-time-data-because-of-data-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _c_(596664, _a_(596663, _c_(596662, _a_(596661, _n_(596659, "df", lambda: df)[_n_(596660, "df", lambda: df)["Hour"] < 0], "all")), "all"))  and _c_(596669, _a_(596668, _c_(596667, _a_(596666, _n_(596665, "df", lambda: df)["Hours"], "all")), "all")) != -12.1:
    _l_(596678)

    _n_(596670, "df", lambda: df)["EndTime"] = _c_(596674, _a_(596672, _n_(596671, "pd", lambda: pd), "to_datetime"), _n_(596673, "df", lambda: df)["EndTime"]) - _c_(596676, _n_(596675, "timedelta", lambda: timedelta), hours=12) 
    _l_(596677) 