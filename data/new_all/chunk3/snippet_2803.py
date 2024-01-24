# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/62732790/apply-a-function-to-columns-in-pandas-raises-attributeerror
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
sample_dict = {'isDuplicate': {'1051681551': False, '1037545402': True, '1035390559': False},
               'dateTime': {'1051681551': _c_(538073, _n_(538072, "Timestamp", lambda: Timestamp), '2019-01-29 09:09:00+0000', tz='UTC'),
               '1037545402': _c_(538075, _n_(538074, "Timestamp", lambda: Timestamp), '2019-01-11 02:06:00+0000', tz='UTC'),
               '1035390559': _c_(538077, _n_(538076, "Timestamp", lambda: Timestamp), '2019-01-08 14:35:00+0000', tz='UTC')},
               'dateTimePub': {'1051681551': None, '1037545402': None, '1035390559': None}}
_l_(538078)

df = _c_(538083, _a_(538081, _a_(538080, _n_(538079, "pd", lambda: pd), "DataFrame"), "from_dict"), _n_(538082, "sample_dict", lambda: sample_dict))
_l_(538084)