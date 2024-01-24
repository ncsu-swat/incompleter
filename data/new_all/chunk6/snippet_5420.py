# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54917838/attributeerror-module-pandas-has-no-attribute-rolling-mean-temp-append
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(369485, _a_(369472, _n_(369471, "temp", lambda: temp), "append"), _c_(369484, _a_(369483, _c_(369482, _a_(369481, _c_(369480, _a_(369474, _n_(369473, "pd", lambda: pd), "rolling_mean"), _c_(369479, _a_(369476, _n_(369475, "pd", lambda: pd), "pivot_table"), _n_(369477, "telemetry", lambda: telemetry),
   index='datetime',
   columns='machineID',
   values=_n_(369478, "col", lambda: col)), window=24), "resample"), '3H',
        closed='left',
        label='right',
        how='first'), "unstack")))
_l_(369486)