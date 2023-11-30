# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/13890935/does-pythons-time-time-return-the-local-or-utc-timestamp
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(1542987)

except ImportError:
    pass

local_time = _c_(1542991, _a_(1542990, _a_(1542989, _n_(1542988, "datetime", lambda: datetime), "datetime"), "now"))
_l_(1542992)
_c_(1542997, _n_(1542993, "print", lambda: print), _c_(1542996, _a_(1542995, _n_(1542994, "local_time", lambda: local_time), "strftime"), '%Y%m%d %H%M%S'))
_l_(1542998)

utc_time = _c_(1543002, _a_(1543001, _a_(1543000, _n_(1542999, "datetime", lambda: datetime), "datetime"), "utcnow")) 
_l_(1543003) 
_c_(1543008, _n_(1543004, "print", lambda: print), _c_(1543007, _a_(1543006, _n_(1543005, "utc_time", lambda: utc_time), "strftime"), '%Y%m%d %H%M%S'))
_l_(1543009)

