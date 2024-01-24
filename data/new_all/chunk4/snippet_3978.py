# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64749731/cant-subtract-hours-from-time-data-because-of-data-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(611970, "df", lambda: df)['Hours'] = _c_(611973, _a_(611972, _n_(611971, "df", lambda: df)['Hours'], "astype"), 'datetime64')
_l_(611974)
_n_(611975, "df", lambda: df)['Hours'] = _a_(611981, _a_(611980, _c_(611979, _a_(611977, _n_(611976, "pd", lambda: pd), "to_datetime"), _n_(611978, "df", lambda: df)['Hours']), "dt"), "time")
_l_(611982)
_n_(611983, "df", lambda: df)['Hours'] = _c_(611990, _a_(611989, _a_(611988, _c_(611987, _a_(611985, _n_(611984, "pd", lambda: pd), "to_datetime"), _n_(611986, "df", lambda: df)['Hours']), "dt"), "floor"), 'd')
_l_(611991)