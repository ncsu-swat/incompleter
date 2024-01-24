# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/64749731/cant-subtract-hours-from-time-data-because-of-data-type-error
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(635873, "df", lambda: df)['Hours'] = _c_(635876, _a_(635875, _n_(635874, "df", lambda: df)['Hours'], "astype"), 'datetime64')
_l_(635877)
_n_(635878, "df", lambda: df)['Hours'] = _a_(635884, _a_(635883, _c_(635882, _a_(635880, _n_(635879, "pd", lambda: pd), "to_datetime"), _n_(635881, "df", lambda: df)['Hours']), "dt"), "time")
_l_(635885)
_n_(635886, "df", lambda: df)['Hours'] = _c_(635893, _a_(635892, _a_(635891, _c_(635890, _a_(635888, _n_(635887, "pd", lambda: pd), "to_datetime"), _n_(635889, "df", lambda: df)['Hours']), "dt"), "floor"), 'd')
_l_(635894)