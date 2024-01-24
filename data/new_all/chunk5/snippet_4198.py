# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61775499/pivot-table-function-not-working-attributeerror-numpy-ndarray-object-has-no
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
no_row_df = _c_(671888, _a_(671884, _n_(671883, "pd", lambda: pd), "pivot_table"), _n_(671885, "no_row_data", lambda: no_row_data), values = "FINALWT", index = ["SURVDATE", "PROV"], aggfunc=_a_(671887, _n_(671886, "np", lambda: np), "sum"))
_l_(671889)
for col in _n_(671890, "count_columns", lambda: count_columns):
    _l_(671904)

    table = _c_(671897, _a_(671892, _n_(671891, "pd", lambda: pd), "pivot_table"), _n_(671893, "no_row_data", lambda: no_row_data), values = "FINALWT", index = ["SURVDATE", "PROV"], columns=[_n_(671894, "col", lambda: col)], aggfunc=_a_(671896, _n_(671895, "np", lambda: np), "sum"))
    _l_(671898)
    no_row_df = _c_(671902, _a_(671900, _n_(671899, "df", lambda: df), "merge"), _n_(671901, "table", lambda: table), left_index=True, right_on=["SURVDATE", "PROV"])
    _l_(671903)
_n_(671905, "no_row_df", lambda: no_row_df)
_l_(671906)