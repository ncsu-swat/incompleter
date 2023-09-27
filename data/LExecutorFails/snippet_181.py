# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/237079/how-do-i-get-file-creation-and-modification-date-times
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from crtime import get_crtimes_in_dir
    _l_(1546043)

except ImportError:
    pass

for fname, date in _c_(1546045, _n_(1546044, "get_crtimes_in_dir", lambda: get_crtimes_in_dir), ".", raise_on_error=True, as_epoch=False):
    _l_(1546051)

    _c_(1546049, _n_(1546046, "print", lambda: print), _n_(1546047, "fname", lambda: fname), _n_(1546048, "date", lambda: date))
    _l_(1546050)

