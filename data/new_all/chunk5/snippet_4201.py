# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61775499/pivot-table-function-not-working-attributeerror-numpy-ndarray-object-has-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
no_row_df = _c_(706880, _a_(706876, _n_(706875, "pd", lambda: pd), "pivot_table"), _n_(706877, "no_row_data", lambda: no_row_data), values = "FINALWT", index = ["SURVDATE", "PROV"], aggfunc=_a_(706879, _n_(706878, "np", lambda: np), "sum"))
_l_(706881)
for col in _n_(706882, "count_columns", lambda: count_columns):
    _l_(706896)

    table = _c_(706889, _a_(706884, _n_(706883, "pd", lambda: pd), "pivot_table"), _n_(706885, "no_row_data", lambda: no_row_data), values = "FINALWT", index = ["SURVDATE", "PROV"], columns=[_n_(706886, "col", lambda: col)], aggfunc=_a_(706888, _n_(706887, "np", lambda: np), "sum"))
    _l_(706890)
    no_row_df = _c_(706894, _a_(706892, _n_(706891, "df", lambda: df), "merge"), _n_(706893, "table", lambda: table), left_index=True, right_on=["SURVDATE", "PROV"])
    _l_(706895)
_n_(706897, "no_row_df", lambda: no_row_df)
_l_(706898)