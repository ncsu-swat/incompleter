# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/5137497/find-the-current-directory-and-files-directory
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import pathlib
    _l_(1547625)

except ImportError:
    pass
filepath = _a_(1547632, _c_(1547631, _a_(1547630, _c_(1547629, _a_(1547627, _n_(1547626, "pathlib", lambda: pathlib), "Path"), _n_(1547628, "__file__", lambda: __file__)), "resolve")), "parent")
_l_(1547633)

