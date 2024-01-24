# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/55629181/calibration-and-holdout-data-attributeerror-int-object-has-no-attribute-n
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from lifetimes.utils import calibration_and_holdout_data
    _l_(388243)

except ImportError:
    pass

summary_cal_holdout = _c_(388246, _n_(388244, "calibration_and_holdout_data", lambda: calibration_and_holdout_data), _n_(388245, "df2", lambda: df2), 'person_id', 'effective_date',
                                        calibration_period_end='2017-12-31',
                                        observation_period_end='2018-12-31')
_l_(388247)

_c_(388252, _n_(388248, "print", lambda: print), _c_(388251, _a_(388250, _n_(388249, "summary_cal_holdout", lambda: summary_cal_holdout), "head")))
_l_(388253)