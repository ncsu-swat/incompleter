# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1093322/how-do-i-check-which-version-of-python-is-running-my-script
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import sys
    _l_(1548180)

except ImportError:
    pass
current_version = _c_(1548187, _a_(1548181, ".", "join"), _c_(1548186, _n_(1548182, "map", lambda: map), _n_(1548183, "str", lambda: str), _a_(1548185, _n_(1548184, "sys", lambda: sys), "version_info")[0:2]))
_l_(1548188)

