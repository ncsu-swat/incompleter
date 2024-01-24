# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50346338/typeerror-write-points-got-multiple-values-for-argument-time-precision-to-i
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from influxdb import InfluxDBClient
    _l_(548334)

except ImportError:
    pass
try:
    from influxdb import DataFrameClient
    _l_(548336)

except ImportError:
    pass
try:
    import pandas as pd
    _l_(548338)

except ImportError:
    pass
Host_IP = 'XXXXXXXX'
_l_(548339)
Port = _n_(548340, "XXXX", lambda: XXXX)
_l_(548341)
User = 'XXXX'
_l_(548342)
Password = 'XXX'
_l_(548343)
DB_Name = 'XXXX'
_l_(548344)
client = _c_(548351, _n_(548345, "InfluxDBClient", lambda: InfluxDBClient), _n_(548346, "Host_IP", lambda: Host_IP), _n_(548347, "Port", lambda: Port), _n_(548348, "User", lambda: User), _n_(548349, "Password", lambda: Password),_n_(548350, "DB_Name", lambda: DB_Name))
_l_(548352)
df = _c_(548362, _a_(548354, _n_(548353, "pd", lambda: pd), "DataFrame"), data=_c_(548358, _n_(548355, "list", lambda: list), _c_(548357, _n_(548356, "range", lambda: range), 30)),index=_c_(548361, _a_(548360, _n_(548359, "pd", lambda: pd), "date_range"), start='2014-11-16',periods=30, freq='H'))
_l_(548363)
_c_(548367, _a_(548365, _n_(548364, "client", lambda: client), "write_points"), _n_(548366, "df", lambda: df), 'demo',{'k1': 'v1', 'k2': 'v2'}, time_precision=None, protocol='json')
_l_(548368)