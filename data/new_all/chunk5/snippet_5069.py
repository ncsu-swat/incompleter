# LExecutor: DO NOT INSTRUMENT

#Source: https://stackoverflow.com/questions/52726959/i-have-a-problem-with-this-error-message-typeerror-unsupported-operand-types
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import csv
    _l_(700677)

except ImportError:
    pass
try:
    import random
    _l_(700679)

except ImportError:
    pass
try:
    import math
    _l_(700681)

except ImportError:
    pass
try:
    import operator
    _l_(700683)

except ImportError:
    pass

with _c_(700685, _n_(700684, "open", lambda: open), 'iris.csv', 'r') as csvfile:
    _l_(700699)

    lines = _c_(700689, _a_(700687, _n_(700686, "csv", lambda: csv), "reader"), _n_(700688, "csvfile", lambda: csvfile))
    _l_(700690)
    for row in _n_(700691, "lines", lambda: lines):
        _l_(700698)

        _c_(700696, _n_(700692, "print", lambda: print), _c_(700695, _a_(700693, ', ', "join"), _n_(700694, "row", lambda: row)))
        _l_(700697)