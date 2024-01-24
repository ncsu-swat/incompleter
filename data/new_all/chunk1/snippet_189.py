# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60280466/merging-two-dataframes-with-pd-na-in-merge-column-yields-typeerror-boolean-val
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(399152, _a_(399149, _n_(399147, "df", lambda: df)[_n_(399148, "some_column", lambda: some_column)], "fillna"), _a_(399151, _n_(399150, "np", lambda: np), "nan"), inplace=True)
_l_(399153)
_c_(399159, _a_(399156, _n_(399154, "df2", lambda: df2)[_n_(399155, "some_column", lambda: some_column)], "fillna"), _a_(399158, _n_(399157, "np", lambda: np), "nan"), inplace=True)
_l_(399160)
df = _c_(399165, _a_(399162, _n_(399161, "df", lambda: df), "merge"), _n_(399163, "df2", lambda: df2), on=_n_(399164, "some_column", lambda: some_column))
_l_(399166)
# Works