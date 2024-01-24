# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/54917838/attributeerror-module-pandas-has-no-attribute-rolling-mean-temp-append
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(374058, _a_(374045, _n_(374044, "temp", lambda: temp), "append"), _c_(374057, _a_(374056, _c_(374055, _a_(374054, _c_(374053, _a_(374047, _n_(374046, "pd", lambda: pd), "rolling_mean"), _c_(374052, _a_(374049, _n_(374048, "pd", lambda: pd), "pivot_table"), _n_(374050, "telemetry", lambda: telemetry),
   index='datetime',
   columns='machineID',
   values=_n_(374051, "col", lambda: col)), window=24), "resample"), '3H',
        closed='left',
        label='right',
        how='first'), "unstack")))
_l_(374059)