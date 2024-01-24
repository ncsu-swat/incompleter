# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64749731/cant-subtract-hours-from-time-data-because-of-data-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _c_(586369, _a_(586368, _c_(586367, _a_(586366, _n_(586364, "df", lambda: df)[_n_(586365, "df", lambda: df)["Hour"] < 0], "all")), "all"))  and _c_(586374, _a_(586373, _c_(586372, _a_(586371, _n_(586370, "df", lambda: df)["Hours"], "all")), "all")) != -12.1:
    _l_(586383)

    _n_(586375, "df", lambda: df)["EndTime"] = _c_(586379, _a_(586377, _n_(586376, "pd", lambda: pd), "to_datetime"), _n_(586378, "df", lambda: df)["EndTime"]) - _c_(586381, _n_(586380, "timedelta", lambda: timedelta), hours=12) 
    _l_(586382) 