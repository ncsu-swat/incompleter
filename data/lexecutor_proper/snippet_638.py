# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1158076/implement-touch-using-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import os
    _l_(63961)

except ImportError:
    pass
def func(filename):
    _l_(63978)

    if _c_(63966, _a_(63964, _a_(63963, _n_(63962, "os", lambda: os), "path"), "exists"), _n_(63965, "filename", lambda: filename)):
        _l_(63977)

        _c_(63970, _a_(63968, _n_(63967, "os", lambda: os), "utime"), _n_(63969, "filename", lambda: filename))
        _l_(63971)
    else:
        with _c_(63974, _n_(63972, "open", lambda: open), _n_(63973, "filename", lambda: filename),'a') as f:
            _l_(63976)

            pass
            _l_(63975)

_c_(63984, _a_(63980, _n_(63979, "os", lambda: os), "utime"), _n_(63981, "filename", lambda: filename),(_n_(63982, "atime", lambda: atime),_n_(63983, "mtime", lambda: mtime)))
_l_(63985)

