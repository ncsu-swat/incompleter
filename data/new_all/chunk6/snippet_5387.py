# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/59221078/typeerror-unhashable-type-numpy-ndarray-arima-time-series
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
Combined = _c_(361826, _a_(361824, _n_(361823, "pd", lambda: pd), "read_csv"), _n_(361825, "file_path", lambda: file_path), parse_dates=['Revenue_mth'], index_col = ['Revenue_mth'])
_l_(361827)
_c_(361830, _a_(361829, _n_(361828, "plt", lambda: plt), "xlabel"), 'Date')
_l_(361831)
_c_(361834, _a_(361833, _n_(361832, "plt", lambda: plt), "ylabel"), 'Revenue amount')
_l_(361835)
_c_(361839, _a_(361837, _n_(361836, "plt", lambda: plt), "plot"), _n_(361838, "Combined", lambda: Combined))
_l_(361840)