# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61717953/pytest-custom-exception-typeerror-exceptions-must-be-derived-from-baseexcep
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from pyupurs.exceptions import FileIsEmptyError
    _l_(426219)

except ImportError:
    pass

...
_l_(426220)

with _c_(426224, _a_(426222, _n_(426221, "pytest", lambda: pytest), "raises"), _n_(426223, "FileIsEmptyError", lambda: FileIsEmptyError)):
    _l_(426227)

    raise _n_(426225, "FileIsEmptyError", lambda: FileIsEmptyError)
    _l_(426226)