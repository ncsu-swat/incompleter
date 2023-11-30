# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/733454/best-way-to-format-integer-as-string-with-leading-zeros
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
add_nulls = lambda number, zero_count : _c_(1539002, _a_(1538999, "{0:0{1}d}", "format"), _n_(1539000, "number", lambda: number), _n_(1539001, "zero_count", lambda: zero_count))
_l_(1539003)

_c_(1539005, _n_(1539004, "add_nulls", lambda: add_nulls), 2,3)
_l_(1539006)
'002'
_l_(1539007)

