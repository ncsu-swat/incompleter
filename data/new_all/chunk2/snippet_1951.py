# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/76004091/nameerror-looking-for-function-when-using-parallel-apply-from-pandarallel
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
df_transport_hourly = _c_(466282, _a_(466278, _c_(466277, _a_(466270, _n_(466269, "df_db_transport", lambda: df_db_transport), "groupby"), ['siteId', 'port', 'systemName', _a_(466273, _a_(466272, _n_(466271, "df_db_transport", lambda: df_db_transport)['startedAt'], "dt"), "date"), _a_(466276, _a_(466275, _n_(466274, "df_db_transport", lambda: df_db_transport)['startedAt'], "dt"), "hour")]), "parallel_apply"), lambda x: _c_(466281, _n_(466279, "calc_transport", lambda: calc_transport), _n_(466280, "x", lambda: x), 'h'))
_l_(466283)