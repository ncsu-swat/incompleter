# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69088617/typeerror-can-not-infer-schema-for-type-class-datetime-timedelta
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df_dif=_c_(452984, _a_(452981, _a_(452980, _n_(452979, "df_lag_drp", lambda: df_lag_drp), "rdd"), "map"), lambda x: (_n_(452982, "x", lambda: x)["prev_row_startdate"]-_n_(452983, "x", lambda: x)["FINISH_DATE"]))
_l_(452985)