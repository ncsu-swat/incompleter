# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/60443038/pandas-date-range-query-gives-typeerror-series-objects-are-mutable-thus-the
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df_contracts = _c_(677607, _n_(677606, "read_csv", lambda: read_csv), "_raw_contracts.csv")
_l_(677608)
_n_(677609, "df_contracts", lambda: df_contracts)['Start'] = _c_(677613, _a_(677611, _n_(677610, "pd", lambda: pd), "to_datetime"), _n_(677612, "df_contracts", lambda: df_contracts)['Start'])
_l_(677614)
_n_(677615, "df_contracts", lambda: df_contracts)['End'] = _c_(677619, _a_(677617, _n_(677616, "pd", lambda: pd), "to_datetime"), _n_(677618, "df_contracts", lambda: df_contracts)['End'])
_l_(677620)
anchor = _c_(677623, _a_(677622, _n_(677621, "pd", lambda: pd), "Timestamp"), '2010-01-01T12')
_l_(677624)
df = _c_(677629, _a_(677626, _n_(677625, "df_contracts", lambda: df_contracts), "loc"), _n_(677627, "df_contracts", lambda: df_contracts)['Start'] < _n_(677628, "anchor", lambda: anchor)) & (_n_(677630, "df_contracts", lambda: df_contracts)['End'] > _n_(677631, "anchor", lambda: anchor))
_l_(677632)