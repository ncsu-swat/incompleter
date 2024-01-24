# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/42694112/when-using-pathlib-getting-error-typeerror-invalid-file-posixpathexample-t
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pathlib import Path
    _l_(379472)

except ImportError:
    pass

filename = _a_(379476, _c_(379475, _n_(379473, "Path", lambda: Path), _n_(379474, "__file__", lambda: __file__)), "parent") / "example.txt"
_l_(379477)
contents = _c_(379482, _a_(379481, _c_(379480, _n_(379478, "open", lambda: open), _n_(379479, "filename", lambda: filename), "r"), "read"))
_l_(379483)