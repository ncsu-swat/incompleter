# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/8142364/how-to-compare-two-dates
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import datetime
    _l_(1541357)

except ImportError:
    pass

eight_am = _c_(1541360, _a_(1541359, _n_(1541358, "datetime", lambda: datetime), "time"), 8,0,0 ) # Time, without a date
_l_(1541361) # Time, without a date

_c_(1541367, _a_(1541366, _c_(1541365, _a_(1541364, _a_(1541363, _n_(1541362, "datetime", lambda: datetime), "datetime"), "now")), "time")) > _n_(1541368, "eight_am", lambda: eight_am)  
_l_(1541369)  

