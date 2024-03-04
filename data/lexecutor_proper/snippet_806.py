# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2225564/get-a-filtered-list-of-files-in-a-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
files = [_n_(65059, "f", lambda: f) for f in _c_(65062, _a_(65061, _n_(65060, "os", lambda: os), "listdir"), '.') if _c_(65066, _a_(65064, _n_(65063, "re", lambda: re), "match"), r'[0-9]+.*\.jpg', _n_(65065, "f", lambda: f))]
_l_(65067)

