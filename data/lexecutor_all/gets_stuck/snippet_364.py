# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/377454/how-do-i-get-my-program-to-sleep-for-50-milliseconds
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import time
    _l_(1540596)

except ImportError:
    pass
_c_(1540598, _n_(1540597, "print", lambda: print), "0.00 seconds")
_l_(1540599)
_c_(1540602, _a_(1540601, _n_(1540600, "time", lambda: time), "sleep"), 0.05) # 50 milliseconds... make sure you put time. if you import time!
_l_(1540603) # 50 milliseconds... make sure you put time. if you import time!
_c_(1540605, _n_(1540604, "print", lambda: print), "0.05 seconds")
_l_(1540606)
try:
    from time import sleep
    _l_(1540608)

except ImportError:
    pass
_c_(1540610, _n_(1540609, "print", lambda: print), "0.00 sec")
_l_(1540611)
_c_(1540613, _n_(1540612, "sleep", lambda: sleep), 0.05) # Don't put time. this time, as it will be confused. You did
_l_(1540614) # Don't put time. this time, as it will be confused. You did
            # not import the whole module
_c_(1540616, _n_(1540615, "print", lambda: print), "0.05 sec")
_l_(1540617)

time_not_passed = True
_l_(1540618)
try:
    from time import time
    _l_(1540620)

except ImportError:
    pass

init_time = _c_(1540622, _n_(1540621, "time", lambda: time)) # Or time.time() if whole module imported
_l_(1540623) # Or time.time() if whole module imported
_c_(1540625, _n_(1540624, "print", lambda: print), "0.00 secs")
_l_(1540626)
while True:
    _l_(1540636)

    if _n_(1540627, "init_time", lambda: init_time) + 0.05 <= _c_(1540629, _n_(1540628, "time", lambda: time)) and _n_(1540630, "time_not_passed", lambda: time_not_passed):
        _l_(1540635)

        _c_(1540632, _n_(1540631, "print", lambda: print), "0.05 secs")
        _l_(1540633)
        time_not_passed = False
        _l_(1540634)

