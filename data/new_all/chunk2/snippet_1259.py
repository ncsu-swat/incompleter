# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/61715302/i-get-the-following-error-attributeerror-enter-when-only-using-one-with-blo
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
with _n_(432775, "filename", lambda: filename) as file_object:
    _l_(432780)

    lines=_c_(432778, _a_(432777, _n_(432776, "file_object", lambda: file_object), "readlines"))
    _l_(432779)

for line in _n_(432781, "lines", lambda: lines):
    _l_(432788)

    _c_(432786, _n_(432782, "print", lambda: print), _c_(432785, _a_(432784, _n_(432783, "line", lambda: line), "strip")))
    _l_(432787)