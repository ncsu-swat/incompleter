# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1207406/how-to-remove-items-from-a-list-while-iterating
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_n_(62141, "somelist", lambda: somelist)[:] = _c_(62147, _n_(62142, "filter", lambda: filter), lambda tup: not _c_(62145, _n_(62143, "determine", lambda: determine), _n_(62144, "tup", lambda: tup)), _n_(62146, "somelist", lambda: somelist))
_l_(62148)
try:
    from itertools import ifilterfalse
    _l_(62150)

except ImportError:
    pass
_n_(62151, "somelist", lambda: somelist)[:] = _c_(62157, _n_(62152, "list", lambda: list), _c_(62156, _n_(62153, "ifilterfalse", lambda: ifilterfalse), _n_(62154, "determine", lambda: determine), _n_(62155, "somelist", lambda: somelist)))
_l_(62158)

