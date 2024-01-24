# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/69001132/use-zip-to-combine-list-with-dataframe-attributeerror-str-object-has-no-att
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
final_dataset_list = []
_l_(426957)
for date, df in _c_(426961, _n_(426958, "zip", lambda: zip), _n_(426959, "date_list", lambda: date_list), _n_(426960, "df_dataset", lambda: df_dataset)):
    _l_(426979)

    if _c_(426964, _n_(426962, "len", lambda: len), _n_(426963, "df", lambda: df)) == 0:
        _l_(426966)

        continue
        _l_(426965)
    _a_(426968, _n_(426967, "df", lambda: df), "loc")[:, 'date'] = _c_(426972, _a_(426970, _n_(426969, "pd", lambda: pd), "to_datetime"), _n_(426971, "date", lambda: date))
    _l_(426973)
    _c_(426977, _a_(426975, _n_(426974, "final_dataset_list", lambda: final_dataset_list), "append"), _n_(426976, "df", lambda: df))
    _l_(426978)