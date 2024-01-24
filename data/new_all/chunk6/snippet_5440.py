# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/50553835/attributeerror-occurs-in-datetime-expression
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from datetime import datetime
    _l_(374149)

except ImportError:
    pass

s = 'Hello, Pythoneers'
_l_(374150)
_c_(374158, _n_(374151, "print", lambda: print), _n_(374152, "s", lambda: s) == _c_(374157, _n_(374153, "eval", lambda: eval), _c_(374156, _n_(374154, "repr", lambda: repr), _n_(374155, "s", lambda: s))))  # no errors here
_l_(374159)  # no errors here

today = _c_(374162, _a_(374161, _n_(374160, "datetime", lambda: datetime), "now"))
_l_(374163)
_c_(374171, _n_(374164, "print", lambda: print), _n_(374165, "today", lambda: today) == _c_(374170, _n_(374166, "eval", lambda: eval), _c_(374169, _n_(374167, "repr", lambda: repr), _n_(374168, "today", lambda: today)))) # error occurs here
_l_(374172) # error occurs here