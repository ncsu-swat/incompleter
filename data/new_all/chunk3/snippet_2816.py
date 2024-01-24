# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62163197/typeerror-passing-series-with-dtype-int-to-dateutil-relativedelta
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_a_(543511, _n_(543510, "df", lambda: df), "loc")[:,'calc_eli_date'] = (
    _c_(543515, _a_(543513, _n_(543512, "datetime", lambda: datetime), "datetime"), _n_(543514, "df", lambda: df)['pol_eff_date'])
    + _c_(543518, _n_(543516, "relativedelta", lambda: relativedelta), years=_n_(543517, "df", lambda: df)['frt_elig_year'])
)
_l_(543519)